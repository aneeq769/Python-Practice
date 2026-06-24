# Practice Problem: Write a single-line list comprehension that takes a list of strings, 
# filters out strings shorter than 4 characters, and converts the remaining strings to uppercase.

# Given Input: words = ["apple", "bat", "cherry", "dog", "elderberry"]
# Expected Output: ['APPLE', 'CHERRY', 'ELDERBERRY']
words = ["apple", "bat", "cherry", "dog", "elderberry"]
a=[]
for i in words:
    if len(i) >= 4:
        print(i.upper())

