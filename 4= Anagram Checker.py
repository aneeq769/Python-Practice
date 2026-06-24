# Practice Problem: Write a function that determines if two strings are anagrams 
# (contain the exact same characters in a different order).


# Given Input: word1 = "listen", word2 = "silent"

# Expected Output: Is "listen" an anagram of "silent"? True
word1 = "listen"
word2 = "silent"
w1=sorted(word1)
w2=sorted(word2)
if w1==w2:
    print(f'Is {word1} an anagram of {word2}? {True}')
else: 
    print(f'{False}')