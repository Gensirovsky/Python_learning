# Division without rest
def get_full_shared(a, b):
    return a % b == 0


# Array filter: numbers
def get_only_numbers(*arr):
    result = []
    for i in arr:
        try:
            i = int(i)
        except ValueError:
            continue
        else:
            result.append(i)
    return result


# Perimetry polygon
def get_p_pon(*args):
    result = 0
    for i in args:
       result += i
    return result

# Perimetry delta
def get_p_delta(a, b, c):
    return a + b + c

# square area
def get_s_qre(a, b):
    return a * b

# square: hypotenuse and 2 side or height and side
import math
def get_s_delta(a = 0, b = 0, right = False):
    if right == True:
        return round(math.sqrt(a**2 + b ** 2), 2)
    h = b
    return (a * h) / 2

# square: 2 side and angle
def get_s2delta(a, b, d):
    return (a/2) * b * math.sin(d)


