import unittest

def is_even(number):
    return number % 2 == 0

class TestIsEvenFunction(unittest.TestCase):
    def is_even(self):
        self.assertTrue(is_even(2))

    def is_odd(self):
        self.assert_False(is_even(7))

if __name__ == "__main__":
    unittest.main()