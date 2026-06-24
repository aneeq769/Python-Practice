# Practice Problem: Write a function to check if a full sentence is a palindrome. 
# You must ignore case, spaces, and all punctuation marks.


# Given Input: "A man, a plan, a canal: Panama"

# Expected Output: True
given= "A man, a plan, a canal: Panama"
a=''
for i in given:
    if i.isalnum():  
        a+=i.lower()
if a==a[::-1]:
    print(True)
else:
    print(False)

    
    

