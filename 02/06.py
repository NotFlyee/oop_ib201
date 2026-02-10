class Rectangle:
    def __init__(self, x: int, y: int, w: int, h: int):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def intersection(self, rect):
        x_left = max(self.x, rect.x)
        x_right = min(self.x + self.w, rect.x + rect.w)
        y_bottom = max(self.y, rect.y)
        y_top = min(self.y + self.h, rect.y + rect.h)

        if x_right > x_left and y_top > y_bottom:
            return Rectangle(x_left, y_bottom, x_right - x_left, y_top - y_bottom)
        else:
            return None

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_w(self):
        return self.w

    def get_h(self):
        return self.h
