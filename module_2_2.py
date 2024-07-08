first = int(input("Ввести 1 число: "))
second = int(input("Ввести 2 число: "))
third = int(input("Ввести 3 число: "))

if first == second and second == third and first == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)
