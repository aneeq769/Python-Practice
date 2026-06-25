# Practice Problem: Write a script that takes two lists of integers from a user, 
# converts them to sets, and determines if the first set is a Subset, a Superset, or Disjoint from the second.

# Given Input: Set A: {1, 2, 3}, Set B: {1, 2, 3, 4, 5}

# Expected Output: Set A is a subset of Set B.
A= {1, 2, 3}
B= {1, 2, 3, 4, 5}
if A.issubset(B):
    print('Set A is a subset of Set B')
elif A.issuperset(B):
    print('Set A is a superset of Set B')
elif A.isdisjoint(B):
    print('Set A is a disjoint of Set B')
else:
    print(f"The sets share these elements: {A & B}")