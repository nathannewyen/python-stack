import unittest


def reverseList(list):
    for i in range(int(len(list)/2)):
        list[i], list[len(list)-i-1] = list[len(list) - i - 1], list[i]
    return list


def isPalindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True


def coins(cents):
    quarters = cents//25
    cents = cents - (quarters*25)
    dimes = (cents//10)
    cents = cents - (dimes*10)
    nickels = cents//5
    cents = cents - (nickels*5)
    pennies = cents
    return quarters, dimes, nickels, pennies


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


def fibonacci(n):
    a = 0
    b = 1

    for num in range(2, n):
        c = a + b
        a = b
        b = c
    return c


class introTDD(unittest.TestCase):
    def test_reverseList(self):
        self.assertEqual(reverseList([4, 5, 6]), [6, 5, 4])
        self.assertEqual(reverseList(
            [0, 95, 123, 10, 1]), [1, 10, 123, 95, 0])
        self.assertEqual(reverseList([1, 2, 3]), [3, 2, 1])

    def test_isPalindrome(self):
        self.assertEqual(isPalindrome("racecar"), True)
        self.assertEqual(isPalindrome("yay"), True)
        self.assertEqual(isPalindrome("anna"), True)
        self.assertEqual(isPalindrome("civic"), True)
        self.assertEqual(isPalindrome("kayak"), True)

    def test_coins(self):
        self.assertEqual(coins(87), (3, 1, 0, 2))
        self.assertEqual(coins(132), (5, 0, 1, 2))
        self.assertEqual(coins(231), (9, 0, 1, 1))
        self.assertEqual(coins(111), (4, 1, 0, 1))
        self.assertEqual(coins(190), (7, 1, 1, 0))

    def test_factorial(self):
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(5), 120)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), 3)
        self.assertEqual(fibonacci(9), 21)
        self.assertEqual(fibonacci(10), 34)


if __name__ == '__main__':
    unittest.main()
