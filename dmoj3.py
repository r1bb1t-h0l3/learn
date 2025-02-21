# -------------------------------------------
# 101. DMOJ problem bfs17p1, Back From Summer '17 P1: Pithy Pastimes

# n = int(input())

# hobbies = list(map(str, input().split()))

# counter = 0
# for hobby in hobbies:
#     if len(hobby) <= 10:
#         counter += 1

# print(counter)

# -------------------------------------------
# 101. DMOJ problem bfs19p1, Back From Summer '19 P1: Winnie's Orphans

# data = list(map(int, input().split()))

# orphanages, children = data[0], data[1]
# best_orphanage = -1

# min_count = float('inf')
# for orphanage_index in range(1, orphanages + 1):
#     cuteness_scores = list(map(int, input().split()))
#     count = sum(1 for score in cuteness_scores if score == 1 or score == 10)

#     if count < min_count:
#         min_count = count
#         best_orphanage = orphanage_index


# print(best_orphanage)

# -------------------------------------------
# 102. DMOJ problem blockgame, A Block Game

# n, k, d = list(map(int, input().split()))

# j = float(input())

# total_kills = k
# total_deaths = d


# for _ in range(n):
#     ki, di = map(int, input().split())
#     total_kills += ki
#     total_deaths += di

# if total_deaths == 0:
#     print('stop hacking!')
# else:
#     final_ratio = total_kills / total_deaths
#     if final_ratio > j:
#         print('Y')
#     else:
#         print('N')

# -------------------------------------------
# 103. DMOJ problem boolean, Boolean

# n = list(map(str, input().split()))

# not_count = n.count('not')

# if not_count % 2 == 0:
#     print(n[-1])
# else:
#     if n[-1] == "True":
#         print("False")
#     else:
#         print("True")

# -------------------------------------------
# 104. DMOJ problem bpc1j1, Facial Recognition

# n = int(input())

# faces = 0
# for _ in range(n):
#     inpt = input()
#     if inpt == "face":
#         faces += 1

# print(faces)

# -------------------------------------------
# 105. DMOJ problem bpc1j2, BPC 1 J2 - Cake
# gcd - greatest common denominator

# def compute_gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# n = int(input())
# a = list(map(int, input().split()))

# gcd_all = a[0]
# for num in a[1:]:
#     gcd_all = compute_gcd(gcd_all, num)
#     if gcd_all == 1:
#         break

# scaled_a = [x // gcd_all for x in a]

# print(" ".join(map(str, scaled_a)))

# -------------------------------------------
# 106. DMOJ problem bsspc21j1, BSSPC '21 J1 - Eggy's New Clothes
#  ( ( s + 2 ) × 3 ) + 16 

# s = int(input())
# x = int(input())

# eggy_size = (( s + 2) * 3) + 16
# if x >= eggy_size:
#     print("Yes it fits!")
# else:
#     print("No, it's too small :(")

# -------------------------------------------
# 106. DMOJ problem bsspc21j2, BSSPC '21 J2 - James and Youtube

# def range_overlap(class_range, youtube_range):
#     class_start, class_end = class_range
#     youtube_start, youtube_end = youtube_range
#     return max(class_start, youtube_start) <= min(class_end, youtube_end)

# number_of_classes = int(input())

# classes = []
# for _ in range(number_of_classes):
#     class_interval = tuple(map(int, input().split()))
#     classes.append(class_interval)

# nuumber_of_youtube_sessions = int(input())

# youtube_sessions = []
# for _ in range(nuumber_of_youtube_sessions):
#     youtube_interval = tuple(map(int, input().split()))
#     youtube_sessions.append(youtube_interval)

# results = []
# for youtube_session in youtube_sessions:
#     overlap = False
#     for class_interval in classes:
#         if range_overlap(class_interval, youtube_session):
#             overlap = True
#             break
#     if overlap:
#         results.append("Break is Over! Stop playing games! Stop watching Youtube!")
#     else:
#         results.append(":eyy:")

# for result in results:
#     print(result)

# -------------------------------------------
# 107. DMOJ problem bsspc22c1p1, BSSPC '22 P1 - Bubble Tea Tracker

# n = int(input())

# totals = []
# for i in range(n):
#     total_spent = int(input())
    
#     if i > 0:
#         prev_num = totals[i - 1]
#         total_spent += prev_num
#     totals.append(total_spent)

# for t in totals:
#     print(t)

# -------------------------------------------
# 108. DMOJ problem bsspc22c1p2, BSSPC '22 P2 - Rhyming Numbers

