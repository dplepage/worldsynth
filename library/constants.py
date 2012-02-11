#!/usr/bin/python
#
# Constants for world generation that typically are used across multiple modules
# the main code itself.
#
#

# Direction
NORTH = [0,-1]
NORTH_EAST = [1,-1]
EAST = [1,0]
SOUTH_EAST = [1,1]
SOUTH = [0,1]
SOUTH_WEST = [-1,1]
WEST = [-1,0]
NORTH_WEST = [-1,-1]
CENTER = [0,0]

DIR_NEIGHBORS = [NORTH, EAST, SOUTH, WEST]
DIR_NEIGHBORS_CENTER = [CENTER, NORTH, EAST, SOUTH, WEST]
DIR_ALL = [NORTH, NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST, NORTH_WEST]
DIR_ALL_CENTER = [CENTER, NORTH, NORTH_EAST, EAST, SOUTH_EAST, SOUTH, SOUTH_WEST, WEST, NORTH_WEST]

#Biomes
BIOME_TYPE_UNDEFINED       = 0
BIOME_TYPE_WATER           = 1
BIOME_TYPE_GRASSLAND       = 2
BIOME_TYPE_FOREST          = 3
BIOME_TYPE_DESERT_SAND     = 4
BIOME_TYPE_DESERT_ROCK     = 5
BIOME_TYPE_MOUNTAIN_LOW    = 6
BIOME_TYPE_MOUNTAIN_HIGH   = 7
BIOME_TYPE_SAVANNAH        = 8
BIOME_TYPE_MARSH           = 9
BIOME_TYPE_SHRUBLAND       = 10
BIOME_TYPE_HILLS           = 11
BIOME_TYPE_SWAMP           = 12
BIOME_TYPE_DESERT_BADLANDS = 13
BIOME_TYPE_MOUNTAIN        = 14
BIOME_TYPE_MOUNTAIN_PEAK   = 15

# BIOME_ELEVATION
BIOME_ELEVATION_HILLS_LOW = 0.60
BIOME_ELEVATION_HILLS = 0.75
BIOME_ELEVATION_MOUNTAIN_LOW = 0.85
BIOME_ELEVATION_MOUNTAIN = 0.90
BIOME_ELEVATION_MOUNTAIN_HIGH = 0.95
BIOME_ELEVATION_MOUNTAIN_PEAK = 1.00

# MOVEMENT
DIAGONAL_COST = 1.41

# World contants
WGEN_HEMISPHERE_NORTH   = 1
WGEN_HEMISPHERE_EQUATOR = 2
WGEN_HEMISPHERE_SOUTH   = 3
WGEN_SEA_LEVEL = 0.25
WIND_OFFSET = 180
WIND_PARITY = -1 # -1 or 1
WGEN_WIND_RESOLUTION = 4 # 1 is perfect, higher = rougher
WGEN_RAIN_FALLOFF = 0.2 # Default 0.2 - less for less rain, more for more rain
WGEN_WIND_GRAVITY = 0.975
TEMPERATURE_BAND_RESOLUTION = 2 # 1 is perfect, higher = rougher

