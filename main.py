from rover import Rover
from grid import Grid
import re
import argparse


def contains_valid_letters(instructions):
    result = bool(re.match('^[MRL]+$', instructions))
    return bool(result)


def is_valid_grid_size(gsize):
    result = True
    if len(gsize) != 2:
        print("\tInput only 2 digits without any spaces.")
        result = False
    if '0' in gsize:
        print("\tNo digit can be 0.")
        result = False
    if gsize == "":
        print("\tInput cannot be empty.")
        result = False
    return result


def is_valid_pos_and_direction(pos_and_direction, gsize):

    pos_and_direction = pos_and_direction.upper()
    valid_directions = ["N", "E", "S", "W", "NORTH", "EAST", "SOUTH", "WEST"]
    result = True

    try:
        pos, direction = pos_and_direction.split(" ")
    except ValueError:
        print("Make sure the position and direction are separated by a space.")
        return False

    if len(pos) != 2:
        print("\tInput a 2 digit position and direction separated by a space.")
        result = False
    if '0' in pos:
        print("\tNo digit can be 0.")
        result = False
    if direction not in valid_directions:
        print("\tDirection must be one of", valid_directions)
        result = False
    if not is_position_in_grid(pos, gsize):
        print("\tPosition not in grid.")
        result = False

    return result


def is_position_in_grid(position, grid_size):
    return not any(int(j) > int(i) for i, j in zip(grid_size, position))


def get_grid_size():
    size = input("Enter terrain size: ")
    while not is_valid_grid_size(size):
        size = input("Enter terrain size: ")
    return int(size[0]), int(size[1])


def get_pos_and_direction(grid_size):

    pos_direction = input("Enter rover position and direction: ").upper()
    while not is_valid_pos_and_direction(pos_direction, grid_size):
        pos_direction = input("Enter rover position and direction: ").upper()

    pos, direction = pos_direction.split(" ")
    return int(pos[0]), int(pos[1]), direction[0]


def get_instructions():
    instructions = input("Input instructions: ").upper()
    while not contains_valid_letters(instructions):
        print("\tInstructions can only contain 'M', 'L' and 'R'.")
        instructions = input("Input instructions: ").upper()
    return instructions


def get_input():
    tmp_rover = Rover()
    tmp_grid = Grid()
    tmp_rover.set_grid(tmp_grid)

    row, column = get_grid_size()
    tmp_rover.get_grid().set_dimensions(row, column)

    rover_row, rover_col, direction = get_pos_and_direction((row, column))
    tmp_rover.set_position(rover_row, rover_col)
    tmp_rover.set_direction(direction)

    # tmp_rover.grid.render_grid(tmp_rover.row, tmp_rover.col, tmp_rover.direction)
    # exit()

    instructions = get_instructions()
    tmp_rover.set_instructions(instructions)
    while not tmp_rover.is_valid_instructions():
        instructions = get_instructions()
        tmp_rover.set_instructions(instructions)
    return row, column, rover_row, rover_col, direction, instructions


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--render", "-r", action="store_true", help="Enable rendering of rover executing instructions.")
    parser.set_defaults(render=False)
    args = parser.parse_args()

    rover = Rover()
    grid = Grid()

    grid_row, grid_col, rover_row, rover_col, direction, instructions = get_input()
    grid.set_dimensions(grid_row, grid_col)
    rover.set_grid(grid)
    rover.set_position(rover_row, rover_col)
    rover.set_direction(direction)
    rover.set_instructions(instructions)

    rover.set_grid(grid)
    rover.execute_instructions(args.render)

    final_position = rover.get_position()
    print("Final co-ordinates: {}{} {}".format(final_position[0], final_position[1], rover.get_direction()))