# n = int(input())

# results = []
# for _ in range(n):
#     numbers = list(map(str, input().split()))
#     x, y = numbers[0], numbers[1]
#     if x[-2:] != '17' and y[-2:] != '17':
#         if (x[-1] == '7' and y[-2:] == '11') or (x[-2:] == '11' and y[-1] == '7'):
#             results.append('YES')
#         else:
#             results.append('NO')
#     else:
#         results.append('NO')

# for result in results:
#     print(result)


# -------------------------------------------
# 109. DMOJ problem bts16p1, Back To School '16: Harambe

# def print_count(characters):
#     lowercase = 0
#     uppercase = 0
#     for char in characters:
#         if char.islower():
#             lowercase += 1
#         elif char.isupper():
#             uppercase += 1

#     if lowercase > uppercase:
#         return 1
#     elif uppercase > lowercase:
#         return 0
#     else:
#         return -1

# characters = input()

# character_type = print_count(characters)

# if character_type == 1:
#     result = characters.lower()
#     print(result)
# elif character_type == 0:
#     result = characters.upper()
#     print(result)
# else:
#     print(characters)

# -------------------------------------------
# 110. DMOJ problem bts17p1, Back To School '17: 🅱aram🅱e

# text = input()
# result = ""

# for i in range(len(text)):
#     char = text[i]
#     if i == 0:
#         result += char
#     if i >= 1:
#         if char.isupper():
#             result += ". " + char
#         else:
#             result += char
#     if i == range(len(text)):
#         result += char + "."

# print(result)

# -------------------------------------------
# 111. DMOJ problem bts18p1, Back To School '18: Harambe


# sentence = input()
# sentence_two = input()
# k = int(input())

# difference_count = 0
# space_letter_change = False

# for char1, char2 in zip(sentence, sentence_two):
#     if char1 != char2:
#         difference_count += 1
#     if (char1 == " " and char2 != ' ') or (char1 != " " and char2 == " "): 
#         space_letter_change = True

# difference_count += abs(len(sentence) - len(sentence_two))

# if difference_count > k:
#     print('No plagiarism')
# elif space_letter_change == True:
#     print('No plagiarism')
# else: 
#     print('Plagiarized')

# -------------------------------------------
# 112. DMOJ problem bts19p1, Back To School '19: H🅰️r🅰️mbe

# n = int(input())

# words = list(map(str, input().split()))
# target_word = input()
# target_len = len(target_word)

# closest_word = ''
# min_difference = 10000 #arbitrary large number

# for word in words:
#     word_len = len(word)

#     if word_len <= target_len:
#         difference = target_len - word_len

#         if difference < min_difference:
#             closest_word = word
#             min_difference = difference

# print(closest_word)

# -------------------------------------------
# 112. DMOJ problem ccc00j2, CCC '00 J2 - 9966 Canadian Computing Competition: 2000 Stage 1, Junior #2

# def is_rotatable(nums, rotate_map):
#     rotated = ''
#     for char in nums:
#         if char not in rotate_map:
#             return False
#         rotated += rotate_map[char]

#     return rotated[::-1] == nums

# m = int(input())
# n = int(input())

# rotate_map = {'0': '0', '1': '1', '8':'8', '6': '9', '9': '6'}

# rotatable_count = 0
# for n in range(m, n + 1):
#     if is_rotatable(str(n), rotate_map):
#         rotatable_count += 1

# print(rotatable_count)

# -------------------------------------------
# 112. DMOJ problem ccc01j1, CCC '01 J1 - Dressing Up

# Read input
# H = int(input())

# # Print top  
# for i in range(H // 2):
#     stars = '*' * (2 * i + 1)
#     spaces = ' ' * (2 * (H - i*2 - 1))
#     print(stars + spaces + stars)

# # Print the middle
# stars = '*' * 2 * H
# print(stars)

# # Print bottom half (mirroring the top half)
# for i in range(H // 2 - 1, -1, -1):
#     stars = '*' * (2 * i + 1)
#     spaces = ' ' * (2 * (H - i*2 - 1))
#     print(stars + spaces + stars)

# -------------------------------------------
# 113. DMOJ problem ccc01j2, CCC '01 J2 - Mod Inverse

# x = int(input())
# m = int(input())

# n_nums = list(map(int, range(1, m + 1)))

# found = True
# for n in n_nums:
#     if (x * n) % m == 1:
#         print(n)
#         found = True
#         break
#     else:
#         found = False

# if found == False:
#     print('No such integer exists.')

