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

#23 Uncrackable wc17c3j3

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

# def count_sequence(user_input: str) -> int:

#     target_sequence = "HONI"
#     sequence_index = 0
#     count = 0
#     for letter in user_input:

#         if letter == target_sequence[sequence_index]:
#             sequence_index += 1

#             if sequence_index == len(target_sequence):
#                 count += 1
#                 sequence_index = 0
    
#     return count
   
# user_input = input('> ')
# result = count_sequence(user_input)
# print(result)

#25 Occupied spaces

# n = int(input('> '))
# yesterday = input('> ')
# today = input('> ')

# occupied = 0

# for i in range(len(yesterday)):
#     if yesterday[i] =='C' and today[i] == "C":
#         occupied += 1

# print(occupied)

#26 Data Plan
# monthly_mb = int(input())
# n = int(input())

# excess = 0

# for i in range(n):
#     used = int(input())
#     excess = excess + monthly_mb - used

# print(excess + monthly_mb)

# total = monthly_mb * (n + 1)
# total_used = 0

# for i in range(n):
#     used = int(input('> '))
#     total_used = total_used + used

# print(total - total_used)

#27 English or French ccc11s1
 
# n = input('> ')

# t = 0
# s = 0
# for line in range(int(n)):
#     text = input('> ')

#     for i in range(len(text)):
#         if text[i] == 'T' or  text[i] == 't':
#             t += 1
#         if text[i] == 'S' or text[i] == 's':
#             s += 1

# print(t)
# print(s)

# if t > s:
#     print('English')
# if s >= t:
#     print('French')

#28 Multiple Choice ccc11s2
# number_of_questions = int(input('> '))
# student = []
# teacher = []
# for n in range(number_of_questions):
#     student_answers = (input('> '))
#     student.append(student_answers)
#     print(student)
# for n in range(number_of_questions):
#     correct_answers = (input('> '))
#     teacher.append(correct_answers)
#     print(teacher)

# correct = 0
# for i in range(number_of_questions):
#     if student[i] == teacher[i]:
#         correct += 1

# print(correct)

#29 lJESTVICA coci12c5p1

# music = input('> ')
# notes = []

# notes.append(music[0])
# for i in range(len(music)):
#     if music[i] == '|':
#         notes.append(music[i+1])

# A = 0
# C = 0
# for i in range(len(notes)):
#     if notes[i] == 'A':
#         A += 1
#     if notes[i] == 'C':
#         C += 1

# if A > C:
#     print('A-mol')
# if A < C:
#     print('C dur')
# if A == C:
#     last_note = music[-1]
#     print(last_note)
#     if last_note == 'C':
#         print('C dur')
#     else:
#         print('A mol')

# print(notes)

#30 Rijeci coci18c4p1

# n = int(input('> '))

# sequence = ['A']
# for i in range(n):
#     new_sequence = []

#     for letter in sequence:
#         if letter == 'A':
#             new_sequence.append('B')
#         if letter == 'B':
#             new_sequence.append('B')
#             new_sequence.append('A')
    
#     sequence = new_sequence

# A = 0
# B = 0

# for i in range(len(sequence)):
#     if sequence[i] == 'A':
#         A += 1
#     if sequence [i] == 'B':
#         B += 1

# print(A, B)

#31 Elder coci18c4p1

# wizard = input('> ')
# duels = int(input('> '))

# elder = [wizard]
# new_wizard = []
# counter = 1
# for _ in range(duels):
    
#     w1 = input('> ')
#     w2 = input('> ')
    
#     if w2 == wizard:
#         new_wizard = w1
#         wizard = new_wizard
#         counter += 1
#         elder.append(new_wizard)

# print(elder)
# print(len(set(elder)))        

#32 Slot machines ccc00s1

# quarters = int(input('> '))

# first = int(input('> '))
# second = int(input('> '))
# third = int(input('> '))

# plays = 0

# while quarters >= 1:
#     machine = plays % 3
#     quarters -= 1
 
#     if machine == 0:
#         first += 1
#         if first % 35 == 0:
#             quarters += 30
#     elif machine == 1:
#         second += 1
#         if second % 100 == 0:
#             quarters +=60
#     elif machine == 2:
#         third += 1
#         if third % 10 == 0:
#             quarters += 9

#     plays += 1

# print(f"Martha plays {plays} times before going broke.")


#33 Epidemiology ccc20j2

# P = int(input('> '))
# N = int(input('> '))
# R = int(input('> '))

