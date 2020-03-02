"""Користувач вводить 3 числа. Вивести на екран введені числа в порядку
зростання."""

a = input("Введіть перше число: ")
b = input("Введіть друге число: ")
c = input("Введіть третє число: ")

try:
    a = float(a)
    b = float(b)
    c = float(c)
except ValueError:
    if a == "" or b == "" or c == "":
        exit("Ви не ввели якусь із змінних")
    print(f"Потрібно ввести лише одне ЧИСЛО в кожну із змінних, також можна вказати дріб (наприклад: 1234.45)")
    exit()


if a <= b and a <= c:
    print(a, end=", ")
    if b <= c:
        print(b, c)
        exit()
    elif c <= b:
        print(c, b)
        exit()

if b <= a and b <= c:
    print(b, end=", ")
    if a <= c:
        print(a, end=", ")
        print(c)
    else:
        if c <= a:
            print(c, end=", ")
            print(a)
            exit()

if c <= b and c <= a:
    print(c, end=", ")
    if b <= a:
        print(b, a)
        exit()
    elif a <= b:
        print(a, b)
        exit()
