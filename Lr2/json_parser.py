import json
from my_parser import Parser
import re


class JsonParser(Parser):

    def dumps(self, obj):
        obj = super().dumps(obj)
        return self.dumps_wrapper(obj)
        #return json.dumps(super().dumps(obj), indent=4)

    def dumps_wrapper(self, obj):
        json_string = "{\n"
        for key in obj:
            if isinstance(obj[key], dict):
                temp_string = self.dumps_wrapper(obj[key])
                if key is list(obj.keys())[-1]:
                    end = "\n"
                else:
                    end = ",\n"
                json_string += "\"" + key + "\"" + ": " + temp_string + end
                continue

            elif isinstance(obj[key], list) or isinstance(obj[key], tuple):
                json_string += "\"" + key + "\"" + ": ["
                for i in range(len(obj[key])):
                    if isinstance(obj[key][i], str):
                        json_string += "\"" + obj[key][i] + "\", "
                    elif isinstance(obj[key][i], int):
                        json_string += str(obj[key][i]) + ", "
                if json_string.endswith(", "):
                    json_string = json_string[: len(json_string) - 2] + "],\n"
                else:
                    json_string += "],\n"

            elif isinstance(obj[key], str):
                json_string += "\"" + key + "\"" + ": " + "\"" + obj[key].replace('\\', '\\\\') + "\"" + ",\n"
            elif isinstance(obj[key], int):
                json_string += "\"" + key + "\"" + ": " + str(obj[key]) + ",\n"

            elif isinstance(obj[key], type(None)):
                json_string += "\"" + key + "\"" + ": " + 'null' + ",\n"

            if key is list(obj.keys())[-1]:
                json_string = json_string[: len(json_string) - 2]
                json_string += '\n'

        if json_string.endswith(",\n"):
            json_string = json_string[:(len(json_string) - 2)] + "}"
        else:
            json_string += "}"
        return json_string


    #def loads(self, json_string):
    #    return super().loads(json.loads(json_string))


    def loads(self, json_string):
        if 'code' in json_string:
            return super().loads(self.json_to_function(json_string));
        else:
            return super().loads(self.json_to_object(json_string));

    tuples = ['co_consts', 'co_names', 'co_freevars', 'co_cellvars']
    lists = ['nlocals', 'co_code', 'co_lnotab', 'co_varnames']

    def json_to_function(self, json_string):
        json_string = json_string.replace("},\n\"globals\"", "}\n\"globals\"")
        string = re.sub('[{}\"]', '', json_string)
        arr = string.split('\n')
        code = dict()
        glob = dict()
        arr = [item for item in arr if not item == '']
        for item in arr:
            pair = item.split(': ')
            pair[1] = re.sub('[,]', '', pair[1])
            if pair[0] == 'code' or pair[0] == 'globals':
                continue
            if pair[0] in self.tuples:
                value = self.string_to_tuple(pair[1])
            elif pair[0] in self.lists:
                value = self.string_to_list(pair[1])
            else:
                if isinstance(pair[1], str):
                    if pair[1].isdigit():
                        value = int(pair[1])
                    else:
                        value = pair[1]

            if pair[0].startswith('co_'):
                code[pair[0]] = value
            else:
                glob[pair[0]] = value
        func = dict()
        func['code'] = code
        func['globals'] = glob
        return func

    def string_to_tuple(self, string):
        return self.string_to_collection(string, tuple())

    def string_to_list(self, string):
        return self.string_to_collection(string, list())

    def string_to_collection(self, string, collection):
        string = string.replace('[', '').replace(']', '')
        arr = string.split(' ')
        arrval = []
        for item in arr:
            if isinstance(item, str):
                if item.isdigit():
                    value = int(item)
                    arrval.append(value)
                else:
                    value = item
                    if value != '':
                        arrval.append(value)
        return arrval


    def json_to_object(self, json_string):
        string = re.sub('[{}\"]', '', json_string)
        arr = string.split('\n')
        glob = dict()
        arr = [item for item in arr if not item == '']
        for item in arr:
            pair = item.split(': ')
            pair[1] = re.sub('[,]', '', pair[1])
            if pair[0] == 'code' or pair[0] == 'globals':
                continue
            if isinstance(pair[1], str):
                if pair[1].isdigit():
                    value = int(pair[1])
                else:
                    value = pair[1]

            glob[pair[0]] = value

        return glob
