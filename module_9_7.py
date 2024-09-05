def is_prime(func):
    """
    Функция-декоратор, которая распечатывает "Простое", если результат 'обёрнутой' функции будет простым числом и
    "Составное" в противном случае.
    :param func: function, 'обёрнутая' функция
    :return: function
    """

    def wrapper(*args):
        number = func(*args)

        d = 2
        while d * d <= number and number % d != 0:
            d += 1
        if d * d > number:
            print("Простое")
        else:
            print("Составное")
        return number

    return wrapper


@is_prime
def sum_three(a: int, b: int, c: int):
    """Сумма трёх чисел"""
    return a + b + c


if __name__ == "__main__":
    result = sum_three(2, 3, 6)
    print(result)
