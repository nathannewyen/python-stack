# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
def biggie_size(array):
    newArray = []
    for number in array:
        if number > 0:
            number = "big"
        newArray.append(number)
    return newArray


print(biggie_size([-1, 3, 5, -5]))


# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values.
def count_positives(arr):
    count = 0
    for numbers in arr and range(0, len(arr)):
        if numbers > 0:
            count += 1
    if numbers == (len(arr) - 1):
        arr[numbers] = count
    return arr


print(count_positives([-1, 1, 1, 1]))


# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
def sum_total(myArr):
    sum = 0
    for i in myArr:
        sum = sum + i
    return sum


print(sum_total([1, 2, 3, 4]))


# Average - Create a function that takes a list and returns the average of all the values.
def average(newArr):
    sum = 0
    avg = 0
    for i in newArr:
        sum = sum + i
    avg = sum / len(newArr)
    return avg


print(average([1, 2, 3, 4]))


# Length - Create a function that takes a list and returns the length of the list.
def length(myNewArr):
    length_count = 0
    for i in range(len(myNewArr)):
        length_count = length_count + 1
    return length_count


print(length([37, 2, 1, -9]))


# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
def minimum(myArray):
    for i in myArray:
        min = myArray[0]
        if i < min:
            min = i
        elif len(myArray) < 0:
            return False
    return min


print(minimum([37, 2, 1, -9]))


# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
def maximum(myNewArr):
    for i in myNewArr:
        max = myNewArr[0]
        if max < i:
            max = i
        elif len(myNewArr) < 0:
            return False
    return max


print(maximum([37, 2, 1, -9]))


# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
def ultimate_analyst(myUltArr):
    max = myUltArr[0]
    min = myUltArr[0]
    sum = 0
    newUltArr = []
    count_length = 0
    for i in myUltArr:
        count_length = count_length + 1
        if max > i:
            max = i
        if min < i:
            min = i
        sum = sum + i
    avg = sum / len(myUltArr)
    newUltArr.append(
        f"sumTotal: {sum}, average: {avg}, minimum: {min}, maximum: {max}, length: {count_length}")
    return newUltArr


print(ultimate_analyst([37, 2, 1, -9]))


# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
def reverse(reverse_array):
    length = len(reverse_array)

    for i in range(0, length // 2):
        length = length - 1
        temp = reverse_array[i]
        reverse_array[i] = reverse_array[length]
        reverse_array[length] = temp
    return reverse_array


print(reverse([37, 2, 1, -9]))
