import pickle
from Parser import Parser

class PickleParser(Parser):

    def dump(self, save_file_path, obj):
        with open(save_file_path, 'wb') as file:
            pickle.dump(obj, file)

    def dumps(self, obj):
        pickle_string = pickle.dumps(obj)
        return pickle_string

    def load(self, load_file_path):
        with open(load_file_path, 'rb') as file:
            load_string = pickle.load(file)
        return load_string

    def loads(self, string):
        return pickle.loads(string)

            

