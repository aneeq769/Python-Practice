# Practice Problem: Merge two dictionaries. If they share a key, the new dictionary should 
# store a list containing values from both dictionaries instead of overwriting the first one.


# Given Input: d1 = {"a": 1, "b": 2}, d2 = {"b": 3, "c": 4}
# Expected Output: {'a': [1], 'b': [2, 3], 'c': [4]}
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3={}
for key , value in d1.items():
    d3[key]=[value]
for key , value in d2.items():
    if key in d3:
        d3[key].append(value)
    else:
        d3[key]=[value]
print(d3)
