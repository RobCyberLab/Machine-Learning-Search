
class MapReduce:
    def __init__(self):
        self.data = {}

    def run(self, collection):
        self.data = {}
        for key, values in collection:
            self.map(key, values)
        for key, values in self.data.items():
            self.reduce(key, values)

    def emit(self, key, value):
        if key in self.data:
            self.data[key].append(value)
        else:
            self.data[key] = [value]

    def map(self, _key, _values):
        raise Exception("map function not implemented")

    def reduce(self, _key, _values):
        raise Exception("reduce function not implemented")