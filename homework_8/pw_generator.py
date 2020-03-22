import string
import random

def get_password(len_p):
    return (''.join(random.choice(string.ascii_letters) for i in range(len_p)))


def get_pw():
    len_p = None
    while len_p == None:
        try:
            len_p = int(input("What length should the password be?  "))
        except ValueError:
            print("You must enter a number")
            continue
    pw = get_password(len_p)
    print(pw)
    pww = None
    while pww == None:
        x = input("Does this password work for you? (+/-): ")
        if x == "+":
            print("OK!")
            break
        else:
            pw = get_password(len_p)
            print(pw)
    return pw


if __name__ == "__main__":
    get_pw()