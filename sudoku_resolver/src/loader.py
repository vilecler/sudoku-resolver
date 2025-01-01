"""
Class to Load a Sudoku.

Author: Vivien Leclercq
Created: 01/01/2025
"""

import os
from random import randrange

import numpy as np

from sudoku_resolver.src.models.sudoku import Sudoku


class Loader:
    """
    Class to load a new Sudoku.

    Usage:
        loader = Loader.from_sudoku_number()
        loader.get_sudoku()

        or

        loader = Loader.from_sudoku_number(42)
        loader.get_sudoku()
    """

    SUDOKUS_FILE = os.path.join(os.path.dirname(__file__), "data", "sudoku.csv")
    SUDOKUS_COUNT = 9000000  # Number of sudokus in SUDOKUS_FILE

    def __init__(self, sudoku_number: int):
        if not sudoku_number:
            raise ValueError(f"A sudoku number must be provided, got {sudoku_number}.")

        self.sudoku_number = sudoku_number

    def get_sudoku(self) -> Sudoku:
        """
        Method to trigger the loading of Sudoku.
        """
        raw_sudoku = self._load_raw_sudoku()
        return self._convert_raw_sudoku(raw_sudoku)

    def _load_raw_sudoku(self) -> str:
        with open(self.SUDOKUS_FILE, "r", encoding="utf-8") as file:
            for current_line_number, line in enumerate(file, 1):
                if current_line_number == self.sudoku_number:
                    return line.strip().split(",")[0]
        raise ValueError(f"Unavailable to find sudoku number {self.sudoku_number}.")

    @staticmethod
    def _convert_raw_sudoku(raw_sudoku: str) -> Sudoku:
        """
        Convert raw Sudoku to a Sudoku
        """
        numbers = [int(nb) for nb in raw_sudoku]
        grid = np.array(numbers)
        return Sudoku(grid)

    @classmethod
    def from_sudoku_number(cls, sudoku_number: int = 0):
        """
        Load a sudodu from its number.
        A random number is selected if no number is provided.
        """
        if not sudoku_number:
            sudoku_number = randrange(1, cls.SUDOKUS_COUNT + 1)
        return cls(sudoku_number)
