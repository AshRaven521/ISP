from my_parser import Parser
from factory import Factory
import dis

def sum(num1, num2):
    return num1 + num2

sum_lambda = lambda lam1, lam2: lam1 + lam2

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
    #gettype("Toml").dump(gettype("Json").load("./func.json"), "./func.toml")

    gettype("Json").dump(sum, "./func.json")
    gettype("Toml").dump(gettype("Json").load("./func2.json"), "./func.toml")
    gettype("Pickle").dump(sum, "func.pickle")

    json_obj = gettype("Json").loads(gettype("Json").dumps(sum_lambda))
    print(json_obj(2, 3))

    gettype("Json").dump(sum_lambda, "./func3.json")
    #На всякий случай
    #dis.show_code(sum)

if __name__ == '__main__':
    main()
