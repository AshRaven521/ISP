import json
from my_parser import Parser


class JsonParser(Parser):

    def dumps(self, obj):
        return json.dumps(super().dumps(obj), indent=4)

    def loads(self, json_string):
        return super().loads(json.loads(json_string))
