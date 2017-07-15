def getMaxMinOfMapArray(mapArray):
    maxNum = 0.0
    minNum = 0.0

    for y in mapArray:
        for x in y:
            if x > maxNum:
                maxNum = x
            if x < minNum:
                minNum = x

    return [minNum, maxNum]

def mapNumberToRange(num, startMin, startMax, endMin, endMax):
    # print(num - startMin, startMax - num, endMax - endMin)
    return (num - startMin) / (startMax - startMin) * (endMax - endMin) + endMin

def normalizeMapArray(mapArray):
    maxAndMin = getMaxMinOfMapArray(mapArray)
    startMin = maxAndMin[0]
    startMax = maxAndMin[1]
    newMapArray = []
    for y in mapArray:
        newMapArray.append(list(map(lambda x: mapNumberToRange(x, startMin, startMax, -1.0, 1.0), y)))

    # for y in range(len(mapArray)):
    #     for x in range(len(mapArray[y])):
    #         print(mapArray[y][x], newMapArray[y][x])

    return newMapArray

def stretchValue(num, power):
    num = pow(num, power)
    if type(num) == complex:
        num = num.real
    return num