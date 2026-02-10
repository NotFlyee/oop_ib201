import numpy as np

class Table:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.table = np.zeros((cols, rows), dtype=np.int16).reshape(cols, rows)

    def get_value(self, row: int, col: int):
        return self.table[col, row] if 0 <= row < self.rows and 0 <= col < self.cols else None
    
    def set_value(self, row: int, col: int, value: int):
        self.table[col, row] = value

    def n_rows(self):
        return self.rows
    
    def n_cols(self):
        return self.cols
