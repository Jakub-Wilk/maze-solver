# possible tile states
TILES = {
    'wall': 0,  # untraversable, black
    'path': 1,  # not explored yet, white
    'unknown': 2,  # branch already explored, but undetermined, red
    'checking': 3,  # the branch currently being checked, green
    'dead': 4  # branch already explored, leads to a dead end, light gray
}

# tile color values

TILE_COLORS = {

}