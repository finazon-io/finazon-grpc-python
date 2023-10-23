PATH_THIS:=$(realpath $(dir $(lastword ${MAKEFILE_LIST})))

PATH_DIST:=${PATH_THIS}/finazon_grpc_python
PATH_PROTO:=proto/finazon_grpc_python/*.proto

PYTHON_VIRTUAL_ENV:=${PATH_THIS}/.venv
PYTHON:=${PYTHON_VIRTUAL_ENV}/bin/python3
PIP:=${PYTHON_VIRTUAL_ENV}/bin/pip
POETRY_VERSION=1.6.1
POETRY=${PYTHON_VIRTUAL_ENV}/bin/poetry

.PHONY: install
install:
	@echo "Create python virual enviroment ..."
	@python3 -m venv ${PYTHON_VIRTUAL_ENV}
	@echo "Install package dependencies ..."
	@mkdir -p ${PATH_DIST}
	@touch ${PATH_DIST}/__init__.py
	@${PIP} install poetry==${POETRY_VERSION}
	@${POETRY} install

.PHONY: generate
generate:
	make install
	@mkdir -p ${PATH_DIST}
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
	@sed -i 's/version = [^ ]*/version = "${VERSION}"/' ${PATH_THIS}/pyproject.toml

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
	@rm -rf ${PYTHON_VIRTUAL_ENV} ${PATH_DIST}
