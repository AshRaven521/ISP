import json_parser
import pickle_parser
import toml_parser
import yaml_parser

class Factory:
    @staticmethod
    def parse(obj, format, obj_type):
        variant = parse_variant("dump", "dumps")
        parser = get_parser(format)
        if variant == "dump":
            file_path = get_file_path()
            if format == "Json" or format == "Toml":
                if obj_type == "Function":
                    parser.dump(parser, file_path, parser.function_to_dictionary(parser, obj))
                    temp_func = parser.load(parser, file_path)
                    print(temp_func)
                elif obj_type == "Object":
                    parser.dump(parser, file_path, parser.object_to_dictionary(parser, obj))
                    temp_object = parser.load(parser, file_path)
                    print(temp_object)
                elif obj_type == "Class":
                    parser.dump(parser, file_path, parser.class_to_dictionary(parser, obj))
                    temp_class = parser.load(parser, file_path)
                    print(temp_class)
            if format == "Pickle" or format == "Yaml":
                parser.dump(parser, file_path, obj)
                temp = parser.load(parser, file_path)
                print(temp)
        elif variant == "dumps":
            if format == "Json" or format == "Toml":
                if obj_type == "Function":
                    function_string = parser.dumps(parser, parser.function_to_dictionary(parser, obj))
                    temp_function_string = parser.loads(parser, function_string)
                    print(temp_function_string)
                elif obj_type == "Object":
                    object_string = parser.dumps(parser, parser.object_to_dictionary(parser, obj))
                    temp_obj_string = parser.loads(parser, object_string)
                    print(temp_obj_string)
                elif obj_type == "Class":
                    class_string = parser.dumps(parser, parser.class_to_dictionary(parser, obj))
                    temp_class_string = parser.loads(parser, class_string)
                    print(temp_class_string)
            if format == "Pickle" or format == "Yaml":
                string = parser.dumps(parser, obj)
                temp_string = parser.loads(parser, string)
                print(temp_string)

def get_parser(file_format):
        if file_format == 'Json':
            return json_parser.JsonParser
        elif file_format == 'Pickle':
            return pickle_parser.PickleParser
        elif file_format == 'Toml':
            return toml_parser.TomlParser
        elif file_format == 'Yaml':
            return yaml_parser.YamlParser
        else:
            raise ValueError(file_format)

def choose_format(first_param, second_param, third_param):
        print(f"1 - {first_param}\n"
              f"2 - {second_param}\n"
              f"3 - {third_param}\n"
              "4 - Выход")
        user_input = int(input())
        if user_input == 1:
            return first_param
        elif user_input == 2:
            return second_param
        elif user_input == 3:
            return third_param
        else:
            exit(0)


def parse_variant(first_param, second_param):
    print(f"1 - {first_param}\n"
          f"2 - {second_param}\n"
          "3 - Выход")
    user_input = int(input())
    if user_input == 1:
        return first_param
    elif user_input == 2:
        return second_param
    else:
        exit(0)

def get_file_path():
    print("Введите путь к файлу: ")
    user_input = str(input())
    return user_input