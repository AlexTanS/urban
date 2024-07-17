def print_params(a=1, b='строка', c=True):
    '''Функция, которая принимает три параметра со значениями по умолчанию'''
    print(a, b, c)


print('Вызвать функцию print_params с разным количеством аргументов, включая вызов без аргументов:')
print_params()
print_params('ABBA', True, (12, 7))
print_params(b=25)
print_params(c=[1, 2, 3])
print()

values_list = ["ABBA", 25, (12, 7)]  # список с тремя элементами разных типов
values_dict = {'a': False, 'b': (44, 77), 'c': 25}  # словарь с тремя ключами и значениями разных типов

print_params(*values_list)  # передача параметров в функцию print_params, используя распаковку параметров
print_params(**values_dict)  # передача параметров в функцию print_params, используя распаковку параметров

values_list_2 = [54.32, 'Строка']  # список с двумя элементами разных типов
print_params(*values_list_2, 42)  # проверка работы print_params(*values_list_2, 42)
