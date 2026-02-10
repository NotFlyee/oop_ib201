import numpy as np

class Table:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.table = np.zeros((cols, rows), dtype=np.int16)

    def get_value(self, row: int, col: int):
        return self.table[col, row] if 0 <= row < self.rows and 0 <= col < self.cols else None
    
    def set_value(self, row: int, col: int, value: int):
        self.table[col, row] = value

    def n_rows(self):
        return self.rows
    
    def n_cols(self):
        return self.cols
    
    def delete_row(self, row: int):
        self.rows -= 1
        self.table = np.delete(self.table, row, axis=1)
    
    def delete_col(self, col: int):
        self.cols -= 1
        self.table = np.delete(self.table, col, axis=0)
    
    def add_row(self, row: int):
        self.rows += 1
        self.table = np.insert(self.table, row, np.zeros((1, self.cols), dtype=np.int16), axis=1)
    
    def add_col(self, col: int):
        self.cols += 1
        self.table = np.insert(self.table, col, np.zeros((1, self.rows), dtype=np.int16), axis=0)
