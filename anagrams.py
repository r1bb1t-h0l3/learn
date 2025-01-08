# PROBLEM 1
# Write a program to check whether the two given strings are anagrams.


# Two strings are said to be anagrams if the two strings contain the same set of characters, but the order can be different.


# For example: "coding" and "dincog" are anagrams. "ninjas" and "jasnni" are anagrams. 

# My initial solution
# usr_inpt = input("> ").split(" ")

# def is_anagram(usr_inpt):
#     w1, w2 = usr_inpt[0], usr_inpt[1]

#     if sorted(w1) == sorted(w2):
#         return "anagram"
#     else:
#         return "not anagram"

# anagram = is_anagram(usr_inpt)
# print(anagram)

# cons - uses sortiing which hass a time complexity of nlogn

# Version with counter for faster performance O(n)
# from collections import Counter

# usr_input = input("> ").split(" ")

# def is_anagram(usr_inpt):
#     w1, w2 = usr_inpt[0], usr_inpt[1]
#     if Counter(w1) == Counter(w2):
#         return "anagram"
#     else:
#         return "not anagram"
# anagram = is_anagram(usr_input)
# print(anagram)

#Edge cases such as case sensitivity considered

from collections import Counter

def is_anagram(w1, w2):
    # Normalise input (case insensitive, ignore spaces)
    w1, w2 = w1.lower().replace(" ", ""), w2.lower().replace(" ","")
    return "anagram" if Counter (w1) == Counter(w2) else "not anagram"

# Input 
usr_inpt = input("> ").split(" ")
print(is_anagram(usr_inpt[0], usr_inpt[1]))