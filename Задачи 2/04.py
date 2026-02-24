class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    @classmethod
    def from_string(cls, s: str) -> "Point":
        x, y = map(float, s.split(','))
        return Point(x, y)
    
    @classmethod
    def from_dict(cls, d: dict) -> "Point":
        x, y = d.values()
        return Point(float(x), float(y))
    
    @staticmethod
    def distance(a: "Point", b: "Point") -> float:
        return round(((a.x - b.x)**2 + (a.y - b.y)**2) ** 0.5, 2)
