import noise, pygame, random, datetime
import generation, display

sizeX = 800
sizeY = 800
squareSize = 1
elevation = []

# print(mapArray)

random.seed(datetime.datetime.now())

# Generate perlin noise

nz = random.random()

octaves = 4
freq = 1.0
redistribPower = .3

for y in range(sizeY):
    row = []
    for x in range(sizeX):
        nx = x/sizeX - (sizeX / 2.0)
        ny = y/sizeY - (sizeY / 2.0)
        randNoise = noise.snoise3(1 * nx, 1 * ny, 1 * nz, 1)
        randNoise += .5 * noise.snoise3(2 * nx, 2 * ny, 2 * nz, 2)
        randNoise += .25 * noise.snoise3(4 * nx, 2 * ny, 2 * nz, 4)

        # Redistribution
        randNoise = generation.stretchValue(randNoise, redistribPower)


        # print(randNoise)
        row.append(randNoise)
    elevation.append(row)

# print(mapArray)

elevation = generation.normalizeMapArray(elevation)

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
        color = display.biome(elevation[y][x])
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