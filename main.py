import noise, pygame, random, datetime
import generation, display

# Initialize global variables and seed the random number generator
sizeX = 800
sizeY = 800
squareSize = 1
elevation = []
moisture = []

random.seed(datetime.datetime.now())

# Generate elevation using noise
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
        nx = x/sizeX - (sizeX / 2.0)
        ny = y/sizeY - (sizeY / 2.0)
        randNoise = noise.snoise3(1 * nx, 1 * ny, 1 * nz, 1)
        randNoise += .5 * noise.snoise3(2 * nx, 2 * ny, 2 * nz, 2)
        randNoise += .25 * noise.snoise3(4 * nx, 2 * ny, 2 * nz, 4)

        # Redistribution
        randNoise = generation.stretchValue(randNoise, redistribPower)

        row.append(randNoise)
    moisture.append(row)

moisture = generation.normalize2DArray(moisture, -1.0, 1.0)

# Set up pygame for display
pygame.init()
screen = pygame.display.set_mode([sizeX * squareSize, sizeY * squareSize])
pygame.display.set_caption("Random Islands")

done = False
clock = pygame.time.Clock()

# Draw the perlin noise to the screen
for y in range(sizeY):
    for x in range(sizeX):
        r, g, b = display.biomeMoistureColoring(elevation[y][x], moisture[y][x])
        # r, g, b = display.biomeColoring(elevation[y][x])

        pygame.draw.rect(screen, (r, g, b), [x * squareSize, y * squareSize, squareSize, squareSize])

pygame.display.flip()


# Wait for user to exit
while not done:
    clock.tick(10)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

pygame.quit()