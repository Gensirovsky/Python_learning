"""Створити свій міні-конвертер валют. При запуску програми попросити в
користувача такі дані: 1. Яку суму грошей він хоче конвертувати. 2. Яка
це валюта. 3. У яку валюту перевести дану суму. Дана програма повинна
підтримувати такі валюти, як долари, євро та гривні."""
sum = input('Яку суму грошей ви хочете конвертувати?\n - ')
try:
    sum = float(sum)
except ValueError:
    print("Хазяїн вчив мене конвертувати лише цифри (x_x)")
    exit()

cur = input(f'Це {sum} UAH/USD/EUR?\n - ')

converted_down = ''
converted = ''

if cur == "UAH" or cur == "USD" or cur == "EUR":
    converted = input("У яку валюту бажаєте перевести введену суму? UAH/USD/EUR\n - ")
else:
    if cur == "uah" or cur == "usd" or cur == "eur":
        print("Нє. Ну, нормально не міг написати. маленькими... ^-^")
        converted_down = input("У яку валюту бажаєте перевести введену суму? UAH/USD/EUR\n - ")
    else:
        print("Оберіть валюту із запропонованих")
        exit()

if converted != True:
    if converted_down == "uah":
        converted = "UAH"
    elif converted_down == "eur":
        converted = "EUR"
    elif converted_down == "usd":
        converted = "USD"

if cur == "uah" or cur == "eur" or cur == "usd":
    if cur == "uah":
        cur = "UAH"
    elif cur == "eur":
        cur = "EUR"
    elif cur == "usd":
        cur = "USD"

if cur == converted:
    result = sum
    print(f"як не дивно {sum} {cur} = {result} {converted} ")
    exit()
elif cur == converted_down:
    print(f"як не дивно {sum} {cur} = {result} {converted_down} ")
    exit()

if cur == "UAH" and converted == "USD":
    result = sum * 0.041
elif cur == "UAH" and converted == "EUR":
    result = sum * 0.037
elif cur == "USD" and converted == "UAH":
    result = sum * 24.4                         #conventer
elif cur == "USD" and converted == "EUR":
    result = sum * 0.91
elif cur == "EUR" and converted == "UAH":
    result = sum * 26.54
elif cur == "EUR" and converted == "USD":
    result = sum * 1.08

print(f"{sum} {cur} = {round(result, 3)} {converted} ")

