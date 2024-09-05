def all_variants(text):
    """
    Вывод всех подпоследовтельностей входящего текста
    :param text: str
    :return: str
    """
    # Упорядоченный вывод по количеству символов
    for i in range(len(text)):
        len_substring = i + 1  # длина подпоследовательности
        pointer = 0
        while len(text) - pointer > 0:
            if len(text[pointer: pointer + len_substring]) == len_substring:
                yield text[pointer: pointer + len_substring]
            else:
                break
            pointer += 1

    # НЕ Упорядоченный вывод по количеству символов
    # i = 0
    # while i <= len(text):
    #     j = 0
    #     while j < i:
    #         yield text[j:i]
    #         j += 1
    #     i += 1


if __name__ == "__main__":
    a = all_variants("abcd")
    for i in a:
        print(i)
