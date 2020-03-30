import json


def get_name():
    with open("logs/logs.json", "r")as file:
        names = json.load(file)
        return names


def get_roles():
    with open("logs/roles.json", "r") as file:
        roles = json.load(file)
        return roles


def get_login(log_names, log_roles):
    while True:
        name = input("Enter your name: ")
        password = input("Enter password: ")
        if log_names.get(name) == password:
            access = log_roles.get(name)
            print(f"--------------------\nHello, {name}", "\n" + f"Your status - {access}\n--------------------")
            print("You can:")
            print("1. Read the article (Read)")
            if access == "ADMIN" or access == "EDITOR":
                print("2. Edit the article (Edit)")
            if access == "ADMIN":
                print("3. Add a user (Add user)")
            with open("logs/role_now.json", "w")as file:
                json.dump({"name": access}, file, indent=4)
            return access
        else:
            print("You have entered invalid data")


if __name__ == '__main__':
    main()
