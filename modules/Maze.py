from __future__ import annotations

from PIL import Image

from modules import Constants


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

        # Convert an image of the maze to a two-dimensional list of tiles.
        # Every pixel is determined to be either
        # black-ish ( R+G+B ∈ <0; 256*3/2> ) or white-ish ( R+G+B ∈ (256*3/2; 256*3> )
        grid = []
        for i in range(width):
            grid.append([])
            for j in range(height):
                r, g, b = rgb_image.getpixel((i, j))
                if r + g + b <= 384:
                    tile = Constants.TILES["wall"]
                else:
                    tile = Constants.TILES["path"]
                grid[i].append(tile)

        # return an instance of Maze
        return cls(width, height, grid)

    def is_position_in_bounds(self, position: tuple[int, int]) -> bool:
        if position[0] < 0 or position[0] > self.width:
            return False
        elif position[1] < 0 or position[1] > self.height:
            return False
        else:
            return True

    def get_tile_at(self, position: tuple[int, int]) -> int:
        if not self.is_position_in_bounds(position):
            raise IndexError(f"Position {position} out of bounds!")
        return self.grid[position[0]][position[1]]
