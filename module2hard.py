from random import Random

n = Random().randint(3, 20)  # случайное число от 3 до 20


def decryptor(n):
    result = ""
    pairs_numbers = []
    for i in range(1, n):
        for j in range(2, n):
            if (n % (i + j)) == 0:
                if (j, i) not in pairs_numbers and i != j:
                    pairs_numbers.append((i, j))
                    result += str(i) + str(j)
    return result


print("Первое число:", n)
print("Пары чисел (пароль):", decryptor(n))
