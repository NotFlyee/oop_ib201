class FoodInfo:
    def __init__(self, proteins: int, fats: int, carbohydrates: int):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def get_proteins(self) -> int:
        return self.proteins
    
    def get_fats(self) -> int:
        return self.fats
    
    def get_carbohydrates(self) -> int:
        return self.carbohydrates
    
    def get_kcalories(self) -> int:
        return 4 * self.proteins + 9 * self.fats + 4 * self.carbohydrates
    
    def __add__(self, other):
        return FoodInfo(self.proteins + other.proteins, self.fats + other.fats, self.carbohydrates + other.carbohydrates)
