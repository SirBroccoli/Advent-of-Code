'''
"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. 
After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; 
she'd like to know if you could help her with her word search (your puzzle input). 
She only has to find one word: 

XMAS.

This word search allows words to be 

horizontal, 
vertical, 
diagonal, 
written backwards, 
or even overlapping other words. 

It's a little unusual, 
though, as you don't merely need to find one instance of XMAS - 
you need to find all of them. 
Here are a few ways XMAS might appear, 
where irrelevant characters have been replaced with .:


..X...
.SAMX.
.A..A.
XMAS.S
.X....
The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX

In this word search, XMAS occurs a total of 18 times; 
here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX

Take a look at the little Elf's word search. 
How many times does XMAS appear?
#################################
--- Part Two ---
The Elf looks quizzically at you. 
Did you misunderstand the assignment?

Looking for the instructions, 
you flip over the word search to find that this isn't actually an XMAS puzzle; 
it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. 
One way to achieve that is like this:

M.S
.A.
M.S
Irrelevant characters have again been replaced with . in the above diagram. 
Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, 
but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. 

How many times does an X-MAS appear?
'''
with open('/home/pi/Documents/PythonFiles/Advent of Code 2024/Day 4/puzzle.txt', 'r') as f:
    puzzle = [line.strip() for line in f] 
# puzzle = [[i] for i in file]
# print(puzzle)

vertical_test_down = [
    ['X', '.', '.', '.'],
    ['M', '.', '.', '.'],
    ['A', '.', '.', '.'],
    ['S', '.', '.', '.']
]
vertical_test_up = [
    ['S', '.', '.', '.'],
    ['A', '.', '.', '.'],
    ['M', '.', '.', '.'],
    ['X', '.', '.', '.']
]
horizontal_test_right = [
    ['.', '.', '.', '.'],
    ['.', '.', '.', '.'],
    ['X', 'M', 'A', 'S'],
    ['.', '.', '.', '.']
]
horizontal_test_left = [
    ['.', '.', '.', '.'],
    ['.', '.', '.', '.'],
    ['S', 'A', 'M', 'X'],
    ['.', '.', '.', '.']
]
diag_test_down_right= [
    ['X', '.', '.', '.'],
    ['.', 'M', '.', '.'],
    ['.', '.', 'A', '.'],
    ['.', '.', '.', 'S']
]
diag_test_down_left= [
    ['.', '.', '.', 'X'],
    ['.', '.', 'M', '.'],
    ['.', 'A', '.', '.'],
    ['S', '.', '.', '.']
]
diag_test_up_right = [
    ['.', '.', '.', 'S'],
    ['.', '.', 'A', '.'],
    ['.', 'M', '.', '.'],
    ['X', '.', '.', '.']
]
diag_test_up_left = [
    ['S', '.', '.', '.'],
    ['.', 'A', '.', '.'],
    ['.', '.', 'M', '.'],
    ['.', '.', '.', 'X']
]
final_test = [
    ['S', '.', '.', 'S', '.', '.', 'S'],
    ['.', 'A', '.', 'A', '.', 'A', '.'],
    ['.', '.', 'M', 'M', 'M', '.', '.'],
    ['S', 'A', 'M', 'X', 'M', 'A', 'S'],
    ['.', '.', 'M', 'M', 'M', '.', '.'],
    ['.', 'A', '.', 'A', '.', 'A', '.'],
    ['S', '.', '.', 'S', '.', '.', 'S']
]

def diagDownRight(puzzle, i, j):
    '''
    Reading Left to Right Down diagonally
    Only iterate up to the number of Rows - 3 
    Only iterate up to the number of Element - 3
    Returns True if equal to 'XMAS'
    '''
    x_row = 0
    m_row = 1
    a_row = 2
    s_row = 3
    
    x = puzzle[i+x_row][j+x_row] 
    m = puzzle[i+m_row][j+m_row]
    a = puzzle[i+a_row][j+a_row]
    s = puzzle[i+s_row][j+s_row]
    if x + m + a + s == 'XMAS':
        print('diagDownRight is True')
        return True
def diagDownLeft(puzzle, i, j):
    '''
    Reading Left to Right Down diagonally Left
    Starts at the 3rd element and iterates Down Left One value each Letter
    Returns True if equal to 'XMAS'
    '''
    x_row = 0
    m_row = 1
    a_row = 2
    s_row = 3
    
    x = puzzle[i+x_row][j+x_row]
    m = puzzle[i+m_row][j-m_row]
    a = puzzle[i+a_row][j-a_row]
    s = puzzle[i+s_row][j-s_row]
    # print(x, m, a, s)
    if x+m+a+s == 'XMAS':
        print('diagDownLeft is True')
        return True
def diagUpRight(puzzle, i, j):
    '''
    Reading Left to Right, Iterating Up and Right one Value per character
    We use a value of 3 in the range functions because we are reducing the elements 
    of a list by how many letters there are in the word we are trying to find by 
    starting on the 'X'.  IE, "XMAS"
    Returns True if equal to 'XMAS'
    '''
    x_row = 0
    m_row = 1
    a_row = 2
    s_row = 3

    x = puzzle[i+x_row][j+x_row]
    m = puzzle[i-m_row][j+m_row]
    a = puzzle[i-a_row][j+a_row]
    s = puzzle[i-s_row][j+s_row]
    # print(x, m, a, s)
    if x+m+a+s == 'XMAS':
        print('diagUpRight is True')
        return True
