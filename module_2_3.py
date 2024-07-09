my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# my_list = [1, 2, 4, 45, 5, 7]
index = 0
while my_list[index] >= 0:
    if my_list[index] == 0:
        index += 1
        continue
    else:
        print(my_list[index])
        index += 1

    if len(my_list) <= index:
        break
