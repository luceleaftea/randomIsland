import noise
import pygame
import random

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

# Assumes noise numbers are on a range of -1.0 to 1.0
def convertPerlinToColor(perlin):
    floatColor = (perlin + 1) / 2.0 * 255
    return round(floatColor)

def biome(e):

    WATER = (62, 96, 193)
    BEACH = (93, 128, 252)
    FOREST = (116, 169, 99)
    JUNGLE = (62, 126, 98)
    SAVANNAH = (165, 189, 126)
    DESERT = (191, 210, 175)
    SNOW = (210, 210, 215)

    if (e < 0.1): return WATER
    if (e < 0.2): return BEACH
    if (e < 0.3): return FOREST
    if (e < 0.5): return JUNGLE
    if (e < 0.7): return SAVANNAH
    if (e < 0.9): return DESERT
    return SNOW

sizeX = 800
sizeY = 800
squareSize = 1
mapArray = []

# print(mapArray)

random.seed()

# Generate perlin noise

nz = random.random()

octaves = 4
freq = 1.0

for y in range(sizeY):
    row = []
    for x in range(sizeX):
        nx = x/sizeX - (sizeX / 2.0)
        ny = y/sizeY - (sizeY / 2.0)
        randNoise = noise.snoise3(1 * nx, 1 * ny, 1 * nz, 1)
        randNoise += .5 * noise.snoise3(2 * nx, 2 * ny, 2 * nz, 2)
        randNoise += .25 * noise.snoise3(4 * nx, 2 * ny, 2 * nz, 4)

        # Redistribution (force
        randNoise = pow(randNoise, 1.3)
        if type(randNoise) == complex:
            randNoise = randNoise.real


        # print(randNoise)
        row.append(randNoise)
    mapArray.append(row)

# print(mapArray)

mapArray = normalizeMapArray(mapArray)

# print(mapArray)


# Set up pygame for display
pygame.init()
screen = pygame.display.set_mode([sizeX * squareSize, sizeY * squareSize])
pygame.display.set_caption("Random Islands")

done = False
clock = pygame.time.Clock()

# Draw the perlin noise to the screen
# screen.fill((255, 255, 255))

for y in range(sizeY):
    for x in range(sizeX):
        # color = convertPerlinToColor(mapArray[y][x])
        color = biome(mapArray[y][x])
        # print(color)
        # r = mapNumberToRange(color, 0, 255, 0, 255)
        # g = 255
        # b = mapNumberToRange(color, 0, 255, 29, 255)

        r = color[0]
        g = color[1]
        b = color[2]

        pygame.draw.rect(screen, (r, g, b), [x * squareSize, y * squareSize, squareSize, squareSize])

pygame.display.flip()


# Wait for user to exit
while not done:
    clock.tick(10)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

pygame.quit()