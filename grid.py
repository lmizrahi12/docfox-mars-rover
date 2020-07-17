try:
    from terminaltables import SingleTable
    render = True
except ImportError:
    print("Terminaltables not found. Grid will not be rendered.")
    render = False

from time import sleep
from os import system
from sys import platform


class Grid:
    def __init__(self):
        self.rows = -1
        self.cols = -1
        self.arrows = {"W": "\u2190", "N": "\u2191", "E": "\u2192", "S": "\u2193"}
        self.clear_command = "cls" if platform == 'win32' else "clear"

    def set_dimensions(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def get_dimensions(self):
        return self.rows, self.cols

    def build_grid(self, rover_row, rover_col, rover_dir):
        grid = []
        for i in range(self.cols, 0, -1):
            row = [str(i)]
            for j in range(self.rows):
                row.append(self.arrows[rover_dir] if (rover_row == j+1 and rover_col == i) else "")
            grid.append(row)
        headings = [str(x+1) for x in range(self.rows)]
        headings.insert(0, "")
        grid.append(headings)

        grid = SingleTable(grid)
        grid.padding_left = 2
        grid.padding_right = 2
        grid.inner_heading_row_border = True
        grid.inner_column_border = True
        grid.outer_border = False
        grid.inner_row_border = True
        return grid.table

    def print_grid(self, grid, instructions):
        system(self.clear_command)
        print(grid)
        print("Instructions:", instructions)
        sleep(0.8)

    def render_grid(self, rover_row, rover_col, rover_dir, instructions):
        if render:
            grid = self.build_grid(rover_row, rover_col, rover_dir)
            self.print_grid(grid, instructions)
