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