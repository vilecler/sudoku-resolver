"""
Class to represent a Sudoku matrix.

Author: Vivien Leclercq
Created: 01/01/2025
"""

import numpy as np
import numpy.typing as npt


class Sudoku:
    """
    Class to represent a Sudoku, it is based on numpy.
    """

    def __init__(self, grid: npt.ArrayLike):
        self.grid = grid

    def display(self):
        """
        Display the current sudoku to the console.
        """
        print("-" + "".join(["-"] * 9 * 4))

        rows = np.split(self.grid, len(self.grid) // 9)
        for row in rows:
            row = "| " + " ".join((str(row[j]) + " |") if row[j] != 0 else ". |" for j in range(9))
            print(row)
            print("-" + "".join(["-"] * 9 * 4))
