# Practice Problem: Create a function that takes a string and returns a count of how many times 
# each character appears. Ignore spaces and make it case-insensitive.


# Given Input: text = "Python Programming"

# Expected Output:
# Character Frequency: 
# Counter({'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, 'r': 2, 'a': 1, 'g': 2, 'm': 2, 'i': 1})
text = "Python Programming"
a=text.lower()
result={}
for i in a:
    if i in result:
        result[i]+=1
    else:
        result[i]=1
print(result)