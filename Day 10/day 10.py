'''
--- Day 10: Hoof It ---
You all arrive at a Lava Production Facility on a 
floating island in the sky. As the others begin to 
search the massive industrial complex, you feel a 
small nose boop your leg and look down to discover 
a reindeer wearing a hard hat.

The reindeer is holding a book titled "Lava Island 
Hiking Guide". However, when you open the book, you 
discover that most of it seems to have been scorched
 by lava! As you're about to ask how you can help, 
 the reindeer brings you a blank topographic map of 
 the surrounding area (your puzzle input) and looks 
 up at you excitedly.

Perhaps you can help fill in the missing hiking trails?

The topographic map indicates the height at each 
position using a scale from 0 (lowest) to 9 (highest).
 For example:

0123
1234
8765
9876
Based on un-scorched scraps of the book, you determine 
that a good hiking trail is as long as possible and has
an even, gradual, uphill slope. For all practical purposes,
this means that a hiking trail is any path that starts 
at height 0, ends at height 9, and always increases by 
a height of exactly 1 at each step. Hiking trails never
steps - only up, down, left, or right 
from the perspective of the map).

You look up from the map and notice that the reindeer 
has helpfully begun to construct a small pile of pencils, 
markers, rulers, compasses, stickers, and other equipment 
you might need to update the map with hiking trails.

A trailhead is any position that starts one or more hiking 
trails - here, these positions will always have height 0. 
Assembling more fragments of pages, you establish that a trailhead's 
score is the number of 9-height positions reachable from that trailhead 
via a hiking trail. In the above example, the single trailhead 
in the top left corner has a score of 1 because it can reach a 
single 9 (the one in the bottom left).

This trailhead has a score of 2:

...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9
(The positions marked . are impassable tiles to simplify 
these examples; they do not appear on your actual topographic map.)

This trailhead has a score of 4 because every 9 is reachable 
via a hiking trail except the one immediately to the left of 
the trailhead:

..90..9
...1.98
...2..7
6543456
765.987
876....
987....
This topographic map contains two trailheads; the trailhead 
at the top has a score of 1, while the trailhead at the bottom 
has a score of 2:

10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01
Here's a larger example:

89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
This larger example has 9 trailheads. Considering the trailheads 
in reading order, they have scores of 5, 6, 5, 3, 1, 3, 5, 3, and 5. 
Adding these scores together, the sum of the scores of all trailheads is 36.

The reindeer gleefully carries over a protractor and adds it to the pile. 
What is the sum of the scores of all trailheads on your topographic map?
'''


def puzzleReader():
    with open('/home/pi/Documents/PythonFiles/Advent of Code/2024/Day 10/puzzle.txt', 'r') as f:
        puzzle = [line.strip() for line in f.readlines()]
    return puzzle

def checkingTheTrail(x, y, puzzle, peak_locations, start_of_trail):
    '''
    this is the recursive function that will check north, south, east, and west
    if it identifies a value that is one greater than its current value,
    it will call this function again and check that new position for the next greatest value
    the puzzle text file is a 42 by 42 grid of numbers
    x and y cannot be lower than 0 and greater than 41\n
    x Int\n
    y Int\n
    puzzle = list\n
    peak_locations list of list\n

    //Is a recursive function supposed to return anythin???
    // Do i need to add the puzzle text file as an argument if it will be inside of the walkingTheTrail function???
    '''
    
    current_position = int(puzzle[x][y])
    curr_coordinates = (int(x), int(y))
    print(f'position {x, y} {current_position}')

    if current_position == 9: 
        print('Current position is a 9')
        
        # from the trail head (0), has this peak been visited before?
        if start_of_trail not in peak_locations:
            print('initializing peak_locations for start_of_trail')
            peak_locations[start_of_trail] = []
       
        # a trail head (0) can visit a peak (curr_coordinates) many times, but only be considered one trail
        # have we visited this peak from the trail head before?
        # if not, add the peak value to the trail head Key
        if curr_coordinates not in peak_locations[start_of_trail]:
            print('adding position to peak_locations')
            peak_locations[start_of_trail].append(curr_coordinates)

    # is north one value greater than our current position?
    if x > 0 and int(puzzle[x-1][y]) == int(current_position) + 1:
        print('checking the north position')
        checkingTheTrail(x - 1, y, puzzle, peak_locations, start_of_trail)
    
    # is East one value greater than our current position?
    if y < len(puzzle)-1 and int(puzzle[x][y+1]) == int(current_position) + 1:
        print('checking the east position')
        checkingTheTrail(x, y+1, puzzle, peak_locations, start_of_trail)

    # is South one value greater than our current position?
    if x < len(puzzle)-1 and int(puzzle[x+1][y]) == int(current_position) + 1:
        print('checking the South position')
        checkingTheTrail(x + 1, y, puzzle, peak_locations, start_of_trail)
    
    # is West one value greater than our current position?  
    if y > 0 and int(puzzle[x][y-1]) == int(current_position) + 1:
        print('moving the west position')
        checkingTheTrail(x, y-1, puzzle, peak_locations, start_of_trail)
    
def walkingTheTrail(puzzle):
    '''
    iterates over the puzzle file,
    Identifying any zero values as the start of the trailhead
    It will call checkinTheTrail function through recursion to identify connecting values that will
    lead to a 9 value through every iteration
    '''
    peak_locations = {} # identify the top of the trailheads in x, y format

    # iterate over the x axis
    for path_x in range(len(puzzle)):
        # print(path_x)
        # iteratign over the y axis
        for path_y in range(len(puzzle)):
            position = puzzle[path_x][path_y]
            base_head_coordinates = (path_x, path_y)
            if puzzle[path_x][path_y] == '0':
                checkingTheTrail(path_x, path_y, puzzle, peak_locations, base_head_coordinates)

    print(peak_locations)
    return peak_locations



puzzle = puzzleReader()

trailheads = walkingTheTrail(puzzle)

trail_score = sum(len(i) for i in trailheads.values())

print(trail_score)