def diagUpLeft(puzzle, i, j):
    '''
    Reading Left to Right, Iterating Up and Left one Value per character
    We use a value of 3 in the range functions because we are reducing the elements 
    of a list by how many letters there are in the word we are trying to find by 
    starting on the 'X'.  IE, "XMAS"
    Returns True if equal to 'XMAS'
    '''
    x_row = 0
    m_row = 1
    a_row = 2
    s_row = 3
    
    # Iterate each Row up to the last 3rd element to avoid Out of bounds
    x = puzzle[i+x_row][j+x_row]
    m = puzzle[i-m_row][j-m_row]
    a = puzzle[i-a_row][j-a_row]
    s = puzzle[i-s_row][j-s_row]
    if x+m+a+s == 'XMAS':
        print(f'diagUpLeft is True')
        return True
def verticalUp(puzzle, i, j):
    '''
    Reading Left to Right, Iterating Straight up Vertically through rows
    We use a value of 3 in the range functions because we are reducing the elements 
    of a list by how many letters there are in the word we are trying to find by 
    starting on the 'X'.  IE, "XMAS"
    Returns True if equal to 'XMAS'
    '''
    x_row = 0
    m_row = 1
    a_row = 2
    s_row = 3
    

    x = puzzle[i+x_row][j]
    m = puzzle[i-m_row][j]
    a = puzzle[i-a_row][j]
    s = puzzle[i-s_row][j]
    # print(x, m, a, s)
    if x+m+a+s == 'XMAS':
        print('verticalUp is True')
        return True
def virticalDown(puzzle, i, j):
    '''
    Reading Left to Right, Iterating Straight down Vertically through rows
    We use a value of 3 in the range functions because we are reducing the elements 
    of a list by how many letters there are in the word we are trying to find by 
    starting on the 'X'.  IE, "XMAS"
    Returns True if equal to 'XMAS'
    '''
    x_row = 0
    m_row = 1
    a_row = 2
    s_row = 3

    x = puzzle[i+x_row][j]
    m = puzzle[i+m_row][j]
    a = puzzle[i+a_row][j]
    s = puzzle[i+s_row][j]
    # print(x, m, a, s)
    if x+m+a+s == 'XMAS':
        print('verticalDown is True')
        return True
def horizontalRight(puzzle, i, j):
    '''
    Reading Left to Right, Iterating Straight across horizontally through the row
    We use a value of 3 in the range functions because we are reducing the elements 
    of a list by how many letters there are in the word we are trying to find by 
    starting on the 'X'.  IE, "XMAS"
    Returns True if equal to 'XMAS'
    '''
    x_row = 0
    m_row = 1
    a_row = 2
    s_row = 3

    x = puzzle[i][j+x_row]
    m = puzzle[i][j+m_row]
    a = puzzle[i][j+a_row]
    s = puzzle[i][j+s_row]
    # print(x, m, a, s)
    if x+m+a+s == 'XMAS':
        print('horizontalRight is True')
        return True
def horizontalLeft(puzzle, i, j):
    '''
    Reading Left to Right, Iterating Straight across horizontally through the row
    We use a value of 3 in the range functions because we are reducing the elements 
    of a list by how many letters there are in the word we are trying to find by 
    starting on the 'X'.  IE, "XMAS"
    Returns True if equal to 'XMAS'
    '''
    x_row = 0
    m_row = 1
    a_row = 2
    s_row = 3

    x = puzzle[i][j-x_row]
    m = puzzle[i][j-m_row]
    a = puzzle[i][j-a_row]
    s = puzzle[i][j-s_row]
    # print(x, m, a, s)
    if x+m+a+s == 'XMAS':
        print('horizontalLeft is True')
        return True

def xMascrosses(puzzle):
    '''
    iterate over ever element looking for the letter 'A',
    if 'A', then chech diagonally from the center both ways, forward and backward.
    returns a Number of Diagonal crosses that == 'MAS'
    '''
    num_of_crosses = 0
    
    for i in range(1, len(puzzle)-1):
        for j in range(1, len(puzzle[i])-1):
            A = puzzle[i][j]
            up_left = puzzle[i-1][j-1]
            up_right = puzzle[i-1][j+1]
            down_left = puzzle[i+1][j-1]
            down_right = puzzle[i+1][j+1]

            top_down_cross = up_left + A + down_right
            bottom_up_cross = down_left + A + up_right

            if top_down_cross == 'MAS' or top_down_cross[::-1] == 'MAS':
                if bottom_up_cross == 'MAS' or bottom_up_cross[::-1] == 'MAS':
                    num_of_crosses += 1
            
    return num_of_crosses
def XMAS(puzzle):
    
    num_of_XMAS = 0
    
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
        
            if i >= 3:
                num_of_XMAS += 1 if verticalUp(puzzle, i, j) else 0
                
            if i < len(puzzle[i])-3:
                num_of_XMAS += 1 if virticalDown(puzzle, i, j) else 0

            if i >= 3 and j >= 3:
                num_of_XMAS += 1 if diagUpLeft(puzzle, i, j) else 0
                
            if i >= 3 and j < len(puzzle[i])-3:
                num_of_XMAS += 1 if diagUpRight(puzzle, i, j) else 0
                
            if i < len(puzzle[i])-3 and j >= 3:
                num_of_XMAS += 1 if diagDownLeft(puzzle, i, j) else 0
                
            if i < len(puzzle[i]) -3 and j < len(puzzle[i]) - 3:
                num_of_XMAS += 1 if diagDownRight(puzzle, i, j) else 0
                
            if j < len(puzzle[i])-3:
                num_of_XMAS += 1 if horizontalRight(puzzle, i, j) else 0
                
            if j >= 3:
                num_of_XMAS += 1 if horizontalLeft(puzzle, i, j) else 0

    return num_of_XMAS
######
# part 1 == 2514

print(xMascrosses(puzzle))        


        



