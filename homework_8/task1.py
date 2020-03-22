import re
from collections import Counter

def get_read_file1(file1):
    text1 = open(file1, "r")
    file1 = text1.read()
    text1.close()
    return file1


def get_read_file2(file2):
    text2 = open(file2, "r")
    file2 = text2.read()
    text2.close()
    return file2


def get_search(text1, text2, words):
    pattern = words
    arr_search1 = re.findall(pattern, text1)
    arr_search2 = re.findall(pattern, text2)
    return arr_search1, arr_search2


def get_same_elements(arr1, arr2, words):
    sort_arr = []
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1
    for i in arr1:
        if i in arr2:
            sort_arr.append(i)
    result = []
    for i in range(len(sort_arr), 1):
        i = 1
    result = f"{words} : " + f"{len(sort_arr)}"
    return result


def main():
    a = False
    while a == False:
        try:
            file1, file2 = (input("What files to look for, lord? ")).split(", ")
            a = True
        except ValueError:
            a = False
            print("You must enter a file name after a comma with a space")
    words = input("Want to find? ")
    try:
        file_r1 = get_read_file1(file1)
        file_r2 = get_read_file2(file2)
    except FileNotFoundError:
        print("No files found")
        exit()
    arr1, arr2 = get_search(file_r1, file_r2, words)
    sort_arr = get_same_elements(arr1, arr2, words)
    print(sort_arr)



if __name__ == '__main__':
    main()