# -------------------------------------------
# 114. DMOJ problem ccc02j1, CCC '02 J1 - 0123456789
# copied from https://github.com/AAZZAZRON/DMOJ-Solutions/blob/main/ccc02j1.py because i couldnt figure out the whitespace
# num = int(input())
# if num == 0:
#     print(" * * *")
#     print("*     *")
#     print("*     *")
#     print("*     *")
#     print("")
#     print("*     *")
#     print("*     *")
#     print("*     *")
#     print(" * * *")
# elif num == 1:
#     print("\n      *")
#     print("      *")
#     print("      *")
#     print("")
#     print("      *")
#     print("      *")
#     print("      *\n")
# elif num == 2:
#     print(" * * *")
#     print("      *")
#     print("      *")
#     print("      *")
#     print(" * * *")
#     print("*")
#     print("*")
#     print("*")
#     print(" * * *")
# elif num == 3:
#     print(" * * *")
#     print("      *")
#     print("      *")
#     print("      *")
#     print(" * * *")
#     print("      *")
#     print("      *")
#     print("      *")
#     print(" * * *")
# elif num == 4:
#     print("\n*     *")
#     print("*     *")
#     print("*     *")
#     print(" * * *")
#     print("      *")
#     print("      *")
#     print("      *\n")
# elif num == 5:
#     print(" * * *")
#     print("*")
#     print("*")
#     print("*")
#     print(" * * *")
#     print("      *")
#     print("      *")
#     print("      *")
#     print(" * * *")
# elif num == 6:
#     print(" * * *")
#     print("*")
#     print("*")
#     print("*")
#     print(" * * *")
#     print("*     *")
#     print("*     *")
#     print("*     *")
#     print(" * * *")
# elif num == 7:
#     print(" * * *")
#     print("      *")
#     print("      *")
#     print("      *")
#     print("")
#     print("      *")
#     print("      *")
#     print("      *\n")
# elif num == 8:
#     print(" * * *")
#     print("*     *")
#     print("*     *")
#     print("*     *")
#     print(" * * *")
#     print("*     *")
#     print("*     *")
#     print("*     *")
#     print(" * * *")
# elif num == 9:
#     print(" * * *")
#     print("*     *")
#     print("*     *")
#     print("*     *")
#     print(" * * *")
#     print("      *")
#     print("      *")
#     print("      *")
#     print(" * * *")

# -------------------------------------------
# 115. DMOJ problem ccc02j2, CCC '02 J2 - AmeriCanadian

# words = []
# while True:
#     word = input()
#     vowels = 'aiouey'

#     if word == 'quit!':
#         break
#     elif len(word) > 4 and word[-3] not in vowels and word[-2:] == 'or':
#         new_word = word[:-2] + 'our'
#         words.append(new_word)
#     else:
#         words.append(word)

# for word in words:
#     print(word)

# -------------------------------------------
# 115. DMOJ problem ccc03j1, CCC '03 J1 - Trident

# t - height of tines, s - spacing between tines, h - handle length

# t = int(input())
# s = int(input())
# h = int(input())

# # print top
# for _ in range(t):    
#     print('*' + ' ' * s + '*' + ' ' * s + '*')

# # print middle
# print((s * 2 + 3)*'*')

# # print handle
# for _ in range(h):
#     print(' ' * (s + 1) + '*')


# -------------------------------------------
# 116. DMOJ problem ccc03j2, CCC '03 J2 - Picture Perfect

# import math

# def minimum_perimeter(n):
#     min_perimeter = float('inf')

#     for width in range(1, int(math.sqrt(n)) + 1):
#         if n % width == 0:
#             length = n // width
#             perimeter = 2 * (length + width)
#             if perimeter < min_perimeter:
#                 min_perimeter = perimeter
#                 optimal_length, optimal_width = length, width  
           
#     return min_perimeter, optimal_length, optimal_width

# answers = []
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     else: 
#         data = minimum_perimeter(n)
#         answer = f'Minimum perimeter is {data[0]} with dimensions {data[2]} x {data[1]}'
#         answers.append(answer)

# for answer in answers:
#     print(answer)
    
# -------------------------------------------
# 117. DMOJ problem ccc04j1, CCC '04 J1 - Squares
# import math

# n = int(input())

# side = int(math.sqrt(n))

# print(f'The largest square has side length {side}.')

# -------------------------------------------
# 118. DMOJ problem ccc04j2, CCC '04 J2 - Terms of Office

# x = int(input())
# y = int(input())

# lcm = 2**2 * 3 * 5

