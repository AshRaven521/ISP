import unittest
import factory
import json_parser
import pickle_parser
import toml_parser
import yaml_parser
from main import Car, summary


def multiple(num1, num2):
    return num1 * num2


class TestParsers(unittest.TestCase):
    def setUp(self):
        self.Car = Car
        self.summary = summary
        self.lamb = lambda a, b: a ** b
        self.car = car
        self.yaml_parser = factory.get_parser("Json")
        self.toml_parser = factory.get_parser("Pickle")
        self.json_parser = factory.get_parser("Toml")
        self.pickle_parser = factory.get_parser("Yaml")

        self.pickle_obj_str = pickle_parser.PickleParser.dumps(self, car)
        self.json_obj_str = json_parser.JsonParser.dumps(self, car)
        self.toml_obj_str = self.toml_parser.dumps(self, car)
        self.yaml_obj_str = yaml_parser.YamlParser.dumps(self, car)

        self.pickle_class_str = pickle_parser.PickleParser.dumps(self, Car)
        self.json_class_str = json_parser.JsonParser.dumps(self, Car)
        self.toml_class_str = self.toml_parser.dumps(self, Car)
        self.yaml_class_str = yaml_parser.YamlParser.dumps(self, Car)

        self.pickle_func_str = pickle_parser.PickleParser.dumps(self, self.summary)
        self.json_func_str = json_parser.JsonParser.dumps(self, self.lamb)
        self.toml_func_str = self.toml_parser.dumps(self, summary)
        self.yaml_func_str = yaml_parser.YamlParser.dumps(self, self.summary)

#Object testing block
    def test_json_obj_dumps(self):
        self.assertEqual(json_parser.JsonParser.dumps(self, car), self.json_obj_str)

    def test_pickle_obj_dumps(self):
        self.assertEqual(pickle_parser.PickleParser.dumps(self, car), self.pickle_obj_str)

    def test_toml_obj_dumps(self):
        self.assertEqual(self.toml_parser.dumps(self, car), self.toml_obj_str)

    def test_yaml_obj_dumps(self):
        self.assertEqual(yaml_parser.YamlParser.dumps(self, car), self.yaml_obj_str)


    def test_pickle_obj_loads(self):
        self.assertEqual(pickle_parser.PickleParser.loads(self, self.pickle_obj_str).brand, car.brand)

    def test_json_obj_loads(self):
        self.assertEqual(json_parser.JsonParser.loads(self, self.json_obj_str).brand, car.brand)

    def test_toml_obj_loads(self):
        self.assertEqual(self.toml_parser.loads(self, self.toml_obj_str).brand, car.brand)

    def test_yaml_obj_loads(self):
        self.assertEqual(yaml_parser.YamlParser.loads(self, self.yaml_obj_str).brand, car.brand)


#Class testing block
    def test_json_class_dumps(self):
        self.assertEqual(json_parser.JsonParser.dumps(self, Car), self.json_class_str)

    def test_pickle_class_dumps(self):
        self.assertEqual(pickle_parser.PickleParser.dumps(self, Car), self.pickle_class_str)

    def test_toml_class_dumps(self):
        self.assertEqual(self.toml_parser.dumps(self, Car), self.toml_class_str)

    def test_yaml_class_dumps(self):
        self.assertEqual(yaml_parser.YamlParser.dumps(self,Car), self.yaml_class_str)


    def test_pickle_class_loads(self):
        self.assertEqual(pickle_parser.PickleParser.loads(self, self.pickle_class_str).model, Car.model)

    def test_json_class_loads(self):
        self.assertEqual(json_parser.JsonParser.loads(self, self.json_class_str).brand, Car.brand)

    def test_toml_class_loads(self):
        self.assertEqual(self.toml_parser.loads(self, self.toml_class_str).brand, Car.brand)

    def test_yaml_class_loads(self):
        self.assertEqual(yaml_parser.YamlParser.loads(self, self.yaml_class_str).brand, Car.brand)


#Function(lambda) testing block
    def test_json_func_dumps(self):
        self.assertEqual(json_parser.JsonParser.dumps(self, self.lamb), self.json_func_str)

    def test_pickle_func_dumps(self):
        self.assertEqual(pickle_parser.PickleParser.dumps(self, self.summary), self.pickle_func_str)

    def test_toml_func_dumps(self):
        self.assertEqual(self.toml_parser.dumps(self, self.summary), self.toml_func_str)

    def test_yaml_func_dumps(self):
        self.assertEqual(yaml_parser.YamlParser.dumps(self, self.summary), self.yaml_func_str)


    def test_pickle_func_loads(self):
        self.assertEqual(pickle_parser.PickleParser.loads(self, self.pickle_func_str)(1, 2), 3)

    def test_json_func_loads(self):
        self.assertEqual(json_parser.JsonParser.loads(self, self.json_func_str)(4, 4), 256)

    def test_toml_func_loads(self):
        self.assertEqual(self.toml_parser.loads(self, self.toml_func_str)(3, 2), 5)

    def test_yaml_func_loads(self):
        self.assertEqual(yaml_parser.YamlParser.loads(self, self.yaml_func_str)(11, 2), 13)



if __name__ == "__main__":
    car = Car("Audi", "Q5")
    unittest.main()