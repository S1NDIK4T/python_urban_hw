def int_unput():
    number = input("Введите число >>> ")
    if number.isdigit():
        return int(number)
    else:
        print("Это не число")
        int_unput()


print("Сравниваемые числа:")
first = int_unput()
second = int_unput()
third = int_unput()
if first == second and first == third:
    print(3)
elif first != second and first != third and second != third:
    print(0)
elif first == second or first == third or second == third:
    print(2)
