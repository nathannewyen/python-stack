arr = [0, 5, 8, 20, 300, 11, -66, 54, 7]


# def bubbleSorting(arr):
#     for j in range(len(arr)-1):
#         for i in range(len(arr)-1-j):
#             if arr[i] > arr[i + 1]:
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
#     return arr


# print(bubbleSorting(arr))


def bubbleSorting(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
            if min != i:
                arr[i], arr[min] = arr[min], arr[i]
    return arr


print(bubbleSorting(arr))
