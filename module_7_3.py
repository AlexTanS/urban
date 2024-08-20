class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        """
        Подготовительный метод
        :return: dict
        """
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        all_words = dict()
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = ""
                for line in file:
                    for punkt in punctuation:
                        line = line.replace(punkt, " ")
                    words += " " + line
                words = words.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        """
        Нахождение индекса первого вхождения искомого слова
        :param word: str, искомое слово
        :return: dict, ключ-название файла, значение - позиция первого такого слова в списке слов этого файла
        """
        result = dict()
        for name, words in self.get_all_words().items():
            index = 1
            for w in words:
                if w.lower() == word.lower():
                    result[name] = index
                    break
                index += 1
        return result

    def count(self, word):
        """
        Подсчет количества вхождений искомого слова
        :param word: str, искомое слово
        :return: dict, ключ - название файла, значение - количество слова word в списке слов этого файла
        """
        result = dict()
        for name, words in self.get_all_words().items():
            index = 0
            for w in words:
                if w.lower() == word.lower():
                    index += 1
            result[name] = index
        return result
