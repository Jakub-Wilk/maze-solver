from modules.Maze import Maze


class Solver:

    def __init__(self, maze: Maze, begin: tuple[int, int], end: [int, int], animate: bool, steps: int,
                 output: str) -> None:

        self.maze = maze
        # set maze_max_coords to the bottom right pixel coordinates
        maze_max_coords = (len(maze.grid) - 1, len(maze.grid[-1]) - 1)

        self.begin = begin

        # check if begin is in bounds
        if self.begin[0] < 0 or self.begin[0] > maze_max_coords[0]:
            raise IndexError("The beginning x coordinate is outside the image!")
        if self.begin[1] < 0 or self.begin[1] > maze_max_coords[1]:
            raise IndexError("The beginning y coordinate is outside the image!")

        # if end is not set, set it to bottom right
        self.end = maze_max_coords if end is None else end

        # check if end is in bounds
        if self.end[0] < 0 or self.end[0] > maze_max_coords[0]:
            raise IndexError("The ending x coordinate is outside the image!")
        if self.end[1] < 0 or self.end[1] > maze_max_coords[1]:
            raise IndexError("The ending y coordinate is outside the image!")

        self.animate = animate
        self.steps = steps
        self.output = output

    def solve(self) -> None:
        pass