# D = 0
# while N < P:
   
#     N = N*R
#     print(N)

#     if N <= P:
#         D += 1
#         print(D)
   

# print(D)

#34 Song playlist ccc08j2
# songs = 'ABCDE'

# button = 0

# while button != 4:
#     button = int(input())
#     presses = int(input())
#     for i in range(presses):
#         if button == 1:
#             songs = songs[1:] + songs[0]
#         elif button == 2:
#             songs = songs[-1] + songs[:-1]
#         elif button == 3:
#             songs = songs[1] + songs[0] + songs[2:]
    
# output = ''

# for song in songs:
#     output = output + song + ' ' 

# print(output[:-1])

#35 AmeriCanadian ccc02j2
# user_word = ''

# while user_word != 'quit!':
#     user_word = input('> ')
#     result = ''
#     i = 0
#     vowel = 'aeiouy'
#     if len(user_word) > 4:
#         while i < len(user_word):
#             if user_word[i:i+2] == 'or' and user_word[i-1] not in vowel:
#                 result += 'our'
#                 i += 2
#             else:
#                 result += user_word[i]
#                 i += 1
#     print(result)

#36 Secret sentence coci08c3p2 own solution

# secret = input('> ')
# not_secret = ''
# vowels = 'aeiou'
# i = 0

# while i < len(secret):
#     if secret[i+2] == secret[i] and secret[i] in vowels:
#         not_secret += secret[i]
#         i += 3
#     else:
#         not_secret += secret[i]
#         i += 1
    
#     print(not_secret)

#36 Secret sentence coci08c3p2 solution 2
# sentence = input('> ')

# result = ''
# i = 0

# while i < len(sentence):
#     result = result + sentence[i]
#     if sentence [i] in 'aeiou':
#         i = i + 3
#     else:
#         i = i + 1

# print(result)

#37 Ptice coci08c1p2

# num = int(input('> '))
# answers = input('> ')

# Adrian = 'ABC'
# Bruno = 'BABC'
# Goran = 'CCAABB'

# def repeated_pattern(name, num):
#     return (name*(num // len(name) + 1 ))[:num]
    

# def number_of_correct_answers(repeated_pattern, answers):
#     correct_answers = 0
#     for i in range(len(answers)):
#         if answers[i] == repeated_pattern[i]:
#             correct_answers += 1
#             i += 1

#     return correct_answers

# adrian_score = number_of_correct_answers(repeated_pattern(Adrian, num), answers)
# bruno_score = number_of_correct_answers(repeated_pattern(Bruno, num), answers)
# goran_score = number_of_correct_answers(repeated_pattern(Goran, num), answers)

# max_score = max(adrian_score, bruno_score, goran_score)
# print(max_score)

#38  Take a Number ecoo13r1p1

# next_number = int(input('> '))
# status = ''
# students = 0

# tmp_take = next_number
# tmp_serve = next_number
# while status != 'EOF':
#     status = input('> ')
    
    
#     if status == 'TAKE':
#         tmp_take += 1
#         if tmp_take > 999:
#             tmp_take = 1
#         students += 1
#         print(tmp_take)
#     if status == 'SERVE':
#         if tmp_serve > 999:
#             tmp_serve = 1
#         tmp_serve += 1
#         print(tmp_serve)
#     if status == 'CLOSE':
#         not_served = tmp_take - tmp_serve
#         if not_served < 0:
#             not_served += 999
#         print(students, not_served, tmp_take)
#         students = 0


#39 When you eat your smarties ecoo15r1p1
# smarties = ''

# time = 0
# counter = 0
# while smarties != 'end of box':
#     smarties = input('> ')

#     counter_tmp = counter
#     if smarties == 'red':
#         time += 16
#     if smarties != 'red':
#         counter += 1
#         if counter % 7 == 0:
#             counter = 0
#             time +=13
# print(time)


#40 Cold compress ccc19j3

# code = input('> ')

# result= []
# current_char = code[0]
# count = 1

# for i in range(1, len(code)):
#     if current_char == code[i]:
#         count += 1
#     else:
#         result.append(str(count))
#         result.append(current_char)
#         current_char = code[i]
#         count = 1

# result.append(str(count))
# result.append(current_char)


# output = " ".join(result)
# print(output)

#41 Village neighbourhood ccc18s1
# n = int(input())

# positions = []

# for i in range(n):
#     positions.append(int(input()))
    
# positions.sort()

