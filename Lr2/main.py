import pickle_parser
import json_parser
import yaml_parser
import toml_parser

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    brand = "Volkswagen"
    model = "Touareg"


def summary(num1, num2):
    result = num1 + num2
    return result


class Driver:
    def __init__(self, name, year_of_getting_driver_license, daily_mileage):
        self.name = name
        self.year_of_getting_driver_license = year_of_getting_driver_license
        self.daily_mileage = daily_mileage


def sub_serializing_menu():
    print("Во что сериализуем?\n"
          "1 - В файл\n"
          "2 - В строку\n")

def sub_deserializing_menu():
    print("Откуда десериализуем?\n"
          "1 - Из файла\n"
          "2 - Из строки\n")
def sub_format_menu():
    print("В какой формат сериализуем?\n"
          "1 - Json\n"
          "2 - Pickle\n"
          "3 - Toml\n"
          "4 - Yaml\n")


def json_menu():
    global json_object_string, json_function_string, json_class_string
    if main_input == 1:
        sub_serializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            json_parser.JsonParser.dump(json_parser.JsonParser, "./test.json",
                                        json_parser.JsonParser.object_to_dictionary(json_parser.JsonParser, car))
        if sub_input == 2:
            json_object_string = json_parser.JsonParser.dumps(json_parser.JsonParser,
                                                              json_parser.JsonParser.object_to_dictionary(
                                                                  json_parser.JsonParser, car))

    if main_input == 2:
        sub_serializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            json_parser.JsonParser.dump(json_parser.JsonParser, "./test.json",
                                        json_parser.JsonParser.function_to_dictionary(json_parser.JsonParser,
                                                                                      summary))
        if sub_input == 2:
            json_function_string = json_parser.JsonParser.dumps(json_parser.JsonParser,
                                                                json_parser.JsonParser.function_to_dictionary(
                                                                    json_parser.JsonParser, summary))

    if main_input == 3:
        sub_serializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            json_parser.JsonParser.dump(json_parser.JsonParser, "./test.json",
                                        json_parser.JsonParser.class_to_dictionary(json_parser.JsonParser, Car))
        if sub_input == 2:
            json_class_string = json_parser.JsonParser.dumps(json_parser.JsonParser,
                                                             json_parser.JsonParser.class_to_dictionary(
                                                                 json_parser.JsonParser, Car))
    if main_input == 4:
        sub_deserializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            temp_obj = json_parser.JsonParser.load(json_parser.JsonParser, "./test.json")
            print(temp_obj)
        if sub_input == 2:
            temp_obj_string = json_parser.JsonParser.loads(json_parser.JsonParser, json_object_string)
            #return temp_obj_string
            print(temp_obj_string)

    if main_input == 5:
        sub_deserializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            temp_func = json_parser.JsonParser.load(json_parser.JsonParser, "./test.json")
            print(temp_func)
        if sub_input == 2:
            temp_func_string = json_parser.JsonParser.loads(json_parser.JsonParser, json_function_string)
            print(temp_func_string)
            #return temp_func_string

    if main_input == 6:
        sub_deserializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            temp_class = json_parser.JsonParser.load(json_parser.JsonParser, "./test.json")
            print(temp_class)
        if sub_input == 2:
            temp_class_string = json_parser.JsonParser.loads(json_parser.JsonParser, json_class_string)
            print(temp_class_string)
            #return temp_class_string

    if main_input == 7:
        exit(0)

def pickle_menu():
    global pickle_object_string, pickle_function_string, pickle_class_string
    if main_input == 1:
        sub_serializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            pickle_parser.PickleParser.dump(pickle_parser.PickleParser, "./test.pickle", car)
        if sub_input == 2:
            pickle_object_string = pickle_parser.PickleParser.dumps(pickle_parser.PickleParser, car)

    if main_input == 2:
        sub_serializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            pickle_parser.PickleParser.dump(pickle_parser.PickleParser, "./test.pickle", summary)
        if sub_input == 2:
            pickle_function_string = pickle_parser.PickleParser.dumps(pickle_parser.PickleParser, summary)
    if main_input == 3:
        sub_serializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            pickle_parser.PickleParser.dump(pickle_parser.PickleParser, "./test.pickle", Car)
        if sub_input == 2:
            pickle_class_string = pickle_parser.PickleParser.dumps(pickle_parser.PickleParser, Car)
    if main_input == 4:
        sub_deserializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            temp_obj = pickle_parser.PickleParser.load(pickle_parser.PickleParser, "./test.pickle")
            print(temp_obj)
        if sub_input == 2:
            temp_obj_string = pickle_parser.PickleParser.loads(pickle_parser.PickleParser, pickle_object_string)
            print(temp_obj_string)

    if main_input == 5:
        sub_deserializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            temp_func = pickle_parser.PickleParser.load(pickle_parser.PickleParser, "./test.pickle")
            print(temp_func)
        if sub_input == 2:
            temp_func_string = pickle_parser.PickleParser.loads(pickle_parser.PickleParser, pickle_function_string)
            print(temp_func_string)

    if main_input == 6:
        sub_deserializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            temp_class = pickle_parser.PickleParser.load(pickle_parser.PickleParser, "./test.pickle")
            print(temp_class)
        if sub_input == 2:
            temp_class_string = pickle_parser.PickleParser.loads(pickle_parser.PickleParser, pickle_class_string)
            print(temp_class_string)

    if main_input == 7:
        exit(0)

