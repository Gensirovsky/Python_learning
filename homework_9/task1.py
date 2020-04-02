def main():
    value = str(int(input("Enter number: ")))
    if value > "3999" or value < "1":
        print("I can't handle numbers like this")
        exit()
    list_num = get_list_of_pawned_numbers(value)
    result = get_conversion_number(list_num)
    print(value, "-", result)


symbol = {
    "1": "I",
    "2": "II",
    "3": "III",
    "4": "IV",
    "5": "V",
    "6": "VI",
    "7": "VII",
    "8": "VII",
    "9": "IX",
    "10": "X",
    "20": "XX",
    "30": "XXX",
    "40": "XL",
    "50": "L",
    "60": "LX",
    "70": "LXX",
    "80": "LXXX",
    "90": "XC",
    "100": "C",
    "200": "CC",
    "300": "CCC",
    "400": "CD",
    "500": "D",
    "600": "DC",
    "700": "DCC",
    "800": "DCCC",
    "900": "CM",
    "1000": "M",
    "2000": "MM",
    "3000": "MMM"
}


def get_list_of_pawned_numbers(v):
    arr = list(v)
    result = []
    j = 10

    for i in range(len(arr)):
        result.append(int(v) % j - sum(result))
        j *= 10
    result.reverse()
    return result


def get_conversion_number(list_num):
    result = []
    for i in list_num:
        result.append(symbol.get(str(i)))
    result = "".join(result)
    return result


if __name__ == '__main__':
    main()


