import typing
from pathlib import Path

import autopep8
from jinja2 import Environment, FileSystemLoader

from tools.service_generator.proto_parser import RpcProtoParser


service_template_file = 'service_template.jinja'
service_file_name_default = '{0}_service.py'
autopep8_options_default = {'max_line_length': 120}


class RpcServiceGenerator:

    def __init__(
            self, templates_path: str, service_file_tpl: typing.Optional[str] = None, autopep8_options: typing.Optional[dict] = None
    ):
        if not service_file_tpl:
            service_file_tpl = service_file_name_default
        self.service_name_tpl = service_file_tpl
        if not autopep8_options:
            autopep8_options = autopep8_options_default
        self.autopep8_options = autopep8_options

        templates_path = Path(templates_path)
        if not templates_path:
            raise Exception(f'Template path {templates_path} is not exists')
        self.tpl_env = Environment(loader=FileSystemLoader(templates_path))

    def run(self, proto_path: str, dest_path: str):
       self.generate_services(proto_path, dest_path)

    def generate_services(self, proto_path: str, dest_path: str):
        dest_path = Path(dest_path)
        if not dest_path.exists():
            raise Exception(f'Dest path {dest_path} is not exists')
        parser = RpcProtoParser(proto_path)
        result = parser.run()
        if len(result) == 0:
            raise Exception(f'Empty result after parsing {proto_path}')
        template = self.tpl_env.get_template(service_template_file)
        for file_desc in result:
            service = file_desc.get_service()
            code = autopep8.fix_code(template.render(service=service, file=file_desc), options=self.autopep8_options)
            service_file_path = dest_path.joinpath(self.service_name_tpl.format(file_desc.get_name_snake()))
            with service_file_path.open('w') as f:
                f.write(code)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Generate services by proto files')
    parser.add_argument('templates_path')
    parser.add_argument('proto_path')
    parser.add_argument('dest_path')
    args = parser.parse_args()
    generator = RpcServiceGenerator(args.templates_path)
    generator.run(
        args.proto_path,
        args.dest_path,
    )