# # left = (positions[1] - positions[0]) / 2   -- if not using "HUGE SiZE"
# # right = (positions[2] - positions[1]) / 2
# # min_size = left + right

# #if using HUGE SIZE:
# min_size = 1000000000

# for i in range(1, n-1):
#     left = (positions[1] - positions[0]) / 2
#     right = (positions[2] - positions[1]) / 2
#     size = left + right
#     if size < min_size:
#         min_size = size

# print(min_size)

#41 Village neighbourhood min method

# n = int(input('> '))
# positions = []

# for i in range(n):
#     positions.append(int(input()))

# positions.sort()

# sizes = []

# for i in range(1, n-1):
#     left = (positions[i] - positions[i - 1]) / 2
#     right = (positions[i] - positions[i - 1]) / 2
#     size = left + right
#     sizes.append(size)

# min_size = min(sizes)
# print(min_size)

#42 No Deal Calculator ccc07j3
# suitcase = []

# n = int(input('> '))
# for _ in range(n):
#     suitcase.append(int(input('> ')))

# banker = int(input('> '))

# money = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]

# for index in sorted(suitcase, reverse=True):
#     money.pop(index-1)
    
# print(money)

# remaining_average = sum(money)/(len(money))
# print(remaining_average)

# if remaining_average > banker:
#     print('no deal')
# else:
#     print('deal')

#43 School trip ec0017r1p1

# YEAR_COSTS = [12, 10, 7, 5]

# for dataset in range(10):
#     trip_cost = int(input('> '))
#     proportions = input().split()
#     num_students = int(input())

#     for i in range(len(proportions)):
#         proportions[i] = float(proportions[i])
        
#     students_per_year = []
    
#     for proportion in proportions:
#         students = int(num_students * proportion)
#         students_per_year.append(students)

#     #account for rounding
#     counted = sum(students_per_year)
#     uncounted = num_students - counted
#     most = max(students_per_year)
#     where = students_per_year.index(most)
#     students_per_year[where] = students_per_year[where] + uncounted

#     total_raised = 0
    
#     for i in range(len(students_per_year)):
#         total_raised = total_raised + students_per_year[i] * YEAR_COSTS[i]
        
#     if total_raised / 2 < trip_cost:
#         print('YES')
#     else:
#         print('NO')

#44 Willow's wild ride ecoo18r1p1

# t = int(input('> '))
# n = int(input('> '))


# willow_busy_until = 0 #last day willow id busy playing with a box
# total_delay = 0 #total number of days Willow delayed project

# for day in range(1, n+1):
#     box_timetable = input('>')
#     if box_timetable == "B":
#         if day <= willow_busy_until:
#             willow_busy_until += t # no -1 because willow is already in the process of playing
#         else:
#             willow_busy_until = day + t - 1 # -1 because willow starts playing with the box on the same day
        
# if willow_busy_until > 0:
#     total_delay = willow_busy_until - n
# if total_delay < 0:
#     total_delay = 0

# print(total_delay)

#Willow's wild ride (list solution)

# t = int(input()) #number of days willow plays with a box
# n = int(input()) #number of days till project is due

# willow_boxes = [] #list to track number of days willow is busy with each box
# total_delay = 0 #total number of days Willow delayed project

# for day in range(n):
#     box_timetable = input()

#     #decrement number of play days for each box in the list
#     willow_boxes = [days_left - 1 for days_left in willow_boxes if days_left - 1 > 0]

#     if box_timetable == "B":
#         #mandy brings new box, add 't' days for this box
#         willow_boxes.append(t)

#     #count total delay (number of boxes willow is still playing with)
#     total_delay += len(willow_boxes)

# print(total_delay)

# def willow_delay(t, n, boxes_by_days):
#     total_delay = 0 #total number of days Willow delayed project

#     for box_timetable in boxes_by_days:
#         total_delay = max(total_delay - 1, 0)
#         if box_timetable == "B":
#             total_delay += t
        
#     total_delay = max(total_delay - 1, 0)
#     return total_delay

# def delay_couter_main():
#     all_delays = []
    
#     for _ in range(10):
#         first_line = input().split()
#         t = int(first_line[0])
#         n = int(first_line[1])
#         boxes_by_days = []

#         for i in range(n):
#             row = input()
#             boxes_by_days.append(row)
        
#         all_delays.append(willow_delay(t, n, boxes_by_days))
    
#     for delay in all_delays:
#         print(delay)

# delay_couter_main()

