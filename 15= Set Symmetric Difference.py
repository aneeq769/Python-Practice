# Practice Problem: Given two lists of student IDs, find the IDs that appear 
# in either the first or the second list, but not in both.


# Given Input: list1 = [101, 102, 103], list2 = [103, 104, 105]

# Expected Output: {101, 102, 104, 105}
list1 = [101, 102, 103] 
list2 = [103, 104, 105]
a=set(list1)
b=set(list2)
c=a^b
print(c)

        

