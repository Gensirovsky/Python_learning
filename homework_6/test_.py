import unittest
from homework_6.my_module import get_full_shared, get_s_delta, get_only_numbers
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
