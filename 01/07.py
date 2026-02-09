class BoundingRectangle:
    def __init__(self):
        self.points = list()

    def add_point(self, x: int, y: int):
        self.points.append((x, y))

    def width(self):
        return max(self.points)[0] - min(self.points)[0]

    def height(self):
        return max(self.points, key=lambda point: point[1])[1] - min(self.points, key=lambda point: point[1])[1]

    def bottom_y(self):
        return min(self.points, key=lambda point: point[1])[1]

    def top_y(self):
        return max(self.points, key=lambda point: point[1])[1]

    def left_x(self):
        return min(self.points)[0]

    def right_x(self):
        return max(self.points)[0]
