class Balance:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, weight: int):
        self.right += weight

    def add_left(self, weight: int):
        self.left += weight

    def result(self):
        if self.right == self.left:
            return '='
        return 'L' if self.left > self.right else 'R'
