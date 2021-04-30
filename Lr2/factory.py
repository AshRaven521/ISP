from pickle_parser import PickleParser
from json_parser import JsonParser
from toml_parser import TomlParser
from yaml_parser import YamlParser



class Factory:

    @staticmethod
    def factory(factorytype):
        if factorytype == "Pickle":
            return PickleParser()
        elif factorytype == "Json":
            return JsonParser()
        elif factorytype == "Toml":
            return TomlParser()
        elif factorytype == "Yaml":
            return YamlParser()
        else:
            raise Exception('Incorrect parser')
