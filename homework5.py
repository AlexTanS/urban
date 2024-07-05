immutable_var = ("ABBA", 35, True, [0, "1", 2])     # создать переменную и присвоить ей кортеж из нескольких элементов
                                                    # разных типов данных
print(immutable_var)       # выполнить операции вывода кортежа immutable_var на экран

# immutable_var[0] = "BAAB"  # попытайтесь изменить элементы кортежа immutable_var
                             # объясните, почему нельзя изменить значения элементов кортежа
# Эта операция выдаёт ошибку - TypeError: 'tuple' object does not support item assignment,
# так как тип 'tuple' не поддерживает назначение элементов, то есть он не изменяемый тип данных, хотя может содержать
# изменяемые типа данных
# В документации (https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences) прямо так и сказано:
# "It is not possible to assign to the individual items of a tuple, however it is possible to create tuples which
# contain mutable objects, such as lists." -> "Невозможно присвоить значение отдельным элементам кортежа, однако можно
# создавать кортежи, содержащие изменяемые объекты, такие как списки."

mutable_var = ["ABBA", 35, False, ("0", 1, 2)]  # создать переменную и присвоить ей список из нескольких элементов
mutable_var[0] = "URBAN"                    # изменить элементы списка
mutable_var[1] =True                        # изменить элементы списка
mutable_var[2] = 40                         # изменить элементы списка
mutable_var[3] = "Здесь был кортеж"         # изменить элементы списка
print("Измененный список:", mutable_var)    # вывести на экран измененный список
