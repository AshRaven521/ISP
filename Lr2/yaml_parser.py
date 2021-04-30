import yaml
from my_parser import Parser


class YamlParser(Parser):

    def dumps(self, obj):
        return yaml.dump(super().dumps(obj))

    def loads(self, yaml_string):
        return super().loads(yaml.unsafe_load(yaml_string))
