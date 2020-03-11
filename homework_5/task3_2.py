try:
    smaller_number = int(input("Enter smaller number: "))
    bigger_number = int(input("Enter bigger number: "))
except ValueError:
    print("Bye")
    exit()

if smaller_number > bigger_number:
    smaller_number, bigger_number = bigger_number, smaller_number

audit_0 = 0
audit_1 = 0
number = 0

for i in range(smaller_number, bigger_number):
    if i % 2 == 0:
        audit_0 += 1
    if audit_0 >= audit_1:
        audit_1 = audit_0
        audit_0 = 0
        number = i
print(number)