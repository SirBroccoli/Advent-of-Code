'''
--- Day 6: Guard Gallivant ---
The Historians use their fancy device again, 
this time to whisk you all away to the North Pole 
prototype suit manufacturing lab... in the year 1518! 
It turns out that having direct access to history is 
very convenient for a group of historians.

You still have to be careful of time paradoxes, 
and so it will be important to avoid anyone from 
1518 while The Historians search for the Chief. 
Unfortunately, a single guard is patrolling 
this part of the lab.

Maybe you can work out where the guard will go ahead 
of time so that The Historians can search safely?

You start by making a map (your puzzle input) 
of the situation. For example:

....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
The map shows the current position of the guard 
with ^ (to indicate the guard is currently facing up 
from the perspective of the map). Any obstructions -
 crates, desks, alchemical reactors, etc. - are shown as #.

Lab guards in 1518 follow a very strict patrol protocol
 which involves repeatedly following these steps:

If there is something directly in front of you, 
turn right 90 degrees.
Otherwise, take a step forward.
Following the above protocol,
the guard moves up several times until she 
reaches an obstacle (in this case, a pile of failed suit prototypes):

....#.....
....^....#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
Because there is now an obstacle in front of the guard, 
she turns right before continuing straight in her new facing direction:

....#.....
........>#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
Reaching another obstacle (a spool of several very long polymers), 
she turns right again and continues downward:

....#.....
.........#
..........
..#.......
.......#..
..........
.#......v.
........#.
#.........
......#...
This process continues for a while, 
but the guard eventually leaves the 
mapped area (after walking past a tank of universal solvent):

....#.....
.........#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#v..
By predicting the guard's route, 
you can determine which specific positions 
in the lab will be in the patrol path. 
Including the guard's starting position, 
the positions visited by the guard before 
leaving the area are marked with an X:

....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..
In this example, the guard will visit 
41 distinct positions on your map.

Predict the path of the guard. 
How many distinct positions will 
the guard visit before leaving the mapped area?
'''

with open('/home/pi/Documents/PythonFiles/Advent of Code 2024/Day 6/puzzle.txt', 'r') as f:
    file = [line.strip() for line in f] 
    puzzle = [list(i) for i in file]

def checkNorth(puzzle, x, y):
    '''
    Check if before moving north you would run into an Obstacle
    returns True if No obstacles
    Returns False if theres an Obstacle, AND change the orientation of the guard 90 degrees turn right
    '''
    north_element_debugger = puzzle[x-1][y]
    if puzzle[x-1][y] != '#':
        return True
    else:
        return False
def moveNorth(x, y):
    '''
    AFter Checking the North Element for Obstacles, Move Guard North
    Makes previous spot a New Value 'O' to keep track of distinct spaces visited
    Returns a new starting Point
    Returns x, y    
    ***Don't forget to save the variables
    ***and the Guards Pointing Direction
    IE x_position, y_position, marker = moveNorth(puzzle, x, y, marker)
    '''
    x -= 1
    if x < 0 or x >= 130:
        raise IndexError("Index Error moveNorth")
    return x, y
def checkEast(puzzle, x, y):
    '''
    Check if before moving East you would run into an Obstacle
    returns True if No obstacles
    Returns False if theres an Obstacle, AND change the orientation of the guard 90 degrees turn right
    '''
    if puzzle[x][y+1] != '#':
        return True
    else:
        return False
def moveEast(x, y):
    '''
    AFter Checking the East Element for Obstacles, Move Guard East
    Returns a new starting Point
    Returns x, y    
    ***Don't forget to save the variables
    ***and the Guards Pointing Direction
    IE x_position, y_position, marker = moveNorth(puzzle, x, y, marker)
    '''
    y += 1
    if y < 0 or y >= 130:
        raise IndexError('Index Error moveEast')
    return x, y
