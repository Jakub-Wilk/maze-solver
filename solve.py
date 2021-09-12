from __future__ import annotations

import argparse
import sys

from PIL import Image

from modules.Maze import Maze


def main(path: str) -> None:
    image = Image.open(path)
    maze = Maze.create_from_image(image)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A rudimentary maze solver")
    parser.add_argument('-p', '--path', default="mazes/test_maze.png", help="The path to the image containing the maze")
    args = parser.parse_args()
    main(args.path)
