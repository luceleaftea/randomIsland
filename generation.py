# Loops through 2D array and returns the min and max values within it
def getMaxMinOf2DArray(array):
    maxNum = 0.0
    minNum = 0.0

    for y in array:
        for x in y:
            if x > maxNum:
                maxNum = x
            if x < minNum:
                minNum = x

    return [minNum, maxNum]

# maps a certain number from one range to another
def mapNumberToRange(num, startMin, startMax, endMin, endMax):
    return (num - startMin) / (startMax - startMin) * (endMax - endMin) + endMin

# Takes a 2D array and normalizes all values in it to the specified range
def normalize2DArray(array, endMin, endMax):
    maxAndMin = getMaxMinOf2DArray(array)
    startMin = maxAndMin[0]
    startMax = maxAndMin[1]
    newArray = []
    for y in array:
        newArray.append(list(map(lambda x: mapNumberToRange(x, startMin, startMax, endMin, endMax), y)))

    return newArray

# Raise the noise value by the specified power (returns real portion of complex numbers)
def stretchValue(num, power):
    num = pow(num, power)
    if type(num) == complex:
        num = num.real
    return num