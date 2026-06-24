# Practice Problem: Given a sentence, reverse each individual word within the string 
# while maintaining the original word order.


# Given Input: "Python is awesome"

# Expected Output: "nohtyP si emosewa"
given= "Python is awesome"
a=given.split()
for i in a:
    print(i[::-1],end=" ")