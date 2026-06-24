# Practice Problem: Create a function rotate_list(lst, n, direction) that shifts the 
# elements of a list by N positions. The direction can be ‘left’ or ‘right’.

# Given Input: List: [1, 2, 3, 4, 5], Shift: 2, Direction: 'right'
# Expected Output: [4, 5, 1, 2, 3]
def rotate_list(given, Shift, Direction):

    if Direction == 'right':
        return given[-Shift:] + given[:-Shift]

    elif Direction == 'left':
        return given[Shift:] + given[:Shift]


print(rotate_list([1, 2, 3, 4, 5], 2, 'right'))