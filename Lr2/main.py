from my_parser import Parser
from factory import Factory
import dis

def sum(num1, num2):
    return num1 + num2

sum_lambda = lambda lam1, lam2: lam1 + lam2

def testfunction():
    return "Hello, world!"


def gettype(type):
    parser = Parser()
    if type == 'Json':
        parser = Factory.factory("Json")
    elif type == 'Yaml':
        parser = Factory.factory("Yaml")
    elif type == 'Pickle':
        parser = Factory.factory("Pickle")
    elif type == 'Toml':
        parser = Factory.factory("Toml")
    return parser

def main():

    #car = Car()

    #Function in file
    gettype("Json").dump(sum, "./func.json")
    gettype("Pickle").dump(sum, "func.pickle")

    # Convert Json in Toml
    gettype("Toml").dump(gettype("Json").load("./func.json"), "./func.toml")

    #Lambda
    json_obj = gettype("Json").loads(gettype("Json").dumps(sum_lambda))
    print(json_obj(2, 3))

    #Function
    gettype("Json").dump(testfunction, "func4.json")
    f = gettype("Json").load("func4.json")
    print(f())

    #Function 2
    gettype("Json").dump(sum, "func3.json")
    h = gettype("Json").load('func3.json')
    print(h(6, 3))

    # Dictionary
    testdict = {'a': 1, 'b': 2}
    print(gettype("Json").loads(gettype("Json").dumps(testdict)))


    gettype("Json").dump(sum,"func.json")
    gettype("Json").load("func.json")

    #На всякий случай
    #dis.show_code(sum)

if __name__ == '__main__':
    main()
