def custom_write(file_name, strings):
    """
    :param file_name: название файла для записи
    :param strings: список строк для записи
    :return: словарь strings_positions
    """
    strings_positions = dict()
    index = 1
    tell = 0
    file = open(file_name, 'w', encoding='utf-8')
    for s in strings:
        tell = file.tell()
        file.write(s + "\n")
        strings_positions[(index, tell)] = s
        index += 1
    file.close()
    return strings_positions


if __name__ == "__main__":
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