def checkSouth(puzzle, x, y):
    '''
    Check if before moving South you would run into an Obstacle
    returns True if No obstacles
    Returns False if theres an Obstacle, AND change the orientation of the guard 90 degrees turn right
    '''
    if puzzle[x+1][y] != '#':
        return True
    else:
        return False
def moveSouth(x, y):
    '''
    AFter Checking the South Element for Obstacles, Move Guard South
    Returns a new starting Point
    Returns x, y    
    ***Don't forget to save the variables
    ***and the Guards Pointing Direction
    IE x_position, y_position, marker = moveNorth(puzzle, x, y, marker)
    '''
    x += 1
    if x < 0 or x >= 130:
        raise IndexError("Index Error moveSouth")
    
    return x, y
def checkWest(puzzle, x, y):
    '''
    Check if before moving West you would run into an Obstacle
    returns True if No obstacles
    Returns False if theres an Obstacle, AND change the orientation of the guard 90 degrees turn right
    '''
    if puzzle[x][y-1] != '#':
        return True
    else:
        return False
def moveWest(x, y):
    '''
    AFter Checking the West Element for Obstacles, Move Guard West
    Returns a new starting Point
    Returns x, y    
    ***Don't forget to save the variables
    ***and the Guards Pointing Direction
    IE x_position, y_position, marker = moveNorth(puzzle, x, y, marker)
    '''
    y -= 1
    if y < 0 or y >= 130:
        raise IndexError('Index Error moveWest')
    return x, y

directions = ['<', '>', '^', 'V', '*']
starting_point = [45, 47]
test = 0
x_position = 45
y_positions = 47
guard_icon = '^'

## Visual Guide to see the Guard moving and WHY DOES SHE KEEP MOVING OUT OF BOUNDS!!!! WTF
# puzzle_mapped = [''.join(s) for s in puzzle]
# guard_map = open('/home/pi/Documents/PythonFiles/Advent of Code 2024/Day 6/puzzle_COPY.txt', 'w')
# for i in puzzle_mapped:
#     guard_map.write(i + '\n')

moving = True
turns = 1
print(f'starting at Position {x_position, y_positions}')
while moving:
    try:
        # moving North
        if guard_icon == '^':
            puzzle[x_position][y_positions] = '*'
            if checkNorth(puzzle, x_position, y_positions) == True:
                x_position, y_positions = moveNorth(x_position, y_positions)
            else:
                guard_icon = '>'
        
        # Moving East
        elif guard_icon == '>':
            puzzle[x_position][y_positions] = '*'
            if checkEast(puzzle, x_position, y_positions) == True:
                x_position, y_positions = moveEast(x_position, y_positions)
            else:
                guard_icon = 'v'

        # Moving South
        elif guard_icon == 'v':
            puzzle[x_position][y_positions] = '*'
            if checkSouth(puzzle, x_position, y_positions) == True:
                x_position, y_positions = moveSouth(x_position, y_positions)
            else:
                guard_icon = '<'

        # Moving West
        elif guard_icon == '<':
            puzzle[x_position][y_positions] = '*'
            if checkWest(puzzle, x_position, y_positions) == True:
                x_position, y_positions = moveWest(x_position, y_positions)
            else:
                guard_icon = '^'
    
    except IndexError:
        moving = False
        break

puzzle_mapped = [''.join(s) for s in puzzle]
guard_map = open('/home/pi/Documents/PythonFiles/Advent of Code 2024/Day 6/puzzle_COPY.txt', 'w')
for i in puzzle_mapped:
    guard_map.write(i + '\n')

tally = 0
for i in puzzle_mapped:
    for j in i:
        if j in directions:
            tally += 1

original_hash = 0
copy_hash = 0

for i in puzzle:
    for j in i:
        if j == '#':
            original_hash += 1
for i in puzzle_mapped:
    for j in i:
        if j == '#':
            copy_hash += 1

print(original_hash, copy_hash)
print(tally)