import math


class F():
    def __init__( # Просто __init__
        self, 
        a: int = 0, # Целая часть
        b: int = 0, # Числитель 
        c: int = 1  # Знаменатель
    ) -> None:
        self.numerator = b
        self.denominator = c

        self.reduce()
        self.replace_whole(a)
    def __repr__(self) -> str: # Просто __repr__
        info = self.get_whole()
        if info[0] == 0:
            return f'Fraction: {info[1]}/{info[2]}'
        if info[1] == 0:
            return f'Whole numder: {info[0]}'
        return f'Fraction: {info[0]} {info[1]}/{info[2]}'

    def reduce(self) -> None: # Сократить
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    # Целая часть
    def replace_whole(self, whole) -> None:
        self.numerator += whole * self.denominator
    def get_whole(self) -> tuple[int, int, int]:
        return (
            self.numerator // self.denominator,                  # Целая часть
            self.numerator - self.numerator // self.denominator * self.denominator, # Числитель
            self.denominator                                     # Знаменатель
        )

    # Вывод данных
    def return_numerator(self) -> int:
        return self.numerator
    def return_denominator(self) -> int:
        return self.denominator
    def return_info(self) -> tuple[int, int]:
        info = self.get_whole()
        return (info[0], {info[1]}, {info[2]})

    # Арифметические действия
    def __find_common_denominator(self, other): # Найти общий знаменатель
        gcd = math.gcd(self.denominator, other.denominator)
        my_additional_multiplier = other.denominator // gcd
        other_additional_multiplier = self.denominator // gcd

        self.numerator *= my_additional_multiplier
        self.denominator *= my_additional_multiplier

        other.numerator *= other_additional_multiplier
        other.denominator *= other_additional_multiplier
        
        return other
    def __add__(self, other) -> "F": #      +  Сложение
        other = self.__find_common_denominator(other)

        return F(
            b = self.numerator + other.numerator, 
            c = self.denominator
        )
    def __sub__(self, other) -> "F": #      -  Вычитание
        other = self.__find_common_denominator(other)

        return F(
            b = self.numerator - other.numerator, 
            c = self.denominator
        )
    def __mul__(self, other) -> "F": #      *  Умножение
        return F(
            b = self.numerator * other.numerator,
            c = self.denominator * other.denominator
        )
    def __truediv__(self, other) -> "F": #  :  Деление
        return self.__mul__(
            F(
                b = other.denominator,
                c = other.numerator
            )
        )


if __name__ == '__main__':
    print((F(30) / F(27) - F(0, 1, 3)) * F(2, 1, 7) + F(0, 2, 5))