import pickle_parser
import json_parser

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

if __name__ == "__main__":
    car = Car("BMW", "X6")

    #Little console UI(now just for json(dump, load))
    while True:
        print("1 - Сериализивать объект\n"
              "2 - Сериализовать функцию\n"
              "3 - Сериализовать класс\n"
              "4 - Десериализовать объект\n"
              "5 - Десериализовать функцию\n"
              "6 - Десериализовать класс\n"
              "7 - Выход")
        user_input = int(input())
        if user_input == 1:
            json_parser.JsonParser.dump(json_parser.JsonParser, "./test.json",
                                        json_parser.JsonParser.object_to_dictionary(json_parser.JsonParser, car))
        if user_input == 2:
            json_parser.JsonParser.dump(json_parser.JsonParser, "./test.json",
                                        json_parser.JsonParser.function_to_dictionary(json_parser.JsonParser, summary))
        if user_input == 3:
            json_parser.JsonParser.dump(json_parser.JsonParser, "./test.json",
                                        json_parser.JsonParser.class_to_dictionary(json_parser.JsonParser, Car))
        if user_input == 4:
            temp_obj = json_parser.JsonParser.load(json_parser.JsonParser, "./test.json")
            print(temp_obj)

        if user_input == 5:
            temp_func = json_parser.JsonParser.load(json_parser.JsonParser, "./test.json")
            print(temp_func)

        if user_input == 6:
            temp_class = json_parser.JsonParser.load(json_parser.JsonParser, "./test.json")
            print(temp_class)

        if user_input == 7:
            exit(0)

    #Pickle testing
    #pickle = pickle_parser.PickleParser.dump(pickle_parser.PickleParser,"./test.pickle", car)
    #car_from_pickle = pickle_parser.PickleParser.load(pickle_parser.PickleParser, "./test.pickle")

    #func = pickle_parser.PickleParser.dump(pickle_parser.PickleParser,"./test.pickle", summary(1, 2))
    #func_from_pickle = pickle_parser.PickleParser.load(pickle_parser.PickleParser,"./test.pickle")
    #print(func_from_pickle)
