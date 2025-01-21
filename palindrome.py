input = 'banana'

def is_palindrome(word: str) -> str:
    for i in range(len(word) // 2):
        if word[i] == word[-1 - i]:
            return "is palindrome"
        else:
            return "not palindrome"
            
    

palindrome = is_palindrome(input)
print(palindrome)

# slightly different solution

# def is_palindrome(word: str) -> bool:
#     for i in range(len(word//2)):
#         if word[i] != word[-1 -i]:
#             return False
#         else:
#             return True
        
# word = input().strip()
# palindrome = is_palindrome(word)

# if palindrome:
#     print("is palindrome")
# else:
#     print("not palindrome")