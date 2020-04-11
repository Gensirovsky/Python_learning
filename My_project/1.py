"""
Написати програму, в яку можна буде записувати завдання та дату, до якої потрібно їх виконати.
Також додати змогу вписувати кількість досвіду(exp), який отримає користувач, а також можливість встановлювати дедйлайни.
Певна кількість досвіду(exp) повинна додавати рівень(lvl) до цілі(branch) користувача.
"""
from actions import Commands


def action(cds):
    do = {
        "add_b": cds.add_b,
        "review": cds.review,
        "add_t": cds.add_t,
        "del_b": cds.del_b,
        "del_t": cds.del_t,
        "mscp": cds.mscp
    }
    while True:
        command = input("- ")
        if command in do:
            return do[command]()
        else:
            print("Invalid command entered")
            continue


def main():
    print("Hello, user!")
    cds = Commands()
    action(cds)


if __name__ == '__main__':
    main()
