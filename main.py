import noise
import pygame
import random

def convertPerlinToColor(perlin):
    # shiftedPerlin = perlin + 1 / 2.0
    # print(perlin)
    # floatColor = shiftedPerlin * 255
    floatColor = (perlin + 1) / 2.0 * 255
    return round(floatColor)

sizeX = 150
sizeY = 150
squareSize = 5
mapArray = []

# print(mapArray)

random.seed()

# Generate perlin noise
# rand = random.randint(0, sizeX)
# nz = ((rand / sizeX) - (sizeX / 2.0))

nz = random.random()

octaves = 4
freq = 4.0

for y in range(sizeY):
    row = []
    for x in range(sizeX):
        nx = x/sizeX - (sizeX / 2.0)
        ny = y/sizeY - (sizeY / 2.0)
        randNoise = noise.snoise3(freq * nx, freq * ny, freq * nz, octaves)
        # print(perlin)
        row.append(randNoise)
    mapArray.append(row)

print(mapArray)


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
        color = convertPerlinToColor(mapArray[y][x])
        # print(color)
        pygame.draw.rect(screen, (color, color, color), [x * squareSize, y * squareSize, squareSize, squareSize])

pygame.display.flip()


# Wait for user to exit
while not done:
    clock.tick(10)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

pygame.quit()