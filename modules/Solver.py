class Solver:

    def __init__(self, maze, begin, end, animate, steps, output):
        self.maze = maze
        self.begin = begin
        self.end = (len(maze) - 1, len(maze[-1]) - 1) if end is None else end
        self.animate = animate
        self.steps = steps
        self.output = output

    def solve(self):
        pass