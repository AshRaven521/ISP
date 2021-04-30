from my_parser import Parser
from factory import Factory

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
    gettype("Toml").dump(gettype("Json").load("./func.json"), "./func.toml")

if __name__ == '__main__':
    main()
