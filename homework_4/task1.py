"""Ввести номер картки, термін дії та CVV (Вводити недійсні дані). Написати
програму, яка перевірятиме, чи валідні ці дані, а саме: код повинен
містити 16 символів, термін дії має бути у форматі “dd/yy”. День та рік
спробувати перевести в int, якщо помилки не буде, то вивести на екран
“Expiration date: ОК”. Перевірити CVV: якщо це не число, або його
довжина не дорівнює 3 символам, вивести на екран повідомлення про
помилку. В разі успіху вивести на екран: “Ha-ha-ha.Now I will use your
credit card!”"""

card = input("Введіть номер своєї карти без пробілів, це ЦіЛкОм БеЗпЕчНо:\n - ")
days = ''
year = ''

if len(card) != 16:
    exit("Номер карти вказано невірно")
try:
    card = int(card)
except ValueError:
    exit("Номер карти вказаний невірно")

date = input("Введіть термін дії карти у форматі dd/yy:\n - ")

try:
    days, year = date.split("/")
    days = int(days)
    year = int(year)
except ValueError:
    exit("Дата вказана невірно")

else:
    if len(str(days)) >= 3 or len(str(year)) >= 3:
        exit("Дата вказана невірно")
    else:
        if 1 <= days <= 31 and 20 <= year:
            print("Expiration date: ОК")
        else:
            exit("У карти закінчився термін дії, або вказана дата не існує")

cvv = input("Введіть ваш CVV код:\n - ")

try:
    cvv = int(cvv)
except ValueError:
    exit("Повідомлення про помилку")

if len(str(cvv)) == 3:
    print("Ha-ha-ha.Now I will use your credit card!")
else:
    exit("Повідомлення про помилку")











