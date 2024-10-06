import typing
import random

# #1
# def multiply_this(n: int) -> int:
#     mult = 1
#     for x in range(1,n+1):
#         mult = x*mult
#     return mult

# #2
# def multiply_sequence(list: [int]) -> int:
#     item = 1
#     for num in list:
#         item *= num
#     return item

# #3
# def filtered_sum(num: int, /, excluded = None) -> int:
#     if excluded is None:
#         excluded = []

#     total = 0
#     for x in range(num):
#         if x not in excluded:
#             total += x
#     return total
    
    
# #excluded = [2]    
# #print(filtered_sum(4, excluded))

# #4
# def correct_grammar(wins: int, s="s") -> None:
#     if wins > 1:
#         print(f"you have won {wins} round{s}")
#     else:
#         print("you have won 1 round.")
    
# #print(correct_grammar(1))

# #5
# def power_operator(base: str, power: int) -> str:
#     return (base)*power

# #print(power_operator("hell", 5))

# #6
# def end_banner(result: tuple):
#     print("Thanks for playing Rock Paper Scissors!")
#     w, r = result
#     if r > 0:
#         print(f">>> You won {w} rounds out of {r}. <<<")

# wr = (4, 7)

# #print(end_banner(wr))

# #7
# def reverse_in_place(list: typing.List[int]):
#     reversed_list = list[::-1]
#     return reversed_list

# #list = [1, 2, 3, 4, 5]
# #print(reverse_in_place(list))

# #8
# def produce_reverse_list(list: typing.List[int]) -> typing.List[int]:
#     n = len(list)
#     reversed_list=[]
#     for _ in  range(n):
#         n -= 1
#         reversed_list.append(list[n])
#     return(reversed_list)

# #9
# def word_count(sentence: str) -> int :
#     word_count_sentence = sentence.count(' ') + 1
#     return word_count_sentence

# sentence = input('> ')
# print(word_count(sentence))

# #10 cone volume 
# PI = 3.141592653589793
# r = int(input('radius > '))
# h = int(input('height > '))

# volume_pi: float = (PI*r**2*h)/3
# print(volume_pi)

#10 Spooky season
# number_of_os: int = int(input('How spooky are you? > '))

# if number_of_os >= 2 and number_of_os <=20:
#     print('sp'+number_of_os*'o'+'ky')

# #11 A New Hope
# N = int(input('> '))
# print('In a galaxy'+" far, "*(N-1) + 'far away...')

# #12 Next in line
# A = int(input('> '))
# B = int(input('> '))

# difference = B - A
# oldest_child = B + difference
# print(oldest_child)

#13 Celsius and Farenheit
# C = int(input('> '))

# F = C*(9/5) + 32

# print(F)

#14
# P = int(input('> '))
# B = int(input('> '))
# D = int(input('> '))

# total_earned = P//B*D + P%B
# print(total_earned)

#15
# A = int(input('> '))
# B = int(input('> '))
# C = int(input('> '))
# D = int(input('> '))
# E = int(input('> '))
# F = int(input('> '))

# Apples = A*3 + B*2 + C
# Bananas = D*3 + E*2 + F

# if Apples > Bananas:
#     print("A")
# elif Bananas > Apples:
#     print("B")
# else:
#     print("T")

#16 Telemaketers

# phone_number = (input('> '))
# if (phone_number[0] == 8 or 9) and (phone_number[3] == 8 or 9) and phone_number[1] == phone_number[2]:
#     print('ignore')
# else:
#     print('answer')

# #17 Canadian Calorie Counting

# burger = int(input('> '))
# drink = int(input('> '))
# side = int(input('> '))
# dessert = int(input('> '))

# if burger == 1:
#     burger = 461
# elif burger == 2:
#     burger = 431
# elif burger == 3:
#     burger = 420
# else:
#     burger == 0

# if drink == 1:
#     drink = 130
# elif drink == 2:
#     drink =160
# elif drink == 3:
#     drink = 118
# else:
#     drink = 0


# if side == 1:
#     side = 100
# elif side == 2:
#     side = 57
# elif side ==3:
#     side = 70
# else:
#     side = 0


# if dessert == 1:
#     dessert = 167
# elif dessert == 2:
#     dessert = 266
# elif dessert == 3:
#     dessert = 75
# else:
#     dessert = 0

# total = burger + drink + side + dessert
# print(total)

#18 Special Day

# month = int(input())
# day = int(input())

# if month == 2 and day == 18:
#     print('Special')
# elif month == 2 and day < 18 or month < 2:
#     print('Before')
# else:
#     print('After')

#19 Happy or Sad

# user_input = input('> ')
# happy = ":-)"
# sad = ":-("


# if user_input.count(happy) == user_input.count(sad):
#     print('unsure')
# if user_input.count(happy) > user_input.count(sad):
#     print('happy')
# if user_input.count(sad) > user_input.count(happy):
#     print("sad")
# if happy not in user_input and sad not in user_input:
#     print('none')

# #20 Satisfaction
# width = random.randint(1, 3)
# print(width)
# cheese = random.randint(0, 100)
# print(cheese)

# if width == 3 and cheese >= 95:
#     print('absolutely')
# elif width == 1 and cheese <= 50:
#     print('fairly')
# else:
#     print('very')

#21 Who's in the middle

# one = random.randint(1,99)
# print(one)
# two = random.randint(1,99)
# print(two)
# three = random.randint(1,99)
# print(three)


# if  two < one < three or three < one < two:
#     print(one)
# if  one < two < three or three < two < one:
#     print(two)
# if one < three < two or two < three < one:
#     print(three)

#22 Three Cups

# swaps = input()

# ball_location = 1

# for swap_type in swaps:
#     if swap_type == 'A' and ball_location == 1:
#         ball_location == 2
#     elif swap_type == 'A' and ball_location == 2:
#         ball_location == 1
#     elif swap_type == 'B' and ball_location == 2:
#         ball_location == 3
#     elif swap_type == 'B' and ball_location == 3:
#         ball_location == 2
#     elif swap_type == 'C' and ball_location == 1:
#         ball_location == 3
#     elif swap_type == 'C' and ball_location == 3:
#         ball_location == 1

# print(ball_location)

#23 Uncrackable

# password = input('> ')

# lowercase = 0
# uppercase = 0
# number = 0
# for letter in password:
#     if(letter.islower()):
#         lowercase += 1
#         print('lowercase: ' + str(lowercase))
#     elif(letter.isupper()):
#         uppercase += 1
#         print('uppercase: ' + str(uppercase))
#     elif(letter.isalnum()):
#         number += 1
#         print('number: ' + str(number))

# if  8 <= len(password) <= 12 and lowercase >= 3 and uppercase >= 2 and number >= 1:
#     print('Valid')
# else:
#     print('Invalid')

#24 HONI



def count_sequence(user_input: str) -> int:

    target_sequence = "HONI"
    sequence_index = 0
    count = 0
    for letter in user_input:

        if letter == target_sequence[sequence_index]:
            sequence_index += 1

            if sequence_index == len(target_sequence):
                count += 1
                sequence_index = 0
    
    return count
   
user_input = input('> ')
result = count_sequence(user_input)
print(result)