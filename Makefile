PATH_THIS:=$(realpath $(dir $(lastword ${MAKEFILE_LIST})))

PATH_DIST:=${PATH_THIS}/finazon_grpc_python
PATH_PROTO:=proto/finazon_grpc_python/*.proto

PYTHON_VIRTUAL_ENV:=${PATH_THIS}/.venv
PYTHON:=${PYTHON_VIRTUAL_ENV}/bin/python3
PIP:=${PYTHON_VIRTUAL_ENV}/bin/pip
POETRY_VERSION=1.8.2
POETRY=${PYTHON_VIRTUAL_ENV}/bin/poetry

VERSION_TUPLE := $(subst ., ,$(VERSION))
VERSION_MAJOR := $(word 1,$(VERSION_TUPLE))
VERSION_MINOR := $(word 2,$(VERSION_TUPLE))
VERSION_GRPC := $(VERSION_MAJOR)-$(VERSION_MINOR)

GENERATOR_TEMPLATES_PATH := ${PATH_THIS}/tools/service_generator/templates
GENERATOR_PROTO_PATH := ${PATH_THIS}/proto/finazon_grpc_python
GENERATOR_DEST_PATH := ${PATH_DIST}/
GENERATOR_CMD := ${PATH_THIS}/tools/service_generator/generator.py ${GENERATOR_TEMPLATES_PATH} ${GENERATOR_PROTO_PATH} ${GENERATOR_DEST_PATH}

.PHONY: install
install:
	@echo "Create python virual enviroment ..."
	@python3 -m venv ${PYTHON_VIRTUAL_ENV}
	@echo "Install package dependencies ..."
	@${PIP} install poetry==${POETRY_VERSION}
	@${POETRY} install --with dev

.PHONY: generate
generate:
	make install
	@echo "Generate services ..."
	@${PYTHON} ${GENERATOR_CMD}
	@echo "Generate proto ..."
	@${PYTHON} \
	  -m grpc_tools.protoc \
	  -I./proto \
	  --python_out=. \
	  --grpc_python_out=. \
	  --plugin=protoc-gen-mypy=${PYTHON_VIRTUAL_ENV}/bin/protoc-gen-mypy \
	  --mypy_out=. \
	  ${PATH_PROTO}

.PHONY: bump_version
bump_version:
	@sed -i 's/^version = [^ ]*/version = "${VERSION}"/' ${PATH_THIS}/pyproject.toml
	@sed -i 's/FINAZON_GRPC_VERSION = [^ ]*/FINAZON_GRPC_VERSION = "${VERSION_GRPC}"/' ${PATH_DIST}/common/settings.py

.PHONY: build
build:
	make generate
	@${POETRY} build

.PHONY: publish
publish:
	@${POETRY} config pypi-token.pypi ${PYPI_TOKEN}
	make build
	@${POETRY} publish

.PHONY: publish_test
publish_test:
	@${POETRY} config repositories.test-pypi https://test.pypi.org/legacy/
	@${POETRY} config pypi-token.test-pypi ${PYPI_TOKEN}
	make build
	@${POETRY} publish -r test-pypi

.PHONY: clean
clean:
	@rm -rf ${PYTHON_VIRTUAL_ENV} ${PATH_DIST}/*.py*

.PHONY: export_requirements
export_requirements:
	@${POETRY} export --without-hashes --without dev -f requirements.txt -o requirements.txt
