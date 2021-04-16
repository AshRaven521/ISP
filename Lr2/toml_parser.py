from my_parser import MyParser
import toml
import inspect


class TomlParser(MyParser):

    def function_to_dictionary(self, func):
        struct = {'__type__': 'function'}
        args = []
        if str(func).__contains__('lambda'):
            lambda_string = str(inspect.getsource(func)[inspect.getsource(func).find("lambda"):])
            struct['code'] = lambda_string
            return struct
        elif func.__name__.startswith('__'):
            struct['name'] = func.__name__
            args = inspect.getfullargspec(func).args
            struct['args'] = args
        else:
            struct['name'] = func.__name__
            for arg in func.__code__.co_varnames:
                if arg == "class_name":
                    break
                args.append(arg)
            struct['args'] = args
            string = str(inspect.getsource(func))
            string = string[string.find("def"):]
            struct['code'] = string
        return struct

    def object_to_dictionary(self, obj):
        if "<class '__main__." in str(obj.__class__):
            struct = {'__type__': 'object', '__class__': obj.__class__.__name__}
            for attr in obj.__dir__():
                if not attr.startswith('__'):
                    attr_value = getattr(obj, attr)
                    if callable(attr_value):
                        if len(inspect.getfullargspec(attr_value).args) > 1:
                            struct[attr] = self.function_to_dictionary(TomlParser, attr_value)
                    elif "<class '__main__." in str(attr_value.__class__):
                        struct[attr] = self.object_to_dictionary(attr_value)
                    else:
                        struct[attr] = attr_value
            return struct
        raise Exception("Only object")

    def class_to_dictionary(self, cl):
        if cl.__class__.__name__ == "type":
            struct = {'__type__': 'class', '__class__': cl}
            for attr in dir(cl):
                if attr == "__init__":
                    attr_value = getattr(cl, attr)
                    struct[attr] = self.function_to_dictionary(self, attr_value)
                if not attr.startswith('__'):
                    attr_value = getattr(cl, attr)
                    if "<class 'type'>" in str(attr_value.__class__):
                        struct[attr] = self.class_to_dictionary(attr_value)
                    elif "<class '__main__." in str(attr_value.__class__):
                        struct[attr] = self.object_to_dictionary(attr_value)
                    elif callable(attr_value):
                        if len(inspect.getfullargspec(attr_value).args) > 1:
                            struct[attr] = self.function_to_dictionary(attr_value)
                    else:
                        struct[attr] = attr_value
        return struct

    def dump(self, save_file_path, obj):
        with open(save_file_path, "w") as file:
            toml.dump(obj, file)

    def dumps(self, obj):
        toml_obj = toml.dumps(obj)
        return toml_obj

    def load(self, load_file_path):
        dict_toml_obj = None
        with open(load_file_path, "r") as file:
            dict_toml_obj = toml.load(file)
        return dict_toml_obj

    def loads(self, s):
        dict_toml_str = toml.loads(s)
        return dict_toml_str
