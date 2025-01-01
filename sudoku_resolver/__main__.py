"""
Main of the project.

Author: Vivien Leclercq
Created: 01/01/2025
"""

import sys

from sudoku_resolver.src.loader import Loader


def main(argv: list[str]):
    """
    Main entrypoint of the program.
    """
    loader = Loader.from_sudoku_number()
    sudoku = loader.get_sudoku()

    sudoku.display()


if __name__ == "__main__":
    main(sys.argv)
