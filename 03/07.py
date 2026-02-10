from itertools import zip_longest

class Polynomial:
    def __init__(self, coefficients: list[int]):
        self.coefficients = coefficients

    def __call__(self, x: int):
        return sum([self.coefficients[i] * x ** i for i in range(len(self.coefficients))])
    
    def __add__(self, other):
        return Polynomial(list(map(lambda cs: cs[0] + cs[1], zip_longest(self.coefficients, other.coefficients, fillvalue=0))))
