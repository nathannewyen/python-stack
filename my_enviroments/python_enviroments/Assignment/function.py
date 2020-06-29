# Countdown
array = []


def countdown(a):
    for number in range(a, -1, -1):
        array.append(number)
    return array


print(countdown(5))


# Print and Return

array_two = [1, 2]


def print_and_return(array_two):
    x, y = array_two
    print(x)
    return y


print(print_and_return(array_two))

# First Plus Length
array_third = [1, 2, 3, 4, 5]


def first_plus_length():
    for num in range(len(array_third)):
        return num + len(array_third) + array_third[0]


print(first_plus_length())

# Values Greater than Second


array_fourth = [5, 2, 3, 2, 1, 4]


def values_greater_than_second():
    k = []
    for i in range(len(array_fourth)):
        if array_fourth[i] > array_fourth[1] and len(array_fourth) > 1:
            k.append(array_fourth[i])
            print(k)
    else:
        return False


values_greater_than_second()


# This Length, That Value

def length_and_value(a, b):
    j = []
    for i in range(a):
        i = 1 * b
        j.append(i)
    print(j)


length_and_value(6, 2)