# answers = []
# year = x
# while year <= y:
#     print(f'All positions change in year {year}')
#     year += lcm
#     if year > y:
#         break
#     answers.append(year)

# for a in answers:
#     print(f'All positions change in year {a}')

#  ccc04j3 CCC '04 J3 - Smile with Similes 
# nr_adj = int(input())
# nr_noun = int(input())

# adjectives = []
# for _ in range(nr_adj):
#     adj = input()
#     adjectives.append(adj)

# nouns = []
# for _ in range(nr_noun):
#     noun = input()
#     nouns.append(noun)

# phrases = []
# for i in range(len(adjectives)):
#     for j in range(len(nouns)):
#         phrase = adjectives[i] + ' as ' + nouns[j]
#         phrases.append(phrase)

# for phrase in phrases:
#     print(phrase)

# ccc05j1 CCC '05 J1 - The Cell Sell

# daytime_min = int(input())
# evening_min = int(input())
# weekend_min = int(input())

# def plan_a(d, e, w):
#     if d > 100:
#         daytime = (d - 100) * 0.25
#     else:
#         daytime = 0
    
#     evening = e * 0.15
#     weekend = w * 0.20

#     return daytime + evening + weekend 

# def plan_b(d, e, w):
#     if d > 250:
#         daytime = (d - 250) * 0.45
#     else:
#         daytime = 0
    
#     evening = e * 0.35
#     weekend = w * 0.25

#     return daytime + evening + weekend 

# plan_a_total = plan_a(daytime_min, evening_min, weekend_min)
# plan_b_total = plan_b(daytime_min, evening_min, weekend_min)

# if plan_a_total > plan_b_total:
#     print(f"Plan A costs {plan_a_total:.2f}")
#     print(f"Plan B costs {plan_b_total:.2f}")
#     print(f"Plan B is cheapest.")

# elif plan_b_total > plan_a_total:
#     print(f"Plan A costs {plan_a_total:.2f}")
#     print(f"Plan B costs {plan_b_total:.2f}")
#     print(f"Plan A is cheapest.")

# else:
#     print(f"Plan A costs {plan_a_total:.2f}")
#     print(f"Plan B costs {plan_b_total:.2f}")
#     print(f"Plan A and B are the same price.")

# ccc05j2 CCC '05 J2 - RSA Numbers
# num1 = int(input())
# num2 = int(input())

# num_list = list(range(num1, num2+1))

# numbers = []
# for i in range(len(num_list)):
#     counter = 0
#     for j in range(1, num_list[i]+1):
#         if num_list[i] % j == 0:
#             counter += 1
#     if counter == 4:
#         numbers.append(num_list[i])

# number_of_rsa_numbers = len(numbers)

# print(f"The number of RSA numbers between {num1} and {num2} is {number_of_rsa_numbers}")

# ccc06j2 CCC '06 J2 - Roll the Dice

# d1 = int(input())
# d2 = int(input())

# counter = 0
# for i in range(1, d1 + 1):
#     for j in range(1, d2 + 1):
#         if i + j == 10:
#             counter += 1

# if counter == 0 or counter > 1:
#     print(f'There are {counter} ways to get the sum 10.')
# else:
#     print(f'There is {counter} way to get the sum 10.')

# ccc07j1 CCC '07 J1 - Who is in the Middle?
# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
 
# def find_mid(n1, n2, n3):
#     if n1 < n2 < n3 or n1 > n2 > n3:
#         return n2
#     elif n2 < n1 < n3 or n2 > n1 > n3:
#         return n1
#     else:
#         return n3
    
# mid_num = find_mid(n1, n2, n3)

# print(mid_num)     

#  ccc07j2 CCC '07 J2 - I Speak TXTMSG

# txt_diction = {'CU': 'see you', 
#                ':-)': "I'm happy", 
#                ':-(': "I'm unhappy", 
#                ';-)': 'wink', 
#                ':-P': 'stick out my tongue', 
#                '(~.~)': 'sleepy', 
#                'TA': 'totally awesome', 
#                'CCC': 'Canadian Computing Competition', 
#                'CUZ': 'because', 
#                'TY': 'thank-you', 
#                'YW': "you're welcome", 
#                'TTYL': 'talk to you later'
#                }

# to_translate = []

# while True:
#     inpt = input()

#     if inpt == 'TTYL':
#         to_translate.append(inpt)
#         break
#     else:
#         to_translate.append(inpt)

# for t in to_translate:
#     if t in txt_diction:
#         print(txt_diction[t])
#     else:
#         print(t)










