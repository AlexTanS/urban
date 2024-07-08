# Написать программу, которая составляет словарь, используя grades и students,
# где ключом будет имя ученика, а значением - его средний балл

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

dict_result = {}  # словарь для хранения результата
students_list = list(students)  # создаем список из имен
students_list.sort()  # сортируем список в алфавитном порядке

i = 0  #счетчик
dict_result.update({students_list[i] : (sum(grades[i]) / len(grades[i]))})
i += 1
dict_result.update({students_list[i] : (sum(grades[i]) / len(grades[i]))})
i += 1
dict_result.update({students_list[i] : (sum(grades[i]) / len(grades[i]))})
i += 1
dict_result.update({students_list[i] : (sum(grades[i]) / len(grades[i]))})
i += 1
dict_result.update({students_list[i] : (sum(grades[i]) / len(grades[i]))})
print(dict_result)

