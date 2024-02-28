import re
import typing
from dataclasses import dataclass, field
from pathlib import Path

import inflection


@dataclass
class HasNameAttribute:
    name: str

    def get_name_snake(self):
        return inflection.underscore(self.name)


@dataclass
class ProtoServiceMethodDescription(HasNameAttribute):
    request: str
    response: str


@dataclass
class ProtoServiceDescription(HasNameAttribute):
    methods: typing.List[ProtoServiceMethodDescription] = field(default_factory=list)


@dataclass
class ProtoFileDescription(HasNameAttribute):
    services: typing.List[ProtoServiceDescription] = field(default_factory=list)

    def get_service(self) -> ProtoServiceDescription:
        return self.services[0]


class RpcProtoParser:
    def __init__(self, proto_path: str):
        self.proto_path = proto_path
        self.service_regex = re.compile(r'service\s+(\w+)\s+{')
        self.method_regex = re.compile(r'rpc\s+(\w+)\((\w+)\)\s+returns\s+\((\w+)\)')

    def run(self) -> typing.List[ProtoFileDescription]:
        result: typing.List[ProtoFileDescription] = []
        proto_path = Path(self.proto_path)
        if not proto_path.exists():
            raise Exception(f'Path {proto_path} is not exists')
        for proto_file in proto_path.glob('*.proto'):
            file_result = self.parse_file(proto_file)
            if file_result:
                result.append(file_result)
        return result

    def parse_file(self, proto_file: Path) -> typing.Optional[ProtoFileDescription]:
        with open(proto_file) as f:
            content = f.read()
            service_matches = re.findall(self.service_regex, content)
            if not service_matches:
                return
            method_matches = re.findall(self.method_regex, content)
            if not method_matches:
                return
            methods = []
            for match in method_matches:
                if len(match) != 3:
                    continue
                methods.append(ProtoServiceMethodDescription(name=match[0], request=match[1], response=match[2]))
            # Only one service per file
            service_name = service_matches[0].replace('Service', '')
            service_desc = ProtoServiceDescription(name=service_name, methods=methods)
            return ProtoFileDescription(name=proto_file.stem, services=[service_desc])
