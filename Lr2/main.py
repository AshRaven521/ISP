import pickle_parser
import json_parser
import yaml_parser
import toml_parser
import factory

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    brand = "Volkswagen"
    model = "Touareg"


def summary(num1, num2):
    result = num1 + num2
    return result

def sub_format_menu():
    print("В какой формат сериализуем?\n"
          "1 - Json\n"
          "2 - Pickle\n"
          "3 - Toml\n"
          "4 - Yaml\n")

if __name__ == "__main__":
    car = Car("BMW", "X6")

    # Little console UI(ok, may be not so little as I think firstly)
    sub_format_menu()
    second_menu_input = int(input())
    obj_variant = factory.choose_format("Object", "Function", "Class")
    if obj_variant == "Object":
        if second_menu_input == 1:
            factory.Factory.parse(car, "Json", obj_variant)
        elif second_menu_input == 2:
            factory.Factory.parse(car, "Pickle", obj_variant)
        elif second_menu_input == 3:
            factory.Factory.parse(car, "Toml", obj_variant)
        elif second_menu_input == 4:
            factory.Factory.parse(car, "Yaml", obj_variant)
    elif obj_variant == "Function":
        if second_menu_input == 1:
            factory.Factory.parse(summary, "Json", obj_variant)
        elif second_menu_input == 2:
            factory.Factory.parse(lambda a: a+4, "Pickle", obj_variant)
        elif second_menu_input == 3:
            factory.Factory.parse(summary, "Toml", obj_variant)
        elif second_menu_input == 4:
            factory.Factory.parse(lambda a: a+5, "Yaml", obj_variant)
    elif obj_variant == "Class":
        if second_menu_input == 1:
            factory.Factory.parse(Car, "Json", obj_variant)
        elif second_menu_input == 2:
            factory.Factory.parse(Car, "Pickle", obj_variant)
        elif second_menu_input == 3:
            factory.Factory.parse(Car, "Toml", obj_variant)
        elif second_menu_input == 4:
            factory.Factory.parse(Car, "Yaml", obj_variant)

