import string
import random

def get_password(len_p):
    print(''.join(random.choice(string.ascii_letters) for i in range(len_p)))


def main():
    len_p = None
    while len_p == None:
        try:
            len_p = int(input("What length should the password be?  "))
        except ValueError:
            print("You must enter a number")
            continue
    get_password(len_p)
    pww = None
    while pww == None:
        x = input("Does this password work for you? (+/-): ")
        if x == "+":
            print("Bye!")
            break
        else:
            get_password(len_p)


if __name__ == "__main__":
    main()