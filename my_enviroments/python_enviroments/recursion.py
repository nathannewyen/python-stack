def rSigma(input):
    if input <= 0:
        return 0
    elif input == 1:
        return 1
    else:
        return input + rSigma(input - 1)


print(rSigma(10))


def rFactor(input):
    if input <= 1:
        return 1
    else:
        return input * rFactor(input - 1)


print(rFactor(10))


def rFibbonachi(input):
    if input == 0:
        return 1
    elif input == 1:
        return 1
    else:
        return input + rFibbonachi(input - 2)


print(rFibbonachi(10))


# Facebook ask interview
def ios(string, sub="", i=0):
    if len(string) == i:
        return [sub]
    else:
        return ios(string, sub + string[i], i+1) + ios(string, sub, i+1)


print(ios("abc"))


# FLOOD FILL SOLUTION:
def floodFill(canvas2D, startXY, newColor, originalColor=None):

    x = startXY[0]
    y = startXY[1]

    # so, canvas2D[y][x] is the current pixel I'm looking at

    if (originalColor == None):
        originalColor = canvas2D[y][x]

    if (canvas2D[y][x] != originalColor):
        print("Not original color")
        return "Not original color"

    changed = False

    if (canvas2D[y][x] == originalColor):
        canvas2D[y][x] = newColor
        changed = True

    if (changed):
        if (y - 1 >= 0):
            print("recursing y-1")
            floodFill(canvas2D, [x, y - 1], newColor, originalColor)

        if (y + 1 < len(canvas2D)):
            print("recursing y+1")
            floodFill(canvas2D, [x, y + 1], newColor, originalColor)

        if (x - 1 >= 0):
            print("recursing x-1")
            floodFill(canvas2D, [x - 1, y], newColor, originalColor)

        if (x + 1 < len(canvas2D[0])):
            print("recursing x+1")
            floodFill(canvas2D, [x + 1, y], newColor, originalColor)

    print("New canvas:")
    print(canvas2D)
    print("")
    return canvas2D


floodFill([
    [3, 2, 3, 4, 3],
    [2, 3, 3, 4, 0],
    [7, 3, 3, 5, 3],
    [6, 5, 3, 4, 1],
    [1, 2, 3, 3, 3]
], [2, 2], 1)
