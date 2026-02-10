class Selector:
    def __init__(self, values: list[int]):
        self.values = values

    def get_odds(self):
        return filter(lambda value: value % 2 != 0, self.values)

    def get_evens(self):
        return filter(lambda value: value % 2 == 0, self.values)
