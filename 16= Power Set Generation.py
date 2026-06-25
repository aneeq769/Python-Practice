# Practice Problem: Write a function that generates the Power Set of a given 
# set (a set of all possible subsets, including the empty set and the set itself).

# Given Input: [1, 2, 3]

# Expected Output:
# [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
from itertools import combinations

given = [1, 2, 3]

result = []

for i in range(len(given) + 1):
    result.extend(combinations(given, i))

print(result)
