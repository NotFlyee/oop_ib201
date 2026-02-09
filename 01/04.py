class OddEvenSeparator:
    def __init__(self):
        self.numbers = list()

    def add_number(self, number: int):
        self.numbers.append(number)

    def even(self):
        return filter(lambda number: number % 2 == 0, self.numbers)
    
    def odd(self):
        return filter(lambda number: number % 2 != 0, self.numbers)
