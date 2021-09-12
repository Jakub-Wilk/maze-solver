from __future__ import annotations

from PIL import Image

import Constants


class Maze:

    # this class is a representation of a maze

    def __init__(self, width: int, height: int, grid: list) -> None:
        self.width = width
        self.height = height
        self.grid = grid

    @classmethod
    def create_from_image(cls, image: Image) -> Maze:
        width = image.size[0]
        height = image.size[1]
        rgb_image = image.convert("RGB")
        grid = []
        for i in range(width):
            grid.append([])
            for j in range(height):
                r, g, b = rgb_image.getpixel((j, i))
                if r + g + b <= 384:
                    tile = Constants.TILES["wall"]
                else:
                    tile = Constants.TILES["path"]
                grid[i].append(tile)
        return cls(width, height, grid)
