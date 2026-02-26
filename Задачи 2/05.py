class Shape:
    d = dict()

    def __init_subclass__(cls) -> None:
        cls.d[cls.__name__] = cls

    @classmethod
    def available(cls) -> list[str]:
        return sorted(cls.d)
    
class Circle(Shape):
    pass

class Square(Shape):
    pass

class Triangle(Shape):
    pass
