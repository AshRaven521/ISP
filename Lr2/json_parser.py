import json
from my_parser import Parser


class JsonParser(Parser):

    def dumps(self, obj):
        obj = super().dumps(obj)
        tempstr = self.dumps_wrapper(obj)
        tempstr = tempstr.replace("None","null")
        tempstr = tempstr.replace("\'", "\"")
        tempstr = tempstr.replace("\\", "\\\\")
        return tempstr
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
                        liststr = str(obj[key][i])
                        json_string += "\n" + liststr + ","
                if json_string.endswith(","):
                    json_string = json_string[: len(json_string) - 1] + "\n],\n"
                else:
                    json_string += "\n],\n"
            else:
                if isinstance(obj[key], str):
                    json_string += "\"" + key + "\"" + ": " + "\"" + obj[key] + "\"" + ", \n"
                else:
                    intstr = str(obj[key])
                    if intstr == "()":
                        intstr = "[]"
                    if obj[key] is None:
                        intstr = "[\nnull\n]"
                    if intstr == "(None,)":
                        intstr = "[\nnull\n]"
                    if intstr.startswith("("):
                        if intstr.endswith(")"):
                            intstr = "[" + intstr[1:]
                            intstr = intstr[:len(intstr) - 1] + "]"
                    json_string += "\"" + key + "\"" + ": " + intstr + ", \n"
        if json_string.endswith(", \n"):
            json_string = json_string[: len(json_string) - 3] + "\n}"
        else:
            json_string += "}"
        return json_string

    def loads(self, json_string):
        return super().loads(json.loads(json_string))
