# Print intergers from 0 to 150
for num in range(150):
    print(num)

# Multiples of Five
for num_multiply in range(5, 1000, 5):
    print(num_multiply)

# Counting, Dojo Way
for num_count in range(100):
    if num_count % 10 == 0:
        print("Coding")
    elif num_count % 5 == 0:
        print("Coding Dojo")
    else:
        print(num_count)

# Add odd integers from 0 to 500,000, and print the final sum.
add = 0
for sum in range(500000):
    add = add + sum
print(add)

# Print positive numbers starting at 2018, counting down by fours.
for numbers in range(2018, 0, -4):
    print(numbers)

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum = 2, highNum = 9, and mult = 3, the loop should print 3, 6, 9 (on successive lines)

lowNumb = 2
highNumb = 9
mult = 3
array = []
for i in range(highNumb + 1):
    if i > lowNumb and i <= highNumb:
        if i % 3 == 0:
            array.append(i)
print(array)
