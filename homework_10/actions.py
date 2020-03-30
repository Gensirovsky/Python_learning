import json


def audit_access(access):
    def wrapped(f):
        def wrapped():
            x = {
                "ADMIN": 0,
                "EDITOR": 1,
                "VISITOR": 2
            }
            with open("logs/role_now.json", "r")as file:
                access_now = json.load(file)
            if x[access] < x[access_now["name"]]:
                print("Access denied")
                exit()
            else:
                return f()
        return wrapped
    return wrapped


def to_do_something():
    doings = {
        "read": get_read,
        "edit": {
            "edit": get_edit_articles,
            "add": get_add_articles
        },
        "add user": get_add_user
    }
    while True:
        x = input("- ").lower()
        if x == "edit":
            print("ADD text or EDIT (add/edit)")
            while True:
                z = input("- ").lower()
                if z == "edit":
                    return doings[x][z]()
                if z == "add":
                    return doings[x][z]()
                else:
                    print("add/edit")
        if x != "read" and x != "add user":
            print("Choose from what is")
            continue
        else:
            return doings[x]()


def get_read():
    names = get_headers()
    print(f"You can view articles: {names} ")
    name_file = input("Enter name article: ")
    with open("media/articles.json", "r") as file:
        text = json.load(file)
        try:
            text = text[name_file]
        except KeyError:
            print("Choose from what is")
            exit()
        print(text)
    return


def get_headers():
    with open("media/articles.json", "r") as f:
        try:
            text = json.load(f)
            if text == {}:
                print("No articles - nothing to edit)")
                exit()
        except json.decoder.JSONDecodeError:
            print("No articles - nothing to edit)")
            exit()
    text = text.keys()
    names = ""
    for i in text:
        names += i + " || "
    return names

@audit_access("EDITOR")
def get_edit_articles():
    names = get_headers()
    print(f"You can edit articles: {names} ")
    name_file = input("Enter name article: ")
    with open("media/articles.json", "r") as file:
        text = json.load(file)
        text_acrticle = text[name_file]
        print(text_acrticle)
    new_text = input("Place for new text: ")
    new_header = input("enter a title for the text: ")
    with open("media/articles.json", "w") as file:
        print(name_file)
        del text[name_file]
        text.update({new_header: new_text})
        json.dump(text, file, indent=4)
        print("Mission complete. respect+")
    return

@audit_access("EDITOR")
def get_add_articles():
    with open("media/articles.json", "r") as file:
        text = json.load(file)
    new_text = input("Place for new text: ")
    while True:
        new_header = input("Enter a title for the text: ")
        if new_header in text:
            print("This title is occupied. Please select another one")
            continue
        else:
            break
    with open("media/articles.json", "w") as file:
        text.update({new_header: new_text})
        json.dump(text, file, indent=4)
        print("Mission complete. respect+")
    return


@audit_access("ADMIN")
def get_add_user():
    name = input("Enter username")
    pw = input("Enter password")
    role = input("Enter role (ADMIN/EDITOR/VISITOR)").upper()
    with open("logs/logs.json", "r")as file:
        file = json.load(file)
    with open("logs/logs.json", "w")as f:
        file.update({name: pw})
        json.dump(file, f, indent=4)
    with open("logs/roles.json", "r")as file:
        file = json.load(file)
    with open("logs/roles.json", "w")as f:
        file.update({name: role})
        json.dump(file, f, indent=4)
    print("Mission complete. respect+")
    return


if __name__ == '__main__':
    main()