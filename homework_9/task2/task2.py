from pw_generator import get_pw
from encrypter import encrypter
import json


def get_w_file(keyword, pw):
    try:
        data = json.load(open("word-key.json"))
    except:
        data = {keyword: pw}
    data.update({keyword: pw})
    with open("word-key.json", "w") as f:
        json.dump(data, f, indent=4)
    return


def get_search_password(keyword):
    with open("word-key.json", "r") as file:
        data = json.load(file)
        password = data.get(keyword)
    return password


def main():
    get_audit_password()
    x = ""
    a = True
    while a:
        x = input("CREATE new or GET old: ")
        if x.lower() == "create" or x.lower() == "get":
            a = False
        else:
            print("Create/get")
    if x.lower() == "create":
        get_new_password()
    else:
        try:
            x_get()
        except ValueError:
            print("You haven't added anything to the file")


def get_new_password():
    pw = get_pw()
    keyword = input("Enter the keyword: ")
    get_w_file(keyword, pw)
    y = input("Please create a password: ")
    get_defense(y)


def x_get():
    keyword = input("Enter the keyword: ")
    search_pw = get_search_password(keyword)
    print(search_pw)
    y = input("Please create a password: ")
    get_defense(y)
    return


def get_defense(y):
    with open("pw_prog.txt", "w") as file:
        y = encrypter(y, "python")
        file.write(y)


def get_audit_password():
    with open("pw_prog.txt", "r") as file:
        dc_pw = file.read()
        file.close()
        if dc_pw == "":
            return
        print(dc_pw)
        pw = encrypter(dc_pw, "python", dc = True)
        print(pw)
        audit = False
        while audit == False:
            audit = True
            users_pw = input("Enter your password ")
            if pw != users_pw:
                audit = False


if __name__ == '__main__':
    main()