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

def puzzleRead():
    with open('/home/pi/Documents/PythonFiles/Advent of Code/2024/Day 6/puzzle.txt', 'r') as f:
        file = [line.strip() for line in f] 
        puzzle = [list(i) for i in file]
    return puzzle

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

def movingMain(puzzle):
    '''
    main function that moves the guard around the puzzle and around obstacles
    Using the move functions and check functions, it alters the puzzle and shows spaces the guard has visited\n
    Starting Position is Hardcoded as it is specific to this puzzle.\n
    returns the puzzle\n
    Returns a List of Lists
    '''
    x_position = 45
    y_positions = 47
    guard_icon = '^'
    moving = True

    # print(f'starting at Position {x_position, y_positions}') # Used for debugging back in the beginning
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

    return puzzle

def mapGuardPositionsToText(puzzle):
    puzzle_mapped = [''.join(s) for s in puzzle]
    guard_map = open('/home/pi/Documents/PythonFiles/Advent of Code/2024/Day 6/puzzle_COPY.txt', 'w')
    for i in puzzle_mapped:
        guard_map.write(i + '\n')
    return puzzle_mapped
def uniquePositions(puzzle_mapped):
    directions = ['<', '>', '^', 'V', '*']
    tally = 0
    for i in puzzle_mapped:
        for j in i:
            if j in directions:
                tally += 1
    return tally


# Run the Main Function
puzzle = puzzleRead()
puzzle = movingMain(puzzle)
puzzle_mapped = mapGuardPositionsToText(puzzle)
tally = uniquePositions(puzzle_mapped)
print(tally) # Answer is 4580

'''
--- Part Two ---
While The Historians begin working around the guard's patrol route, 
you borrow their fancy device and step outside the lab. 
From the safety of a supply closet, 
you time travel through the last few months and record the nightly status
 of the lab's guard post on the walls of the closet.

Returning after what seems like only a few seconds to The Historians, 
they explain that the guard's patrol area is simply too large for them 
to safely search the lab without getting caught.

Fortunately, they are pretty sure that adding a single new obstruction 
won't cause a time paradox. They'd like to place the new obstruction in 
such a way that the guard will get stuck in a loop, making the rest of 
the lab safe to search.

To have the lowest chance of creating a time paradox, The Historians 
would like to know all of the possible positions for such an obstruction. 
The new obstruction can't be placed at the guard's starting position - the 
guard is there right now and would notice.

In the above example, there are only 6 different positions where a new 
obstruction would cause the guard to get stuck in a loop. The diagrams of 
these six situations use O to mark the new obstruction, | to show a 
position where the guard moves up/down, - to show a position where the 
guard moves left/right, and + to show a position where the guard moves 
both up/down and left/right.

Option one, put a printing press next to the guard's starting position:

....#.....
....+---+#
....|...|.
..#.|...|.
....|..#|.
....|...|.
.#.O^---+.
........#.
#.........
......#...
Option two, put a stack of failed suit prototypes in the bottom right quadrant of the mapped area:


....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
......O.#.
#.........
......#...
Option three, put a crate of chimney-squeeze prototype fabric next to the standing desk in the bottom right quadrant:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----+O#.
#+----+...
......#...
Option four, put an alchemical retroencabulator near the bottom left corner:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
..|...|.#.
#O+---+...
......#...
Option five, put the alchemical retroencabulator a bit to the right instead:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
....|.|.#.
#..O+-+...
......#...
Option six, put a tank of sovereign glue right next to the tank of universal solvent:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----++#.
#+----++..
......#O..
It doesn't really matter what you choose to use as an obstacle so 
long as you and The Historians can put it into position without 
the guard noticing. The important thing is having enough options 
that you can find one that minimizes time paradoxes, and in this 
example, there are 6 different positions you could choose.

You need to get the guard stuck in a loop by adding a single new 
obstruction. How many different positions could you choose for 
this obstruction?
'''

def movingPartTwo(puzzle):
    '''
    A Copy of the movingMain function but with a few changes\n
    This function will similarly move the guard around the puzzle and around obstacles
    however, it now returns True if the guard sucessfully enters a infinite loop.
    # This function will not alter the original argument text file\n
    Returns True if Infinite Loop\n
    returns False if the guard leaves the puzzle\n
    '''
    x_position = 45
    y_positions = 47
    guard_icon = '^'
    moving = True
    # puzzle_copy = puzzle.copy()
    while moving:
        try:

        # moving North
            if guard_icon == '^':
                puzzle[x_position][y_positions] = '*'
                if checkNorth(puzzle, x_position, y_positions) == True:
                    x_position, y_positions = moveNorth(x_position, y_positions)
                    print(f'Moved North {x_position, y_positions}')
                else:
                    # Stayed in place and looked East
                    guard_icon = '>'
        
        # Moving East
            elif guard_icon == '>':
                puzzle[x_position][y_positions] = '*'
                if checkEast(puzzle, x_position, y_positions) == True:
                    x_position, y_positions = moveEast(x_position, y_positions)
                    print(f'Moved East {x_position, y_positions}')
                else:
                    # Stayed in place and looked South
                    guard_icon = 'v'

        # Moving South
            elif guard_icon == 'v':
                puzzle[x_position][y_positions] = '*'
                if checkSouth(puzzle, x_position, y_positions) == True:
                    x_position, y_positions = moveSouth(x_position, y_positions)
                    print(f'Moved South {x_position, y_positions}')
                else:
                    # Stayed in place and looked West
                    guard_icon = '<'

        # Moving West
            elif guard_icon == '<':
                puzzle[x_position][y_positions] = '*'
                if checkWest(puzzle, x_position, y_positions) == True:
                    x_position, y_positions = moveWest(x_position, y_positions)
                    print(f'Moved West {x_position, y_positions}')
                else:
                    # Stayed in place and looked North
                    ## TODO
                    # MARK THIS POSITION AS THE START OF AN INFINITE LOOP
                    # WE CAN DETERMINE IF THE GUARD VISITS THIS EXACT SPOT AGAIN 
                    # A SET NUMBER OF TIMES,
                    # IF HE DOES, THEN WE KNOW HE IS IN AN INFINITE LOOP
                    # RETURN TRUE
                    guard_icon = '^'
    
        except IndexError:
            moving = False
            return False
    # return True


def addingObstacles(puzzle):
    '''
    //// TO DO /////
    WE CAN ALTER OUR OBSTACLES TO START ON A KNOWN USED POSITION TO SAVE TIME 
    BUT WHO CARES ABOUT OPTIMIZATION

    given a puzzle, this function adds one obstacle, '#' to the puzzle at a time in every position.
    When adding one position, check to see if our guard now enters an infinite loop
    If it does, increase a counter and move the obstacle to the next position\n
    returns a number of positions that caused the guard to enter an infinite loop    
    '''
    obstacle_counter = 0
    part_2_puzzle = puzzleRead()

    for i in range(len(part_2_puzzle)):
        for j in range(len(part_2_puzzle[i])):
            current_position = (i, j)
            if part_2_puzzle[i][j] == '.':
                # turn current position into an obstacle
                part_2_puzzle[i][j] = '#'
                print(f'Obstacle placed at position {current_position}')
                if movingPartTwo(part_2_puzzle) == True:
                    obstacle_counter += 1
                    print(f'Guard has entered an infinite loop') # currently not working
                else:
                    print(f'Guard still left building')
                    # turn obstacle back into an
                    part_2_puzzle[i][j] = '.'

part_2_puzzle = puzzleRead()

addingObstacles(part_2_puzzle)