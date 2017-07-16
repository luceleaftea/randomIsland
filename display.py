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


def biomeMoistureColoring(e, m):
    OCEAN = (68, 68, 122)
    BEACH = (160, 144, 119)
    SCORCHED = (85, 85, 85)
    BARE = (136, 136, 136)
    TUNDRA = (187, 187, 170)
    SNOW = (221, 221, 228)
    TEMPERATE_DESERT = (201, 210, 155)
    SHRUBLAND = (136, 153, 119)
    TAIGA = (153, 170, 119)
    GRASSLAND = (136, 170, 85)
    TEMPERATE_DECIDUOUS_FOREST = (103, 148, 89)
    TEMPERATE_RAIN_FOREST = (68, 136, 85)
    SUBTROPICAL_DESERT = (210, 185, 139)
    TROPICAL_SEASONAL_FOREST = (85, 153, 68)
    TROPICAL_RAIN_FOREST = (51, 119, 85)


    if (e < 0.1): return OCEAN
    if (e < 0.12): return BEACH

    if (e > 0.8):
        if (m < 0.1): return SCORCHED
        if (m < 0.2): return BARE
        if (m < 0.5): return TUNDRA
        return SNOW;

    if (e > 0.6):
        if (m < 0.33): return TEMPERATE_DESERT
        if (m < 0.66): return SHRUBLAND
        return TAIGA

    if (e > 0.3):
        if (m < 0.16): return TEMPERATE_DESERT
        if (m < 0.50): return GRASSLAND
        if (m < 0.83): return TEMPERATE_DECIDUOUS_FOREST
        return TEMPERATE_RAIN_FOREST

    if (m < 0.16): return SUBTROPICAL_DESERT
    if (m < 0.33): return GRASSLAND
    if (m < 0.66): return TROPICAL_SEASONAL_FOREST
    return TROPICAL_RAIN_FOREST

# Converts a noise value into 3 values representing RGB
def grayscaleColoring(noiseNum):
    color = convertNoiseToColor(noiseNum)
    r = generation.mapNumberToRange(color, 0, 255, 0, 255)
    g = 255
    b = generation.mapNumberToRange(color, 0, 255, 29, 255)
    return (r, g, b)