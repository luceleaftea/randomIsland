import random, noise
import generation

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

def generateElevationMoisture(sizeX, sizeY):
    elevation = []
    moisture = []
    # Generate elevation using noise
    nz = random.random()

    octaves = 4
    freq = 1.0
    redistribPower = .3

    for y in range(sizeY):
        row = []
        for x in range(sizeX):
            nx = x / sizeX - (sizeX / 2.0)
            ny = y / sizeY - (sizeY / 2.0)
            randNoise = noise.snoise3(1 * nx, 1 * ny, 1 * nz, 1)
            randNoise += .5 * noise.snoise3(2 * nx, 2 * ny, 2 * nz, 2)
            randNoise += .25 * noise.snoise3(4 * nx, 2 * ny, 2 * nz, 4)

            # Redistribution
            randNoise = generation.stretchValue(randNoise, redistribPower)

            row.append(randNoise)
        elevation.append(row)

    elevation = generation.normalize2DArray(elevation, -1.0, 1.0)

    # Generate moisture using noise
    nz = random.random()

    octaves = 4
    freq = 1.0
    redistribPower = .3

    for y in range(sizeY):
        row = []
        for x in range(sizeX):
            nx = x / sizeX - (sizeX / 2.0)
            ny = y / sizeY - (sizeY / 2.0)
            randNoise = noise.snoise3(1 * nx, 1 * ny, 1 * nz, 1)
            randNoise += .5 * noise.snoise3(2 * nx, 2 * ny, 2 * nz, 2)
            randNoise += .25 * noise.snoise3(4 * nx, 2 * ny, 2 * nz, 4)

            # Redistribution
            randNoise = generation.stretchValue(randNoise, redistribPower)

            row.append(randNoise)
        moisture.append(row)

    moisture = generation.normalize2DArray(moisture, -1.0, 1.0)

    return elevation, moisture