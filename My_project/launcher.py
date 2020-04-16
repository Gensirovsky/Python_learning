"""
Написати програму, в яку можна буде записувати завдання та дату, до якої потрібно їх виконати.
Також додати змогу вписувати кількість досвіду(exp), який отримає користувач, а також можливість встановлювати дедйлайни.
Певна кількість досвіду(exp) повинна додавати рівень(lvl) до цілі(branch) користувача.
"""
from actions import Commands


def action():
    cds = Commands()

    def commands_help():
        print("  Review your achievements - [review]")
        print("  View existing branches - [v_branches]")
        print("  Add a branch - [add_b]")
        print("  Add a target to a branch - [add_t]")
        print("  Delete a target - [del_t]")
        print("  Delete a branch - [del_b]")
        print("  Completed the target? - [mscp]")
        print("  Exit the program - [/exit]")
        action()

    do = {
        "v_branches": cds.v_branches,
        "add_b": cds.add_b,
        "review": cds.review,
        "add_t": cds.add_t,
        "del_b": cds.del_b,
        "del_t": cds.del_t,
        "mscp": cds.mscp
    }
    while True:
        print("-------------------------------------")
        command = input("Waiting for the order: ")
        print("-------------------------------------")
        if command == "/help":
            return commands_help()
        elif command == "/exit":
            print("Goodbye!")
            exit()
        elif command in do:
            do[command]()
            action()
        else:
            print("Invalid command entered")
            continue


def main():
    print("Hello, user!")
    print('Type "/help" to open the command list')
    action()


if __name__ == '__main__':
    main()
