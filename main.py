import random, datetime, timeit
import generation, display

# Initialize global variables and seed the random number generator
sizeX = 800
sizeY = 800
squareSize = 1
elevation = []
moisture = []

random.seed(datetime.datetime.now())

# start_time = timeit.default_timer()
elevation, moisture = generation.generateElevationMoisture(sizeX, sizeY)
# print(timeit.default_timer() - start_time)

display.pygameDisplay(sizeX, sizeY, squareSize, elevation, moisture)