class User:
    id_counter = 0
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    @classmethod
    def create(cls, name: str) -> "User":
        cls.id_counter += 1 
        return User(cls.id_counter, name)

    @classmethod
    def count(cls) -> int:
        return cls.id_counter
