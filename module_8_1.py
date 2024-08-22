def add_everything_up(a, b):
    """
    Сложение разных типов даннных: a и b, которые могут быть как числами(int, float), так и строками(str).
    :param a: str/float/int
    :param b: str/float/int
    :return: sum, str
    """
    try:
        return round((a + b), 5)  # округление, иначе слишком много знаком после запятой иногда
    except TypeError:
        if isinstance(a, str):
            return a + str(b)
        else:
            return str(a) + b


if __name__ == "__main__":
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))
