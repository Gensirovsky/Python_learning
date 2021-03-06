import string


def m_key(user_key, word):
    for i in user_key:
        if len(user_key) >= len(word):
            break
        user_key.append(i)
    return user_key


def code(word, key):
    alfabet = list(string.ascii_letters)
    arr_code = []
    for i in range(len(word)):
        try:
            new = (alfabet.index(key[i]) + alfabet.index(word[i]))
        except ValueError:
            arr_code.append(word[i])
            continue
        if new > 52:
            new %= 52
        arr_code.append(alfabet[new])
    return arr_code


def decoding(code, key):
    arr_decoding = []
    alfabet = list(string.ascii_letters)
    for i in range(len(code)):
        try:
            x = (alfabet.index(code[i]) - alfabet.index(key[i]))
        except ValueError:
            arr_decoding.append(code[i])
            continue
        arr_decoding.append(alfabet[x])
    return arr_decoding


def encrypter(word, user_key, dc = False):
    word = list(word)
    user_key = list(user_key)
    key = m_key(user_key, word)
    if dc == True:
        dc = decoding(word, user_key)
        return "".join(dc)
    cd = code(word, key)
    return "".join(cd)


if __name__ == '__main__':
    encrypter({'google': 'AOKkS'}, "python")