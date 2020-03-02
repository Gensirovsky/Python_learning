"""3. Користувач вводить свою зарплату, і вводить свою посаду. Написати
програму, яка рахуватиме, скільки податків він заплатить в залежності від
своєї посади. (див. скрін)"""

salary = input("Введіть вашу заробідню плату:\n - ")
try:
    salary = float(salary)
except ValueError:
    salary = input("Заробітну плату потрібно ввести у вигляді цілого числа або дробу (Наприклад: 9463.63):\n - ")
    try:
        salary = float(salary)
    except ValueError:
        print("Циферкі знаходяться прямо над буквами, вони виглядають приблизно так: 1, 2, 3, 4... )")
        exit()
position = input("Введедіть свою посаду Програміст/Бухгалтер/Офіціант/Інша:\n - ")

salary = round(salary, 2)
tax = 0

if position == "Програміст" or position == "програміст":
    tax = salary * 0.13
else:
    if position == "Бухгалтер" or position == "бухгалтер":
        tax = salary * 0.1
    else:
        if position == "Офіціант" or position == "офіціант":
            tax = salary * 0.07
        else:
            if position == "Інша" or position == "інша":
                tax = salary * 0.05
            else:
                print("Ви обрали професію, якої не було в списку запропонованих")
                exit()

if position != "Інша" and position != "інша":
    print(f"Із {position}а, який отримує {salary} грн стягується податок у розмірі {round(tax, 2)} грн")
else:
    if position == "Інша" or position == "інша":
        print(f"При умові, що ви отримуєте {salary} грн, із вас стягуватиметься податок у розмірі {tax} грн")
    else:
        exit("Щось пішло не так(((")










