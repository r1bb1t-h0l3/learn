# 1. Reverse a String

# Write a function that takes a string as input and returns the string reversed.

# Example Input: "hello"
# Example Output: "olleh"

##slicing method, written in C under the hood, time complexity O(n), as the string is traversed once to create reversed copy
##space complexity O(n) as new string is created to store reversed version
# usr_inpt = input("> ")
# output = usr_inpt[::-1]
# print(output)

##using a for loop
## time complexity O(n2) because str is immutable and new striing is created ech time
## spece compexity O(n)

# inpt = input("> ")
# inpt_reversed = ""

# for char in inpt:
#     inpt_reversed = char + inpt_reversed

# print(inpt_reversed)

## using reversed function
## time complexity O(n) as it iterates over string once to create new string
## space complexity O(1) for the new string - as efficient as slicing for most cases

# inpt = input("> ")

# output = "".join(reversed(inpt))
# print(output)

## using a list and join
## time/space complexity O(n), more verbode and less efficient than slicing
# inpt = input("> ")
# output = "".join([inpt[i] for i in range(len(inpt) - 1, -1, -1)])
# print(output)

##using recursion
# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     return s[-1] + reverse_string(s[:-1])

# usr_inpt = input("> ")
# output = reverse_string(usr_inpt)
# print(output)

# 2. Check for Palindrome

# Write a function that checks if a given string is a palindrome. A palindrome reads the same backward as forward.
## using slicing time/space complexity O(n)
# inpt = input('> ')

# inpt_reversed = inpt[::-1]

# if inpt == inpt_reversed:
#     print("palindrome")
# else:
#     print("not palindrome")

## using pointers 
# optimised space complexity O(1)

# def is_palindrome(s: str) -> bool:
#     left, right = 0, len(s) - 1

#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# inpt = input("> ")
# if is_palindrome(inpt):
#     print("palindrome")
# else:
#     print("not palindrome")

# Example Input: "racecar"
# Example Output: True

# 3. FizzBuzz

# Print the numbers from 1 to 100. For multiples of 3, print "Fizz". For multiples of 5, print "Buzz". For multiples of both 3 and 5, print "FizzBuzz".

# 4. Find the Largest Number in a List

# Write a function that takes a list of numbers and returns the largest number.

# Example Input: [1, 2, 3, 4, 5]
# Example Output: 5

# 5. Count Vowels in a String

# Write a function that counts the number of vowels in a given string.

# Example Input: "hello world"
# Example Output: 3

# 6. Remove Duplicates from a List

# Write a function that removes duplicate elements from a list and returns a new list with unique elements.

# Example Input: [1, 2, 2, 3, 4, 4, 5]
# Example Output: [1, 2, 3, 4, 5]

# 7. Merge Two Sorted Arrays

# Write a function that merges two sorted arrays into one sorted array.

# Example Input: [1, 3, 5] and [2, 4, 6]
# Example Output: [1, 2, 3, 4, 5, 6]

# 8. Find the First Non-Repeating Character

# Write a function that takes a string and returns the first character that does not repeat.

# Example Input: "swiss"
# Example Output: "w"

# 9. Generate Fibonacci Sequence

# Write a function that generates the first n numbers in the Fibonacci sequence.

# Example Input: 5
# Example Output: [0, 1, 1, 2, 3]

# 10. Find the Missing Number

# You are given an array of integers from 1 to n, with one number missing. Write a function to find the missing number.

# Example Input: [1, 2, 4, 5] (n=5)
# Example Output: 3

# Bonus: What to Practice

#  • Practice edge cases (e.g., empty inputs, very large inputs).
#  • Optimize for time and space complexity.
#  • Be prepared to explain your thought process step-by-step.