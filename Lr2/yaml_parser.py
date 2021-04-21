from my_parser import MyParser
import yaml

class YamlParser(MyParser):

    def dump(self, save_file_path,obj):
        with open(save_file_path, "w") as file:
            yaml.dump(obj, file)

    def dumps(self, obj):
        yaml_string = yaml.dump(obj)
        return yaml_string

    def load(self, load_file_path):
        obj = None
        with open(load_file_path, "r") as file:
            obj = yaml.unsafe_load(file)
        return obj

    def loads(self, s):
        obj = yaml.unsafe_load(s)
        return obj