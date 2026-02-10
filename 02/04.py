class MinStat:
    def __init__(self):
        self.values = list()

    def add_number(self, number: int) -> None:
        self.values.append(number)

    def result(self) -> int:
        return min(self.values) if self.values else None

class MaxStat:
    def __init__(self):
        self.values = list()

    def add_number(self, number: int) -> None:
        self.values.append(number)

    def result(self) -> int:
        return max(self.values) if self.values else None

class AverageStat:
    def __init__(self):
        self.values = list()

    def add_number(self, number: int) -> None:
        self.values.append(number)

    def result(self) -> float:
        return sum(self.values) / len(self.values) if self.values else None
