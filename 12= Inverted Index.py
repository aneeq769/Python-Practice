# Practice Problem: Create a function that “inverts” a dictionary. 
# Convert a dictionary of Author: [List of Books] into a dictionary of Book: Author.


# Given Input:

# {"Orwell": ["1984", "Animal Farm"], "Huxley": ["Brave New World"]}

# Expected Output:
# {'1984': 'Orwell', 'Animal Farm': 'Orwell', 'Brave New World': 'Huxley'}
given={"Orwell": ["1984", "Animal Farm"], "Huxley": ["Brave New World"]}
result={}
for key, value in given.items():
    for val in value:
        result[val]=key
print(result)
    