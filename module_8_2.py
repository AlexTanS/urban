def personal_sum(numbers):
    """
    Подсчёт суммы чисел в коллекции.
    :param numbers: коллекция, массив
    :return: tuple(result - сумма чисел, incorrect_data - кол-во некорректных данных)
    """
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    return result, incorrect_data


def calculate_average(numbers):
    """
    Среднее арифметическое - сумма всех данных делённая на их количество.
    :param numbers: коллекция, массив
    :return: int
    """
    try:
        sum_, incorrect = personal_sum(numbers)
        return sum_ / (len(numbers) - incorrect)
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


if __name__ == "__main__":
    print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
    print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
