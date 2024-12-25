'''
--- Day 5: Print Queue ---
Satisfied with their search on Ceres, 
the squadron of scholars suggests subsequently scanning the stationery stacks of sub-basement 17.

The North Pole printing department is busier than ever this close to Christmas, 
and while The Historians continue their search of this historically significant facility, 
an Elf operating a very familiar printer beckons you over.

The Elf must recognize you, 
because they waste no time explaining that the new sleigh launch safety manual updates won't print correctly. 
Failure to update the safety manuals would be dire indeed, so you offer your services.

Safety protocols clearly indicate that new pages for the safety manuals must be printed in a very specific order. 
The notation X|Y means that if both page number X and page number Y are to be produced as part of an update, 
page number X must be printed at some point before page number Y.

The Elf has for you both the page ordering rules and the pages to produce in each update (your puzzle input), 
but can't figure out whether each update has the pages in the right order.

For example:

47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
The first section specifies the page ordering rules, 
one per line. The first rule, 47|53, means that if an update includes both page number 47 and page number 53, 
then page number 47 must be printed at some point before page number 53. 
(47 doesn't necessarily need to be immediately before 53; 
other pages are allowed to be between them.)

The second section specifies the page numbers of each update. 
Because most safety manuals are different, 
the pages needed in the updates are different too. 
The first update, 75,47,61,53,29, 
means that the update consists of page numbers 75, 47, 61, 53, and 29.

To get the printers going as soon as possible, 
start by identifying which updates are already in the right order.

In the above example, the first update (75,47,61,53,29) is in the right order:

75 is correctly first because there are rules that put each other page after it: 75|47, 75|61, 75|53, and 75|29.
47 is correctly second because 75 must be before it (75|47) and every other page must be after it according to 47|61, 47|53, and 47|29.
61 is correctly in the middle because 75 and 47 are before it (75|61 and 47|61) and 53 and 29 are after it (61|53 and 61|29).
53 is correctly fourth because it is before page number 29 (53|29).
29 is the only page left and so is correctly last.
Because the first update does not include some page numbers, the ordering rules involving those missing page numbers are ignored.

The second and third updates are also in the correct order according to the rules. 
Like the first update, they also do not include every page number, 
and so only some of the ordering rules apply - within each update, 
the ordering rules that involve missing page numbers are not used.

The fourth update, 75,97,47,61,53, is not in the correct order: 
it would print 75 before 97, which violates the rule 97|75.

The fifth update, 61,13,29, is also not in the correct order, 
since it breaks the rule 29|13.

The last update, 97,13,75,29,47, is not in the correct order due to breaking several rules.

For some reason, the Elves also need to know the middle page number of each update being printed. 
Because you are currently only printing the correctly-ordered updates, you will need to find the middle page number of each correctly-ordered update. In the above example, the correctly-ordered updates are:

75,47,61,53,29
97,61,53,29,13
75,29,13
These have middle page numbers of 61, 53, and 29 respectively. 
Adding these page numbers together gives 143.

Of course, you'll need to be careful: 
the actual list of page ordering rules is bigger and more complicated than the above example.

Determine which updates are already in the correct order. 

What do you get if you add up the middle page number from those correctly-ordered updates?
'''

def puzzleRead():
    '''
    returns a list of the puzzle text file containing
    rules and the pages of the manual separated by an empty list
    '''
    with open('/home/pi/Documents/PythonFiles/Advent of Code/2024/Day 5/puzzle.txt', 'r') as f:
        puzzle = [line.strip() for line in f] 
        return puzzle

def manualRules(puzzle):
    '''
    Identifies all of the rules each manual has to follow 
    determining the page order from the given puzzle
    returns a dictionary containing the rules as key, and value as the page numbers
    '''
    rules = {}
    for line in puzzle:
        if '|' in line:
            rule = line.split('|')
            if rule[0] not in  rules:
                rules[rule[0]] = [rule[1]]
            else:
                rules[rule[0]].append(rule[1])
    return rules

def manualPages(puzzle):
    '''
    Returns a sorted list of all of the pages that need to be printed
    '''
    pages = []
    for line in puzzle:
        if not '|' in line and line != '':
            pages.append(line)
    pages.sort()
    return pages

def rulesCheck(rules, updates):
    '''
    in a reversed iteration, If a previous iteration occurs in the current elements Dict Value, than return False
    '''
    # Start by iterating in reverse of the current Order
    for i in range(len(updates)-1, 0, -1):
        # Our current iteration has dict values that represent numbers that should be after our current iteration
        current_iteration_dictvalues = rules.get(updates[i])
        for j in range(0, i):
            # if a value from the beginning of the list is in the current iteration dict values, return False
            if updates[j] in current_iteration_dictvalues:
                return False
    return True

def medianSum(lists):
    '''
    returns the sum of the median of the lists
    '''
    sum = 0
    for i in lists:
        sum += int(i[len(i) // 2])
    return sum

def main(rules, pages):
    '''
    Checks the rules to see if the pages are in the correct order
    returns a list of all updates that are already in the correct order
    Returns list
    '''
    correct_order = []
    incorrect_order = []
    # get each update, the range of pages to be checked
    # use split to separate the pages from the comma
    for updates in pages:
        updates = updates.split(',')
        # print(f'main function {updates}')
        if rulesCheck(rules, updates):
            correct_order.append(updates)
        else:
            incorrect_order.append(updates)
    # print(f'Correct order of updates is {correct_order}')
    return correct_order, incorrect_order

def mainIncorrectCorrecter(incorrect_list):
    '''
    Takes the incorrect pages and attempts to correct them
    all updates should have a correct answer
    returns a List of the corrected updates
    '''
    corrected_updates = []
    for updates in incorrect_list:
        print(updates)
        correct = False
        while not correct:
            try:
                for i in range(len(updates)-1, 0, -1):
                    current_iteration_dictvalues = rules.get(updates[i])
                    for j in range(0, i):
                        if updates[j] in current_iteration_dictvalues:
                            bad_index = updates.pop(j)
                            updates.insert(i, bad_index)
                            raise ValueError(f'indexes altered. Restarting')
                if rulesCheck(rules, updates):
                    corrected_updates.append(updates)
                    correct = True
            except ValueError:
                continue
    return corrected_updates

# Main ########################
#read the puzzle text file
puzzle = puzzleRead()
# print(puzzle)

# get the rules from the puzzle
rules = manualRules(puzzle)
# print(rules)

# get the pages from the puzzle
pages = manualPages(puzzle)
# print(pages)

# rulesCheck(rules, pages)
correct_pages, incorrect_pages = main(rules, pages)
# print(correct_pages)
# print(incorrect_pages)

total = medianSum(correct_pages) # 4578
# print(total)

'''
--- Part Two ---
While the Elves get to work printing the correctly-ordered updates, 
you have a little time to fix the rest of them.

For each of the incorrectly-ordered updates, 
use the page ordering rules to put the page numbers in the right order. 
For the above example, here are the three incorrectly-ordered updates and their correct orderings:

75,97,47,61,53 becomes 97,75,47,61,53.
61,13,29 becomes 61,29,13.
97,13,75,29,47 becomes 97,75,47,29,13.
After taking only the incorrectly-ordered updates and ordering them correctly, 
their middle page numbers are 47, 29, and 47. Adding these together produces 123.

Find the updates which are not in the correct order. 
What do you get if you add up the middle page numbers after correctly ordering just those updates?
'''
correct_lists = mainIncorrectCorrecter(incorrect_pages)
# print(correct_lists)
total = medianSum(correct_lists)
# print(total)