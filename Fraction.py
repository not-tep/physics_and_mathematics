import math


class Fraction():
    def __init__( # Просто __init__
        self, 
        numerator: int = None, # Числитель 
        denominator: int = None # Знаменатель
    ) -> None:
        if not numerator:
            self.numerator = self.get_field('числитель')
        else:
            self.numerator = numerator
        
        if not denominator:
            self.denominator = self.get_field('знаменатель')
        else:
            self.denominator = denominator

        self.reduce()
    def __repr__(self) -> str: # Просто __repr__
        return f'Fraction: {self.numerator}/{self.denominator}'

    def get_field(self, str_) -> int: # Запросить у пользователя числитель/знаменатель
        while True:
            n = input(f'Введите {str_}:')
            try:
                n = int(n)
                return n
            except ValueError:
                print('Ошибка ввода! Повторите попытку.')
    def reduce(self) -> None: # Сократить
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    # Вывод данных
    def return_numerator(self) -> int:
        return self.numerator
    def return_denominator(self) -> int:
        return self.denominator
    def return_info(self) -> tuple[int, int]:
        return (self.numerator, self.denominator)

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
    def __add__(self, other) -> "Fraction": #     +  Сложение
        other = self.__find_common_denominator(other)

        return Fraction(
            numerator = self.numerator + other.numerator, 
            denominator = self.denominator
        )
    def __sub__(self, other) -> "Fraction": #     -  Вычитание
        other = self.__find_common_denominator(other)

        return Fraction(
            numerator = self.numerator - other.numerator, 
            denominator = self.denominator
        )
    def __mul__(self, other) -> "Fraction": #     *  Умножение
        return Fraction(
            numerator = self.numerator * other.numerator,
            denominator = self.denominator * other.denominator
        )
    def __truediv__(self, other) -> "Fraction":#  :  
        return self.__mul__(
            Fraction(
                numerator = other.denominator,
                denominator = other.numerator
            )
        )


if __name__ == '__main__':
    a1 = Fraction(5, 10)
    a2 = Fraction(20, 30)
    a3 = Fraction(5, 6)
    a4 = Fraction(9, 4)
    a5 = Fraction(3, 1)

    print((a1 + a2 - a3) * a4 / a5)