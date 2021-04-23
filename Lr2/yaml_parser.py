from my_parser import MyParser
import yaml
import inspect

class YamlParser(MyParser):

    def function_to_dictionary(self, func):
        struct = {'__type__': 'function'}
        args = []
        if str(func).__contains__('lambda'):
            s = str(inspect.getsource(func)[inspect.getsource(func).find("lambda"):])
            struct['code'] = s
            return struct
        elif func.__name__.startswith('__'):
            struct['name'] = func.__name__
            args = inspect.getfullargspec(func).args
            struct['args'] = args
            return struct
        else:
            globs = {}
            name = func.__name__
            func_code = inspect.getsource(func)
            if func_code.__contains__('global'):
                subs = func_code.split('global')
                for i in range(1, len(subs)):
                    glob_key = subs[i].lstrip().split("\n")[0]
                    globs.update(dict([(glob_key, func.__globals__[glob_key])]))

            struct['name'] = name
            struct['globals'] = globs
            struct['code'] = func_code
            return struct

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