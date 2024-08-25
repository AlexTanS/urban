def apply_all_func(int_list, *functions):
    """
    Вызывает каждую функцию к переданному списку int_list
    :param int_list: список из чисел (int, float)
    :param functions: неограниченное кол-во функций
    :return: dict (ключ: название вызванной функции, значение: результат работы со списком int_list)
    """
    results = dict()
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


if __name__ == "__main__":
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
