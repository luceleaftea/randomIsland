import noise, pygame, random, datetime
import generation, display

# Initialize global variables and seed the random number generator
sizeX = 800
sizeY = 800
squareSize = 1
elevation = []
moisture = []

random.seed(datetime.datetime.now())

elevation, moisture = generation.generateElevationMoisture(sizeX, sizeY)

display.pygameDisplay(sizeX, sizeY, squareSize, elevation, moisture)