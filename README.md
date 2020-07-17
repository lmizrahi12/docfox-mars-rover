# Docfox Mars Rover Challenge

## Introduction
The solution was written in python 3.6 and is comprised of four parts, the Rover class, the Grid class, the ```main.py``` driver file and the ```tests.py``` unit tests. The Rover class stores all the variables needed for the rover, such as its position and direction, as well as the methods to perform the supplied instructions. The Grid class contains the boundary sizes as well as methods to render the grid if desired. The main file accepts and validates any input before giving it to the Rover and Grid objects. The unit tests test the various functions of the program to ensure their correctness.

## Input
When the main file is run, prompts are displayed to input the boundary size, rover position, rover direction and instructions. The boundary size must be inputted as two single digits without any spaces, e.g. ```88```. The rover position and direction are inputted together separated by a space. Like the boundary size, the position must be entered as two digits without any spaces. The direction must be one of north, south, east or west. The first letter for the direction can be used as well, e.g. n instead of north. Case is not important for the direction. An example for position and direction is ```12 E```. The instructions are inputted as a string consisting of ‘M’, ‘R’ and ‘L’ without spaces. Case is not important. The instructions will not be accepted if they force the rover to move out of bounds and the user will be prompted to input another instruction sequence. The final position and direction will be printed at the end. Appropriate error messages for wrong input will be displayed for all prompts. There is also an optional command line flag ```–-render``` (or ```-r```) if the user wants to enable rendering of the rover executing instructions. To enable rendering, use python main.py ```-–render```. By default, rendering is disabled. The terminaltables library was used to generate the rendered grid. To install use ```pip install terminaltables``` however, this is optional and the program should work whether it is installed or not.

## Design
The ```main.py``` file was designed to receive and process all the input before it is given to the rover object. If this were to be a real rover communication program, the input processing and validation would have to be done locally. The communication delay would be too long if the rover itself were to validate its own information.
The Grid class contains the boundary size and some methods to visualize it. The visualization is made up of a table with coordinates and an arrow with a direction to show the location of the rover. The grid in this case is simple but if it were more complex and had obstacles or an unregular shape, then it would be convenient to have a separate class to store all the obstacles.

The Rover class contains its position, direction, helper functions, Grid object and getters and setters for each attribute. A grid is given to the rover for convenience. Also, as the rover would explore it would update its own map. The main methods are ```is_valid_instructions```, ```move```, ```rotate_left``` and ```rotate_right```. The is_valid_instructions method will run through the given instructions and check if the rover stays within the grid. If it does not stay within the grid, then it returns False otherwise True. The Rover class contains a dictionary which stores each direction and their corresponding movement. When the rover is instructed to move, it looks up the movement it needs to make and applies it. For example, if the rover is facing west then it looks up the corresponding movement which is ```(-1, 0)```. This means that the rover will move one space left on the horizontal axis and zero spaces on the vertical axis.

When the rover is instructed to rotate left, it creates a list of directions going counterclockwise, i.e.
north, west, south, east. It then finds the index of the direction it is facing and reassigns direction to the
direction at the next index. The function for rotating right is the same except for the directions going
clockwise. The reason for storing the movements and directions is to avoid many if statements which
could become less readable. This also makes the code easier to extend.

## Correctness
The correctness of the program was checked with unit tests using the built-in unittest framework. The
tests are found in the ```test.py``` file. The tests are split into three classes, testing boundary input, testing
rover position and direction input and finally, instruction and movement input. The tests were created
to try and cover every input case. The boundary input is tested for:
* empty input,
* a single digit,
* double digits including zeros,
* more than double digits
* and any space characters.

The position and direction input are tested for the same conditions as boundary input as well as:
* direction being one of the accepted formats,
* and position being within the given boundary.

The instruction input is tested for:
* each individual instruction to perform as expected,
* movement in every direction to perform as expected,
* movement keeping the rover within the boundary,
* and edge cases such as one (or both) dimension(s) of the boundary being 1 or 9.

Currently every case has passed. To run the tests, use ```python tests.py```.

## Assumptions
The input is assumed to be alphanumeric and not contain any special characters. The input is assumed
to not contain any leading or trailing space characters. The boundary dimensions are only single digits,
therefore the rover position is also only single digits. The instructions will be rejected if the rover is
forced out of bounds, therefore only instructions which keep the rover in the boundary are accepted.