def yaml_menu():
    global yaml_object_string, yaml_function_string, yaml_class_string
    if main_input == 1:
        sub_serializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            yaml_parser.YamlParser.dump(yaml_parser.YamlParser, car, "./test.yaml")
        if sub_input == 2:
            yaml_object_string = yaml_parser.YamlParser.dumps(yaml_parser.YamlParser, car)

    if main_input == 2:
        sub_serializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            yaml_parser.YamlParser.dump(yaml_parser.YamlParser, summary, "./test.yaml")
        if sub_input == 2:
            yaml_function_string = yaml_parser.YamlParser.dumps(yaml_parser.YamlParser, summary)
    if main_input == 3:
        sub_serializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            yaml_parser.YamlParser.dump(yaml_parser.YamlParser, Car, "./test.yaml")
        if sub_input == 2:
            yaml_class_string = yaml_parser.YamlParser.dumps(yaml_parser.YamlParser, Car)
    if main_input == 4:
        sub_deserializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            temp_obj = yaml_parser.YamlParser.load(yaml_parser.YamlParser, "./test.yaml")
            print(temp_obj)
        if sub_input == 2:
            temp_obj_string = yaml_parser.YamlParser.loads(yaml_parser.YamlParser, yaml_object_string)
            print(temp_obj_string)

    if main_input == 5:
        sub_deserializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            temp_func = yaml_parser.YamlParser.load(yaml_parser.YamlParser, "./test.yaml")
            print(temp_func)
        if sub_input == 2:
            temp_func_string = yaml_parser.YamlParser.loads(yaml_parser.YamlParser, yaml_function_string)
            print(temp_func_string)

    if main_input == 6:
        sub_deserializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            temp_class = yaml_parser.YamlParser.load(yaml_parser.YamlParser, "./test.yaml")
            print(temp_class)
        if sub_input == 2:
            temp_class_string = yaml_parser.YamlParser.loads(yaml_parser.YamlParser, yaml_class_string)
            print(temp_class_string)

    if main_input == 7:
        exit(0)

def toml_menu():
    global toml_object_string, toml_function_string, toml_class_string
    if main_input == 1:
        sub_serializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            toml_parser.TomlParser.dump(toml_parser.TomlParser, "./test.toml",
                                        toml_parser.TomlParser.object_to_dictionary(toml_parser.TomlParser, car))
        if sub_input == 2:
            toml_object_string = toml_parser.TomlParser.dumps(toml_parser.TomlParser,
                                                              toml_parser.TomlParser.object_to_dictionary(
                                                                  toml_parser.TomlParser, car))

    if main_input == 2:
        sub_serializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            toml_parser.TomlParser.dump(toml_parser.TomlParser, "./test.toml",
                                        toml_parser.TomlParser.function_to_dictionary(toml_parser.TomlParser, summary))
        if sub_input == 2:
            toml_function_string = toml_parser.TomlParser.dumps(toml_parser.TomlParser,
                                                              toml_parser.TomlParser.function_to_dictionary(
                                                                  toml_parser.TomlParser, summary))
    if main_input == 3:
        sub_serializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            toml_parser.TomlParser.dump(toml_parser.TomlParser, "./test.toml",
                                        toml_parser.TomlParser.class_to_dictionary(toml_parser.TomlParser, Car))
        if sub_input == 2:
            toml_class_string = toml_parser.TomlParser.dumps(toml_parser.TomlParser,
                                                              toml_parser.TomlParser.class_to_dictionary(
                                                                  toml_parser.TomlParser, Car))
    if main_input == 4:
        sub_deserializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            temp_obj = toml_parser.TomlParser.load(toml_parser.TomlParser, "./test.toml")
            print(temp_obj)
        if sub_input == 2:
            temp_obj_string = toml_parser.TomlParser.loads(toml_parser.TomlParser, toml_object_string)
            print(temp_obj_string)

    if main_input == 5:
        sub_deserializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            temp_func = toml_parser.TomlParser.load(toml_parser.TomlParser, "./test.toml")
            print(temp_func)
        if sub_input == 2:
            temp_func_string = toml_parser.TomlParser.loads(toml_parser.TomlParser, toml_function_string)
            print(temp_func_string)

    if main_input == 6:
        sub_deserializing_menu()
        sub_input = int(input())
        if sub_input == 1:
            temp_class = toml_parser.TomlParser.load(toml_parser.TomlParser, "./test.toml")
            print(temp_class)
        if sub_input == 2:
            temp_class_string = toml_parser.TomlParser.loads(toml_parser.TomlParser, toml_class_string)
            print(temp_class_string)

    if main_input == 7:
        exit(0)

if __name__ == "__main__":
    car = Car("BMW", "X6")

    # Little console UI(ok, may be not so little as I think firstly)
    sub_format_menu()
    second_menu_input = int(input())
    while True:
        print("1 - Сериализивать объект\n"
              "2 - Сериализовать функцию\n"
              "3 - Сериализовать класс\n"
              "4 - Десериализовать объект\n"
              "5 - Десериализовать функцию\n"
              "6 - Десериализовать класс\n"
              "7 - Выход")
        main_input = int(input())
        if second_menu_input == 1:
            json_menu()
        if second_menu_input == 2:
            pickle_menu()
        if second_menu_input == 3:
            toml_menu()
        if second_menu_input == 4:
            yaml_menu()

