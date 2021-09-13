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

    def solve(self) -> None:
        pass
