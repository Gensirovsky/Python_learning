try:
    number = int(input("Enter number: "))
except ValueError:
    print()
    exit()

r1 = 0
r2 = 1
for i in range(-1, number):
    print(r1, end=" ")
    r3 = r1 + r2
    r1 = r2
    r2 = r3
