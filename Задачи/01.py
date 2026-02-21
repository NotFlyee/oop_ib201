class User:
    def __init__(self, username: str, password: str) -> None:
        self.__username = username
        self.__password = password

    @property    
    def username(self) -> str:
        return self.__username
    
    def check_password(self, password: str) -> bool:
        return password == self.__password

    def set_password(self, old_password: str, new_password: str) -> bool:
        password_is_correct = old_password == self.__password
        if password_is_correct:
            self.__password = new_password
        return password_is_correct
