import generation

# Converts noise values to a RGB scale (0-255)
# Assumes noise values are on a range of -1.0 to 1.0
def convertNoiseToColor(noiseNum):
    floatColor = (noiseNum + 1) / 2.0 * 255
    return round(floatColor)

# Converts noise values to specified biome RGB values
# Assumes noise values are on a scale of 0.0 to 1.0
def biomeColoring(noiseNum):

    WATER = (62, 96, 193)
    BEACH = (93, 128, 252)
    FOREST = (116, 169, 99)
    JUNGLE = (62, 126, 98)
    SAVANNAH = (165, 189, 126)
    DESERT = (191, 210, 175)
    SNOW = (210, 210, 215)

    if (noiseNum < 0.1): return WATER
    if (noiseNum < 0.2): return BEACH
    if (noiseNum < 0.3): return FOREST
    if (noiseNum < 0.5): return JUNGLE
    if (noiseNum < 0.7): return SAVANNAH
    if (noiseNum < 0.9): return DESERT
    return SNOW

# Converts a noise value into 3 values representing RGB
def grayscaleColoring(noiseNum):
    color = convertNoiseToColor(noiseNum)
    r = generation.mapNumberToRange(color, 0, 255, 0, 255)
    g = 255
    b = generation.mapNumberToRange(color, 0, 255, 29, 255)
    return (r, g, b)