#45 Baker Bonus ecoo17r3p1

# for dataset in range(10):
#     first_line = input().split()
#     franchisees = int(first_line[0])
#     days = int(first_line[1])
#     grid = []

#     for i in range(days):
#         row = input().split()
#         for j in range(franchisees):
#             row[j] = int(row[j])
#         grid.append(row)

#     bonuses = 0
    
#     for row in grid:
#         total = sum(row)
#         if total % 13 == 0:
#             bonuses = bonuses + total // 13

#     for col_index in range(franchisees):
#         total = 0
#         for row_index in range(days):
#             total = total + grid[row_index][col_index]
#         if total % 13 == 0:
#             bonuses = bonuses + total // 13

#     print(bonuses)

#46 Cezar

# n = int(input('> '))

# column_sequence = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
# grid = []
# for i in range(len(column_sequence)):
#     row = []
#     for j in range(4):
#         row.append(int(column_sequence[i]))
#     grid.append(row)
    
# cesar_cards = []
# for _ in range(n):
#     cesar_card = int(input('> '))
#     cesar_cards.append(cesar_card)

#     for row in grid:
#         if cesar_card in row:
#             row.remove(cesar_card)

# cesar_sum = sum(cesar_cards)
# difference = 21 - cesar_sum

# if difference == 0:
#     print('DOSTA')
# else:
#     count_less = 0
#     count_more = 0
#     for row in grid:
#         for element in row:
#             if element <= difference:
#                 count_less += 1
#             else:
#                 count_more += 1

        
#     if count_more >= count_less:
#         print('DOSTA')
#     else:
#         print('VUCI')

#47 Preokret coci18c2p1


seconds_A = []
points_A = int(input())
for _ in range(points_A):
    scores_A = int(input())
    seconds_A.append(scores_A)

print(seconds_A)

seconds_B=[]
points_B = int(input())
for _ in range(points_B):
    scores_B = int(input())
    seconds_B.append(scores_B)

print(seconds_B)

full_game = 4*12*60
half_game = full_game/2

total_pointsA = 0
total_pointsB = 0

for time in seconds_A:
    if time <= half_game:
        total_pointsA += 1
        
for time in seconds_B:
    if time <= half_game:
        total_pointsB += 1
        
total_points = total_pointsA + total_pointsB

total_scores = points_A + points_B

print(total_scores)

scoreA = 0
scoreB = 0
turnarounds = 0

for i in range(total_scores):
    if seconds_A[i] < seconds_B[i]:
        scoreA += 1
    if seconds_B[i] < seconds_A[i]:    
        scoreB += 1
    print(scoreA, scoreB)
    if scoreA - scoreB != 0 or scoreB - scoreA != 0:
        turnarounds += 1
        print(turnarounds)

print(turnarounds)



#48 Babbling brooks ccc00s2

# n = int(input('> '))

# streams = []

# for _ in range(n):
#     streams.append(int(input()))

# command = 0

# while True:
#     command = (input())

#     if command == '99':
#         stream_split = int(input())
#         stream_split_percentage = float(input())
#         value = streams[stream_split-1]

#         first_part = value*(stream_split_percentage/100)
#         second_part = value*(1 - (stream_split_percentage/100))

#         streams.pop(stream_split-1)
#         streams.insert(stream_split-1, first_part)
#         streams.insert(stream_split, second_part)

#     if command == '88':
#         index = int(input())

#         merged_streams = streams[index-1] + streams[index]
#         streams[index-1] = merged_streams
#         streams.pop(index)


#     if command == '77':
#         break

# rounded_streams = [round(num) for num in streams]
# print(*rounded_streams)




#49 Free Shirts ecoo19r1p1

# for dataset in range(10):

#     first_line = input().split()
#     clean_shirts = int(first_line[0])
#     number_of_events = int(first_line[1])
#     number_or_days = int(first_line[2])

#     event_days = []
#     for _ in range(number_of_events):
#         days = input().strip().split()
#         for day in days:
#             event_days.append(int(day))
 

#     laundry_days = 0
#     total_shirts = clean_shirts
#     grand_total_shirts = clean_shirts
   
#     for day in range(number_or_days):
     
#         if clean_shirts == 0:    
#             laundry_days += 1
#             clean_shirts = grand_total_shirts
#         if (day+1) in event_days:
#             clean_shirts += 1 
#             grand_total_shirts += 1
#         if clean_shirts >= 1:
#             clean_shirts -= 1    

#     print(laundry_days)













