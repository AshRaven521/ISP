import json
import re

from my_parser import Parser


class JsonParser(Parser):

    def dumps(self, obj):
        obj = super().dumps(obj)
        temp_str = self.dumps_wrapper(obj)
        temp_str = temp_str.replace("None","null")
        temp_str = temp_str.replace("\'", "\"")
        temp_str = temp_str.replace("\\", "\\\\")
        return temp_str
        #return json.dumps(super().dumps(obj), indent=4)

    def dumps_wrapper(self, obj):
        json_string = "{\n"
        for key in obj:
            if isinstance(obj[key], dict):
                temp_string = self.dumps_wrapper(obj[key])
                json_string += "\"" + key + "\"" + ": " + temp_string + ", \n"
                continue
            elif isinstance(obj[key], list):
                json_string += "\"" + key + "\"" + ": ["

                for i in range(len(obj[key])):
                    if isinstance(obj[key][i], str):
                        json_string += "\"" + obj[key][i] + "\","
                    else:
                        list_str = str(obj[key][i])
                        json_string += "\n" + list_str + ","
                if json_string.endswith(","):
                    json_string = json_string[: len(json_string) - 1] + "\n],\n"
                else:
                    json_string += "\n],\n"
            else:
                if isinstance(obj[key], str):
                    json_string += "\"" + key + "\"" + ": " + "\"" + obj[key] + "\"" + ", \n"
                else:
                    int_str = str(obj[key])
                    if int_str == "()":
                        int_str = "[]"
                    if obj[key] is None:
                        int_str = "[\nnull\n]"
                    if int_str == "(None,)":
                        int_str = "[\nnull\n]"
                    if int_str.startswith("("):
                        if int_str.endswith(")"):
                            int_str = "[" + int_str[1:]
                            int_str = int_str[:len(int_str) - 1] + "]"
                    json_string += "\"" + key + "\"" + ": " + int_str + ", \n"
        if json_string.endswith(", \n"):
            json_string = json_string[: len(json_string) - 3] + "\n}"
        else:
            json_string += "}"
        return json_string

    def loads(self, json_string):
        return super().loads(json.loads(json_string))

    #def loads(self, json_string):
    #    if 'code' in json_string:
    #        return super().loads(self.json_to_function(json_string));
    #    else:
    #        return None

    tuples = ['co_consts', 'co_names', 'co_varnames', 'co_freevars', 'co_cellvars']
    lists = ['nlocals', 'co_flags', 'co_code']

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
        func['globals'] = globals
        return func

    def string_to_tuple(self, string):
        return self.string_to_collection(string, tuple())

    def string_to_list(self, string):
        return self.string_to_collection(string, list())

    def string_to_collection(self, string, collection):
        string = string.replace('[', '').replace(']', '')
        arr = string.split(' ')

        for item in arr:
            if isinstance(item, str):
                if item.isdigit():
                    value = int(item)
                    collection.add(value)
                else:
                    value = item
                    collection.add(value)

        return collection
