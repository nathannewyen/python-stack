# import the python testing framework
import unittest
# our "unit"
# this is what we are running our test on


def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False
# our "unit tests"
# initialized by creating a class that inherits from unittest.TestCase


def reverseArray(list):
    for i in range(int(len(list)/2)):
        list[i], list[len(list)-i-1] = list[len(list) - i - 1], list[i]
    return list


class IsEvenTests(unittest.TestCase):
    # each method in this class is a test to be run

    def testOne(self):
        self.assertEqual(reverseArray([1, 2, 3]), [3, 2, 1])

    def testTwo(self):
        self.assertEqual(isEven(2), True)
        # another way to write above is
        self.assertTrue(isEven(2))

    def testThree(self):
        self.assertEqual(isEven(3), False)
        # another way to write above is
        self.assertFalse(isEven(3))
    # any task you want run before any method above is executed, put them in the setUp method

    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method

    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")


if __name__ == '__main__':
    unittest.main()  # this runs our tests


# str = "hello)))((("


# def balance(x):
#     count = 0
#     for i in x:
#         if i == "(":
#             count += 1
#         elif i == ")":
#             count -= 1
#         if count < 0:
#             return False
#     return count == 0


# print(balance(str))


# # String is Paladrome

my_str = "yay"


def isPaladrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True


print(isPaladrome(my_str))


# class Team:
#     def __init__(self, name):
#         self.name = name
#         self.participants = []

#     def add_member(self, participant):
#         self.participants.append(participant)
#         return self

#     def team_member(self):
#         displaystr = "Team members: "
#         for participant in self.participants:
#             displaystr += f"{participant.name},"
#         print(displaystr)


# class Participant:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def print_info(self):
#         print(
#             f"Product: {self.name}, Price: ${self.price}"
#         )


# messi = Participant("Messi", 20000)
# ronaldo = Participant("Ronaldo", 20000)


# team1 = Team("Juventus")
# team1.add_member(ronaldo).add_member(messi)


# messi.print_info()

# team1.team_member()


# # Braces Valid
# def bracesValid(string):
#     parens = 0

# string = "ab[] sad {[}]"

# brace = 0
# bracket = 0
# arr = []
# for i in range(len(string)):
#     if string[i] == “(“:
#         parens += 1
#         arr.append(string[i])
#     if string[i] == “)”:
#         parens -= 1
#     if arr[len(arr)-1] == “(“:
#         arr.pop()
#     if string[i] == “{“:
#         brace += 1
#         arr.append(string[i])
#     if string[i] == “}”:
#         brace -= 1
#     if arr[len(arr)-1] == “{“:
#         arr.pop()
#     if string[i] == “[“:
#         bracket += 1
#         arr.append(string[i])
#     if string[i] == “]”:
#         bracket -= 1
#     if arr[len(arr)-1] == “[“:
#         arr.pop()

#     if parens < 0 or brace < 0 or bracket < 0:
#         print("premature closing symbol")
#         return False
# if parens != 0 or brace != 0 or bracket != 0:
#     print("uneven amount of matching symbols")
#     return False
# elif len(arr) > 0:
#     print("symbols not in valid order")
#     return False
# else:
#     return True
# bracesValid(“W(a{t}s[o(n{c}o)m]e)h[e{r}e]!”)


# def lenofArray(someList):
#     count = 0
#     for i in range(0, len(someList)):
#         count += 1
#         print(count)


# print(lenofArray([37, 2, 1, -9, 11, 24, 16, 8, 3, 1, 100]))
