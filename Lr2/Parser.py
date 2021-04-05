from abc import ABC, abstractmethod

class Parser:

    @abstractmethod
    def dump(self, file_path, obj):
        pass
    @abstractmethod
    def dumps(self, obj):
        pass
    @abstractmethod
    def load(self, file_path):
        pass
    @abstractmethod
    def loads(self, string):
        pass