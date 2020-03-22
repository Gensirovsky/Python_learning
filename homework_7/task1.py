"""Написати три функції. Задача першої функції:
отримання всіх чисел з рядка за допомогою регулярного виразу.
Задача другої функції: пошук в тексті дати у форматі “дд-мм-рррр”
за допомогою регулярного виразу. Задача третьої функції:
Перевірка, чи в тексті присутні слова “Red”, “Green”, “Blue”, “Yellow”"""
import re


def get_only_numbers(text):
    textlookfor = r"\d+"
    result = ", ".join(re.findall(textlookfor, text))
    return result


def get_date(x):
    textlookfor = r"\d\d\-\d\d\-\d{2}"
    result = ", ".join(re.findall(textlookfor, x))
    return result


def get_color_true(x):
    colors = ["red", "green", "blue", "yellow"]
    search = set(", ".join(re.findall(r"\b[Bb]lue\b|\b[Rr]ed\b|\b[Yy]ellow\b|\b[Gg]reen\b", x)).lower().split(", "))
    result = ""
    for i in colors:
        if i in search:
            result += f"{i.title()} is True\n"
    return result


def main():
    file = open("homework.txt", "r+")
    text = file.read()
    print("Date in text:", get_date(text))
    print("Numbers in text::", get_only_numbers(text))
    print(get_color_true(text))


if __name__ == '__main__':
    main()
