n = input("Введіть число: ")
try:
    n = int(n)
except ValueError:
    print("Потрібно ввести ціле число")
    exit()
audit = True
if n == 0:
    print(0)
    exit()
elif n == 1 or n == -1:
    print(1, )
    exit()
else:
    minus = False
    i = 1
    numbers = [1, ]
    minus_numbers = []
    end = 1
    if n < 0:
        n = -n
        minus = True
    while audit:
        numbers.append(i)
        i += numbers[-2]
        end += 1
        if end == n:
            audit = False

    if minus:
        for j in range(len(numbers)):
            if j % 2 == 0:
                minus_numbers.append(numbers[j])
            else:
                minus_numbers.append(-numbers[j])
        print(*minus_numbers, sep=", ")
    else:
        print(*numbers, sep=", ")

