# Practice Problem: Write a function that removes duplicate elements from a list. 
# You cannot use set() because sets do not maintain the original order of elements.

# Given Input: [1, 2, 2, 3, 1, 4, 2]
# Expected Output: [1, 2, 3, 4]
given=[1, 2, 2, 3, 1, 4, 2]
a=[]
for i in given:
    if i not in a:
        a.append(i)
    
print(a)