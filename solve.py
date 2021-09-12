from __future__ import annotations

from argparse import ArgumentParser, RawTextHelpFormatter

from PIL import Image

from modules.Maze import Maze
from modules.Solver import Solver


def main() -> None:
    parser = ArgumentParser(description="A rudimentary maze solver", formatter_class=RawTextHelpFormatter)
    parser.add_argument(
        "-p",
        "--path",
        default="mazes/test_maze.png",
        metavar="<path>",
        help="specifies the path to the maze"
    )
    parser.add_argument(
        "-b",
        "--begin",
        nargs=2,
        default=(0, 0),
        type=int,
        metavar=("<x>", "<y>"),
        help="specifies where the solver should start\n(defaults to \"0 0\")"
    )
    parser.add_argument(
        "-e",
        "--end",
        nargs=2,
        default=None,
        type=int,
        metavar=("<x>", "<y>"),
        help="specifies where the solver should end\n(defaults to the bottom right pixel)"
    )
    parser.add_argument(
        "-a",
        "--animate",
        action="store_true",
        help="turns on animation mode\nthe solver will render images every few steps of the process\n(every single "
             "step by default) "
    )
    parser.add_argument(
        "-s",
        "--steps",
        default=1,
        type=int,
        metavar="<step count>",
        help="specifies how often an animation frame will be rendered\n(defaults to 1)"
    )
    parser.add_argument(
        "-o",
        "--output",
        default="output.png",
        metavar="<path>",
        help="specifies the output file (or directory, if animating)\n(defaults to output.png)"
    )
    args = parser.parse_args()

    image = Image.open(args.path)
    maze = Maze.create_from_image(image)
    solver = Solver(maze, args.begin, args.end, args.animate, args.steps, args.output)

    solver.solve()


if __name__ == '__main__':
    main()
