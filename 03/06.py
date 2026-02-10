class SparseArray:
    def __init__(self):
        self.data = dict()

    def __setitem__(self, key: int, value: int):
        self.data[key] = value

    def __getitem__(self, key: int):
        return self.data.get(key, 0)
