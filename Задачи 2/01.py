class Temperature:
    @staticmethod
    def c_to_f(c: float) -> float:
        print(round(c * 1.8 + 32, 2))

    @staticmethod
    def f_to_c(f: float) -> float:
        print(round((f - 32) / 1.8, 2))
