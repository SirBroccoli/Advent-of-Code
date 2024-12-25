"""
--- Day 2: Red-Nosed Reports ---
Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, 
the engineers there run up to you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. 
You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. 
You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many reports, one report per line. 
Each report is a list of file called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. 
The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. 
So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?
ANSWER 287
"""
# # get the contents of the puzzle
# with open('/home/pi/Documents/PythonFiles/Advent of Code 2024/Day 2/puzzle.txt', 'r') as f:
#     file = [line.strip() for line in f]

# # We will call two functions for every row in the puzzle
# # the first function will test if every number decreases from the first
# def decreases(puzzle):
#     '''
#     taks first element and compares the following elements
#     each iteration should be smaller than, and not equal to
#     returns True or False
#     '''
#     puzzle = puzzle.split()
#     length_of_argument = len(puzzle)

#     for i in range(0, length_of_argument-1):
#         anum = int(puzzle[i])
#         bnum = int(puzzle[i+1])
#         difference = abs(anum-bnum)
        
#         if anum < bnum:
#             return False
#         elif difference > 3 or difference == 0:
#             return False
               
#     return True

# # this function will test if every num after the first only increases
# def increases(puzzle):
#     '''
#     taks first element and compares the following elements
#     each iteration should be greater than, and not equal to
#     returns True or False
#     '''
#     puzzle = puzzle.split()
#     length_of_argument = len(puzzle)

#     for i in range(0, length_of_argument-1):
#         anum = int(puzzle[i])
#         bnum = int(puzzle[i+1])
#         difference = abs(anum-bnum)
        
#         if anum > bnum:
#             return False
#         elif difference > 3 or difference == 0:
#             return False
               
#     return True

# def problemDampener(i, puzzle):
#     '''
#     Brute force removing a problem element in a list
#     takes the previous iteration and removes the element and 
#     reiterates over the list a second time to determine if the 
#     levels are safe as the previous function
#     returns True or False

#     once you identify the failure,
#     iterate over each element but...
#     use splicing to remove one particular element
#     Look to see if the iteration turns true because 
#     '''
    


# # the number of safe reports for each row of the puzzle
# safe = 0
# notsafe = 0

# for row in range(0, len(file)):
#     workingrow = file[row]
#     rowdecreases = decreases(file[row])
#     rowincrease = increases(file[row])

#     if rowincrease:
#         print(f'increases {workingrow}')
#         safe += 1
#     elif rowdecreases:
#         print(f'decreases {workingrow}')
#         safe += 1 
#     else:
#         print(f'neither increases or decreases {workingrow}')
#         notsafe += 1

# print(safe, notsafe)

def is_valid_sequence(file):

    increasing = True
    decreasing = True

    for i in range(len(file) - 1):
        difference = file[i + 1] - file[i]

        if difference == 0 or abs(difference) > 3:
            return False  # Difference is either 0 or greater than 3

        if difference < 0:
            increasing = False  # Not increasing
        elif difference > 0:
            decreasing = False  # Not decreasing

    return increasing or decreasing

def count_valid_rows(file_path):
    valid_rows = 0

    with open(file_path, 'r') as f:
        for line in f:
            number = list(map(int, line.strip().split()))
            if is_valid_sequence(number):
                valid_rows += 1

    return valid_rows

# Example usage
file_path = '/home/pi/Documents/PythonFiles/Advent of Code 2024/Day 2/puzzle.txt'
valid_rows_count = count_valid_rows(file_path)
print(f'Number of valid rows: {valid_rows_count}')
