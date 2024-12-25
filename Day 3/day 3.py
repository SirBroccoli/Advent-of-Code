"""
--- Day 3: Mull It Over ---
"Our computers are having issues, so I have no idea if we have any Chief Historians in stock! 
You're welcome to check the warehouse, though," says the mildly flustered shopkeeper at the North Pole Toboggan Rental Shop. 
The Historians head out to take a look.

The shopkeeper turns to you. "Any chance you can see why our computers are having issues again?"

The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted. 
All of the instructions have been jumbled up!

It seems like the goal of the program is just to multiply some numbers. 
It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. 
For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

However, because the program's memory has been corrupted, 
there are also many invalid characters that should be ignored, 
even if they look like part of a mul instruction. 
Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

For example, consider the following section of corrupted memory:

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?
"""
with open('/home/pi/Documents/PythonFiles/Advent of Code 2024/Day 3/puzzle.txt', 'r') as f:
    file = [line.strip() for line in f] 
    puzzle = []
    for i in file:
        puzzle += i
    puzzle = ''.join(puzzle)

def mulSolution(element):
    '''
    When the string 'mul' is found
    this function will parse the elements after it
    there should be two sets of numbers separated by a comma
    enclosed in open and closed brackets with no other characters in between
    will multiply the two sets of numbers after cleaning
    
    returns product of two numbers
    else returns 0
    '''
    # identify the numbesr directly following the string 'mul'
    # I took the index of 'mul' and added 12 for the estimation of the closing bracket
    # because the rules state there can at max be two 3 digit numbers 
    numbers = puzzle[element+3:element + 12]
    # print(numbers)

    # find the index of the comma, so we can attempt to clean each element
    # maybe use the closing bracket to index from right to left
    try:
        comma_ind = numbers.index(',')
        close_bracket = numbers.index(')')

        # isolate the first set of numbers in the mul argument
        # Isolate the second set of numbers in the mul argument    
        first_numbers = int(numbers[1:comma_ind])
        second_numbers = int(numbers[comma_ind+1:close_bracket])

        # get the product by multiplying the two sets of numbers
        product = first_numbers * second_numbers

        return product
    
    except ValueError:
        # if there isn't a comma, or a closing bracket, than the argument is not usable
        return 0
    except TypeError:
        # if there are any characters in the argument, than the numbers cannot be multiplied
        return 0

total = 0

# by default mul operation are enabled at the beginning 
switch = True

for element, value in enumerate(puzzle):
    # find 3 elements that match 'mul'
    mul = puzzle[element:element + 3]
    
    # Part 2
    # Find any do and don't switches
    do = puzzle[element:element + 2]
    do_not = puzzle[element: element + 5]
    
    if do == 'do':
        switch = True
    if do_not == 'don\'t':
        switch = False
    if mul == 'mul':
        if switch == True:
            total += mulSolution(element)
print(total)
# 184576302
# 


#######################################################################
# Backup of my Part One Solution

# for element, value in enumerate(puzzle):
#     # find 3 elements that match 'mul'
#     mul = puzzle[element:element + 3]

#     if mul == 'mul':
#         # identify the numbesr directly following the string 'mul'
#         # I took the index of 'mul' and added 12 for the estimation of the closing bracket
#         # because the rules state there can at max be two 3 digit numbers 
#         numbers = puzzle[element+3:element + 12]
#         # print(numbers)

#         # find the index of the comma, so we can attempt to clean each element
#         # maybe use the closing bracket to index from right to left
#         try:
#             comma_ind = numbers.index(',')
#             close_bracket = numbers.index(')')

#             # isolate the first set of numbers in the mul argument
#             # Isolate the second set of numbers in the mul argument    
#             first_numbers = int(numbers[1:comma_ind])
#             second_numbers = int(numbers[comma_ind+1:close_bracket])

#             # get the product by multiplying the two sets of numbers
#             # add the product to get the total sum of all products
#             product = first_numbers * second_numbers
#             total += product

#             print(f'{first_numbers} * {second_numbers}: {total}')
#             # print(element, numbers, comma_ind, first_numbers, close_bracket)

#         except ValueError:
#             print(f'{element} ValueError, Something\'s Missing: Skipping {mul+numbers}')
#             pass
#         except TypeError:
#             print(f'{element} TypeError, Character mixed with the numbers: Skipping {mul+numbers}')
#             pass

