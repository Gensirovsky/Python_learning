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

import unittest

class my_test(unittest.TestCase):
    def test_get_full_True(self):
        res = get_full_shared(10, 2)
        self.assertEqual(res, True)

    def test_get_full_False(self):
        res = get_full_shared(19, 2)
        self.assertEqual(res, False)

    def test_get_only_numbers(self):
        res = get_only_numbers(12, 34, "23", "34g", 76, 4, 73, "324f%")
        self.assertEqual(res, [12, 34, 23, 76, 4, 73])

    def test_get_s_delta(self):
        res = get_s_delta(2, 3)
        self.assertEqual(res, 3.0)

    def test_get_s_delta_h(self):
        res = get_s_delta(2, 3, True)
        self.assertEqual(res, 3.61)


if __name__ == "__main__":
    unittest.main()
