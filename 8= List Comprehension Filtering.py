# Practice Problem: Given a list of strings, use a single list comprehension to extract strings that 
# meet two criteria: they must be longer than 5 characters AND they must start with a vowel (a, e, i, o, u).

# Given Input: ["apple", "education", "ice", "ocean", "python", "umbrella"]
# Expected Output: ['education', 'umbrella']
given= ["apple", "education", "ice", "ocean", "python", "umbrella"]
vowel='aeiou'
a=[]
for i in given:
    if len(i)>5 and i[0] in vowel:
        a.append(i)
print(a)