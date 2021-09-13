from modules.Maze import Maze


class Solver:

    # this class is responsible for traversing the maze and determining a correct route

    def __init__(self, maze: Maze, begin: tuple[int, int], end: [int, int], animate: bool, steps: int,
                 output: str) -> None:

        self.maze = maze
        self.begin = begin

        # check if begin is in bounds
        if not self.maze.is_position_in_bounds(self.begin):
            raise IndexError("Begin position out of bounds!")

        # if end is not set, set it to bottom right
        self.end = (self.maze.width, self.maze.height) if end is None else end

        # check if end is in bounds
        if not self.maze.is_position_in_bounds(self.end):
            raise IndexError("End position out of bounds!")

        self.animate = animate
        self.steps = steps
        self.output = output

    def is_crossroads(self, position: tuple[int, int]) -> bool:
        # this function returns True if the current tile has three or four neighbouring traversable tiles
        x, y = position
        north = 1 if self.maze.get_tile_at((x, y + 1)) else 0
        east = 1 if self.maze.get_tile_at((x + 1, y)) else 0
        south = 1 if self.maze.get_tile_at((x, y - 1)) else 0
        west = 1 if self.maze.get_tile_at((x - 1, y)) else 0
        if north + east + south + west > 2:
            return True
        else:
            return False

    def solve(self) -> None:
        pass
