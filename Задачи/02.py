class Counter:
    def __init__(self, start: int = 0) -> None:
        self._value = start

    def value(self) -> int:
        return self._value

    def inc(self) -> None:
        self._value += 1

    def dec(self) -> None:
        self._value -= 1


class LimitedCounter(Counter):
    def __init__(self, min_value: int, max_value: int, start: int = 0) -> None:
        super().__init__(start)
        self.min_value = min_value
        self.max_value = max_value

    def inc(self) -> None:
        self._value += 1 if self._value < self.max_value else 0

    def dec(self) -> None:
        self._value -= 1 if self._value > self.min_value else 0