#Colour contant
# http://df.magmawiki.com/index.php/Colour (as reference)
COLOR_BLACK = 0x000000
COLOR_CLEAR = 0x808080
COLOR_GRAY = 0x808080
COLOR_SILVER = 0xC0C0C0
COLOR_WHITE = 0xFFFFFF
COLOR_TAUPE_ROSE = 0x905D5D
COLOR_CHESTNUT = 0xCD5C5C
COLOR_MAROON = 0x800000
COLOR_RED = 0xFF0000
COLOR_VERMILION = 0xE34234
COLOR_RUSSET = 0x755A57
COLOR_SCARLET = 0xFF2400
COLOR_BURNT_UMBER = 0x8A3324
COLOR_TAUPE_MEDIUM = 0x674C47
COLOR_DARK_CHESTNUT = 0x986960
COLOR_BURNT_SIENNA = 0xE97451
COLOR_RUST = 0xB7410E
COLOR_AUBURN = 0x6F351A
COLOR_MAHOGANY = 0xC04000
COLOR_PUMPKIN = 0xFF7518
COLOR_CHOCOLATE = 0xD2691E
COLOR_TAUPE_PALE = 0xBC987E
COLOR_TAUPE_DARK = 0x483C32
COLOR_DARK_PEACH = 0xFFDAB9
COLOR_COPPER = 0xB87333
COLOR_LIGHT_BROWN = 0xCD853F
COLOR_BRONZE = 0xCD7F32
COLOR_PALE_BROWN = 0x987654
COLOR_DARK_BROWN = 0x654321
COLOR_SEPIA = 0x704214
COLOR_OCHRE = 0xCC7722
COLOR_BROWN = 0x964B00
COLOR_CINNAMON = 0x7B3F00
COLOR_TAN = 0xD2B48C
COLOR_RAW_UMBER = 0x734A12
COLOR_ORANGE = 0xFFA500
COLOR_PEACH = 0xFFE5B4
COLOR_TAUPE_SANDY = 0x967117
COLOR_GOLDENROD = 0xDAA520
COLOR_AMBER = 0xFFBF00
COLOR_DARK_TAN = 0x918151
COLOR_SAFFRON = 0xF4C430
COLOR_ECRU = 0xC2B280
COLOR_GOLD = 0xD4AF37
COLOR_PEARL = 0xF0EAD6
COLOR_BUFF = 0xF0DC82
COLOR_FLAX = 0xEEDC82
COLOR_BRASS = 0xB5A642
COLOR_GOLDEN_YELLOW = 0xFFDF00
COLOR_LEMON = 0xFDE910
COLOR_CREAM = 0xFFFDD0
COLOR_BEIGE = 0xF5F5DC
COLOR_OLIVE = 0x808000
COLOR_YELLOW = 0xFFFF00
COLOR_IVORY = 0xFFFFF0
COLOR_LIME = 0xCCFF00
COLOR_YELLOW_GREEN = 0x9ACD32
COLOR_DARK_OLIVE = 0x556832
COLOR_GREEN_YELLOW = 0xADFF2F
COLOR_CHARTREUSE = 0x7FFF00
COLOR_FERN_GREEN = 0x4F7942
COLOR_MOSS_GREEN = 0xADDFAD
COLOR_GREEN = 0x00FF00
COLOR_MINT_GREEN = 0x98FF98
COLOR_ASH_GRAY = 0xB2BEB5
COLOR_EMERALD = 0x50C878
COLOR_SEA_GREEN = 0x2E8B57
COLOR_SPRING_GREEN = 0x00FF7F
COLOR_DARK_GREEN = 0x013220
COLOR_JADE = 0x00A86B
COLOR_AQUAMARINE = 0x7FFFD4
COLOR_PINE_GREEN = 0x01796F
COLOR_TURQUOISE = 0x30D5C8
COLOR_PALE_BLUE = 0xAFEEEE
COLOR_TEAL = 0x008080
COLOR_AQUA = 0x00FFFF
COLOR_LIGHT_BLUE = 0xADD8E6
COLOR_CERULEAN = 0x007BA7
COLOR_SKY_BLUE = 0x87CEEB
COLOR_CHARCOAL = 0x36454F
COLOR_SLATE_GRAY = 0x708090
COLOR_MIDNIGHT_BLUE = 0x003366
COLOR_AZURE = 0x007FFF
COLOR_COBALT = 0x0047AB
COLOR_LAVENDER = 0xE6E6FA
COLOR_DARK_BLUE = 0x00008B
COLOR_BLUE = 0x0000FF
COLOR_PERIWINKLE = 0xCCCCFF
COLOR_DARK_VIOLET = 0x423189
COLOR_AMETHYST = 0x9966CC
COLOR_DARK_INDIGO = 0x310062
COLOR_VIOLET = 0x8B00FF
COLOR_INDIGO = 0x4B0082
COLOR_PURPLE = 0x660099
COLOR_HELIOTROPE = 0xDF73FF
COLOR_LILAC = 0xC8A2C8
COLOR_PLUM = 0x660066
COLOR_TAUPE_PURPLE = 0x50404D
COLOR_TAUPE_GRAY = 0x8B8589
COLOR_FUCHSIA = 0xF400A1
COLOR_MAUVE = 0x993366
COLOR_LAVENDER_BLUSH = 0xFFF0F5
COLOR_DARK_PINK = 0xE75480
COLOR_MAUVE_TAUPE = 0x915F6D
COLOR_DARK_SCARLET = 0x560319
COLOR_PUCE = 0xCC8899
COLOR_CRIMSON = 0xDC143C
COLOR_PINK = 0xFFC0CB
COLOR_CARDINAL = 0xC41E3A
COLOR_CARMINE = 0x960018
COLOR_PALE_PINK = 0xFADADD
COLOR_PALE_CHESTNUT = 0xDDADAF
