"""3. Вводиться два числа (a та b). В даному інтервалі потрібно вивести число,
яке має найбільше дільників. Тобто, якщо а=10, b=20,
то потрібно перевірити числа 11, 12, 13…. 20, і вивести на екран таке число,
яке має найбільше дільників, тобто частка при діленні рівна 0.
В наведеному прикладі вище потрібно вивести на екран число “18”,
оскільки воно має найбільше дільників (1, 2, 3, 6, 9, 18) і є максимальним."""
a = input("Введіть перше число: ")
b = input("Введіть друге число: ")
try:
    a = int(a)
    b = int(b)
except ValueError:
    print("Потрібно ввести ціле число")
    exit()
arr_numbers = []
if a < b and a < 0:
    a = 0                 #if any number < 0
elif b < a and b < 0:
    b = 0

if b == 0 and a == 0:
    print("У нуля немає дільників")
    exit()

if a > b:
    c = a - 1
    if b == 0:
        i = 1
    else:
        i = b
elif b > a:                #finding a smaller number
    c = b
    i = a + 1
else:
    print(a)
    exit()

while i <= c:
    for j in range(1, i+1):
        if i % j == 0:
            arr_numbers.append(i)  #add the number to the array as many times as its divisors
        if j == i:
            i += 1

if a > b:
    i = b + 1
    end = b
elif b > a:
    i = a + 1
    end = a
else:
    i = a
    end = b
max_number = 0

while i <= c:
    if max_number < arr_numbers.count(i):
        max_number = arr_numbers.count(i)       #finding the number of divisors
    i += 1

while i > end:
    if max_number == arr_numbers.count(i):
        max_number = i                          #find the number of the array with the largest number of divisors
        break
    i -= 1
print(max_number)



