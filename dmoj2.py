#51 Rue's Rings ecoo18r1p2

# for dataset in range(1):

#     routes = []

#     number_of_routes = int(input())
#     for _ in range(number_of_routes):
#         route_info = list(map(int, input().split()))
#         route_id = route_info[0]
#         min_r = min(route_info[2:])

#         routes.append((route_id, min_r))

#     min_diameter = 70001
#     for i in range(len(routes)):
#         if routes[i][1] < min_diameter:
#             min_diameter = routes[i][1]

#     route_number = []
#     for i in range(len(routes)):
#         if min_diameter == routes[i][1]:
#             route_number.append((routes[i][0]))

        
#     route_number.sort()
#     str_sorted_routes = list(map(str, route_number))
#     answer = '{' + ','.join(str_sorted_routes)+'}'
#     print(f"{min_diameter} {answer}")

#52 Emacs coci19c5p1

# num_rows_cols = list(map(int, input().split()))
# num_rows = num_rows_cols[0]
# num_cols = num_rows_cols[1]

# grid = []

# for _ in range(num_rows):
#     row = input()

#     grid.append(row)

# rectangles = 0
# for i in range(num_rows):
#     for j in range(num_cols):
#         if (i - 1) >= 0 and (j-1) >=0: 
#             if (grid[i][j] == "*" and grid[i-1][j-1] != "*" and grid[i][j-1] != "*"
#                 and grid[i-1][j] != "*") : 
#                 rectangles += 1
#         if (i - 1) < 0 and (j-1) >=0:
#             if grid[i][j] == "*" and grid[i][j-1] != "*":
#                 rectangles += 1
#         if ( i - 1) >= 0 and (j - 1) < 0:
#             if grid[i][j] == "*" and grid[i - 1][j] != "*":
#                 rectangles += 1
#         if (i-1) < 0 and (j-1) < 0:
#             if grid[i][j] == "*":
#                 rectangles +=1

# print(rectangles)

#53 Crtanje coci20c2p1

# row = x+100 if need to access row x

# num_days = int(input())
# net_change = input()

# current_row_num = 0
# grid = [['.']*num_days]
# for day in range(num_days):
#     if net_change[day] == "+":
#         grid[current_row_num][day] = "/"
#     elif net_change[day]  == "-":
#         grid[current_row_num][day] = "\\"
#     elif net_change[day] == "=":
#         grid[current_row_num][day] = "_"
#     if day + 1 < num_days:
#         if net_change[day] == "+" and net_change[day + 1] == "+":
#             current_row_num -= 1
#         elif net_change[day] == "-" and net_change[day + 1] == "-":
#             current_row_num += 1
#         elif net_change[day] == "+" and net_change[day + 1] == "=":
#             current_row_num -= 1
#         elif net_change[day] == "=" and net_change[day + 1] == "-":
#             current_row_num += 1    
#         if current_row_num < 0:
#             grid.insert(0, ['.']*num_days) 
#             current_row_num = 0
#         elif current_row_num >= len(grid):
#             grid.append(["."]*num_days)

# str_grid = list(map(''.join, grid))
# str_grid = [ st.strip() for st in str_grid ]
# print("\n".join(str_grid))

#54 Card game ccc99s1

# NUM_CARDS = 52

# def no_high(lst):
#     """ 
#     lst is a list of strings representing cards.

#     Return True if there are no high cards in lst, False otherwise.
#     """

#     if 'jack' in lst:
#         return False
#     if 'queen' in lst:
#         return False
#     if 'king' in lst:
#         return False
#     if 'ace' in lst:
#         return False
#     return True

# deck = []

# for i in range(NUM_CARDS):
#     deck.append(input())

# score_a = 0
# score_b = 0
# player = 'A'

# for i in range(NUM_CARDS):
#     card = deck[i]
#     points = 0
#     remaining = NUM_CARDS - i - 1
#     if card == 'jack' and remaining >=1 and no_high(deck[i+1:i+2]):
#         points = 1
#     elif card == 'queen' and remaining >= 2 and no_high(deck[i+1: i+3]):
#         points = 2
#     elif card == 'king' and remaining >=3 and no_high(deck[i+1:i+4]):
#         points = 3
#     elif card == 'ace' and remaining >=4 and no_high(deck[i+1:i+5]):
#         points = 4

#     if points > 0:
#         print(f'Player {player} scores {points} point(s).')

#     if player == "A":
#         score_a = score_a + points
#         player = 'B'
#     else:
#         score_b = score_b + points
#         player = 'A'

# print(f'Player A: {score_a} point(s).')
# print(f'Player B: {score_b} point(s).')

#55 Action Figures https://acm.timus.ru/problem.aspx?space=1&num=2144

#Read input
#Check whether all boxes are OK
#Obtain a new lit of boxees with only left and right heights
#Sort boxes
#Determine whether boxes are organised



# def read_boxes(n):
#     """
#     n is the number of boxes to read.

#     Read the boxes from the input, and return them as a list of boxes;
#     Each box is a list of action figure heights.
#     """

#     boxes = []
#     for i in range(n):
#         box = input().split()
#         box.pop(0)
#         for i in range(len(box)):
#             box[i] = int(box[i])
#         boxes.append(box)
#     return boxes

# def all_boxes_ok(boxes):

# def read_boxes(n):
#     """
#     n is the number of boxes to read.

#     Read the boxes from the input, and return them as a list of boxes;
#     Each box is a list of action figure heights.
#     """

#     boxes = []
#     for i in range(n):
#         box = input().split()
#         box.pop(0)
#         for i in range(len(box)):
#             box[i] = int(box[i])
#         boxes.append(box)
#     return boxes

# def all_boxes_ok(boxes):
#     """
#     boxes is a list of boxes; each box is a list of action figure heights.

#     Return True if each box in boxes has its action figures in 
#     nondecreasing order of height, False otherwise.
#     """

#     for box in boxes:
#         if not box_ok(box):
#             return False
#         return True

# def box_ok(box):
#     """
#     box is the list of action figure heights in a given box.

#     Return True if the heights in box are in nondecreasing order,
#     False otherwise.
#     """

#     for i in range(len(box) - 1):
#         if box[i] > box[i + 1]:
#             return False

#     return True

# def boxes_endpoints(boxes):
#     """
#     boxes is a list of boxes; each box is a lit of action figure heights.

#     return a list, where each value is a list of two values:
#     the heights of the leftmost and rightmost figures in a box.
#     """

#     endpoints = []
#     for box in boxes:
#         endpoints.append(box[0], box[-1])
#     return endpoints

# def all_endpoints_ok(endpoints):
#     """
#     endpoints is a list, where each value is a list of two values:
#     the heights of the leftmost and rightmost action figures in a box.

#     Requires: endponts is sorted by action figure heights.

#     Return True if the endpoints came from boxes that can be put in order,
#     False otherwise.
#     """

#     maximum = endpoints[0][1]
#     for i in range(1, len(endpoints)):
#         if endpoints[i][0] < maximum:
#             return False
#         maximum = endpoints[i][1]
#     return True

# #Main Program
# #Read input
# n = int(input())
# boxes = read_boxes(n)

# #Check whether all boxes are OK
# if not all_boxes_ok(boxes):
#     print('NO')
# else:
#     #Obtain a new list of boxes with only left and ight heights
#     endpoints = boxes_endpoints(boxes)

#     #Sort boxes
#     endpoints.sort()

#     #Determine whether boxes are organised
#     if all_endpoints_ok(endpoints):
#         print('YES')
#     else:
#         print('NO')


# 56 From 1987 to 2013 ccc13s1

# def digit_same(year) -> bool:
#     return len(set(year)) != len(year)

# input_year = int(input())
# year = str(input_year + 1)

# while digit_same(year):       #while always default True
#     num_year = int(year)
#     num_year += 1
#     year = str(num_year)

# print(year)


#from 1987 to 2013 var2
# def same_digit(numberInt):
#     number = str(curentNumber)
#     for i in range(len(number)):
#         for j in range(len(number)):
#             if i != j and number[i] == number[j]:
#                 return True
    
#     return False


# initialNumber = int(input())

# curentNumber = initialNumber + 1
 

# while same_digit(curentNumber):
#     curentNumber += 1

# print(curentNumber)

#are we nearly there yet? ccc18j3

# dist_input = input()
# dist_lst = dist_input.split()

# def distance_table(dist_lst):
#     num1 = int(dist_lst[0])
#     num2 = int(dist_lst[1])
#     num3 = int(dist_lst[2])
#     num4 = int(dist_lst[3])
#     print(0, num1, num1 + num2, num1 + num2 + num3, num1 + num2 + num3 + num4 )
#     print(num1 + 0, 0, num2, num2 + num3, num2 + num3 + num4)
#     print(num1 + num2, num2, 0, num3, num3 + num4)
#     print(num1 + num2 + num3, num2 + num3, num3, 0, num4)
#     print(num1 + num2 + num3 + num4, num2 + num3 + num4, num3 + num4, num4, 0)
    

# distance_table(dist_lst)
    

#number reversals 
# # 1 - using "range"       
# numbers = [1, 2, 3, 4, 5]

# reversed_numbers = []

# for i in range(len(numbers) -1, -1, -1):
#     reversed_numbers.append(numbers[i])

# print(reversed_numbers)

# #2 using while loop (requies "tuple unpacking" for numbers[start], numbers[end] = numbeers[end], numbers[start])

# numbers = [1, 2, 3, 4, 5]

# start = 0
# end = len(numbers) - 1

# #swap elements until pointers meet in the middle

# while start > end:
#     #swap elements at start and end
#     numbers[start], numbers[end] = numbers[end], numbers[start]
#     #move pointers towards center
#     start +=1
#     end -=1

# print(numbers)

# #3 reversing a number without converting to string
# num = 12345
# reversed_num = 0

# while num > 0:
#     #extract the last digit
#     last_digit = num % 10
#     #shift reversed_num left and add last digit
#     reversed_num = reversed_num * 10 + last_digit
#     num //= 10

# print(reversed_num)

#57 Decoding DNA - ecoo12r1p2

# def DNA_data() -> list:
#     DNA_list = []

#     while len(DNA_list) < 5:
#         DNA_string = input()
#         DNA_list.append(DNA_string)
#     return DNA_list
    

# # identify TATAAT promotr and return start of transcription index
# def start_of_transcription(DNA_string: str) -> int:
#     index = DNA_string.find("TATAAT")
#     if index != -1:
#         # find returns -1 if no such string found, so we can control for this case
#         start_of_transcription = index + 10
#         return start_of_transcription
#     else:
#         print("promoter not found in strand")
#         return -1
            
# #save transcription_units
# def transcription_units(DNA_data, start_of_transcription) -> list:
#     transcription_units =[]
#     for strand in DNA_data:
#         transcription_unit = strand[start_of_transcription:]
#         transcription_units.append(transcription_unit)
#     return transcription_units


# def complementary_reversed(sequence):    
#     complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
#     complement_sequence = "".join(complement[base] for base in sequence)
#     return complement_sequence[::-1]


# # identify base 6 terminator sequence
# def end_of_transcription(transcription_units) -> int:
#     length = 6 #length of terminatro sequence
#     end_of_transcription = None

#     for i in range(len(transcription_units)):
#         # extract candidate with base 6
#         candidate = transcription_units[i:i + length]
#         complementary_rev = complementary_reversed(candidate)

#         #search for this complementary reversed sequence after the candidate sequence
#         found_index = transcription_units.find(complementary_rev, i + length)

#         if found_index != -1:
#             end_of_transcription = found_index
#             break
        
#     #if no valid terminator found transcripton ends at end of strand
#     if end_of_transcription is None:
#         print("no terminator sequences found")

#     return end_of_transcription
  
# #convert RNA              
# def get_RNA(transcription_units, end_of_transcription):
#     if end_of_transcription is not None:
#         rna_code = {"A":"U","U":"A","C":"G","G":"C"}

#         # get transcription unit segment
#         dna_segment = transcription_units[:end_of_transcription]

#         # convert DNA to RNA
#         rna_result = "".join(rna_code[base] for base in dna_segment)
#         return rna_result
    
#     else:
#         print("no end of transcription found")
#         return None

# #Main program
# dna_strings_lst = DNA_data()
# print(start_of_transcription(dna_strings_lst))


#58 16 bit s/w only

# nr_lines = int(input())

# for _ in range(nr_lines):
#     data = input().split(" ")
#     data_int = list(map(int, data))
#     if data_int[0] * data_int[1] == data_int[2]:
#         print("POSSIBLE DOUBLE SIGMA")
#     else:
#         print("16 BIT S/W ONLY")

#59 Mispelling
# n = int(input())
# output = []
# for _ in range(n):
#     data = input().split(" ")
#     data_lst = list(map(str, data))
#     number = int(data_lst[0]) - 1
#     word = " ".join(data_lst[1:])
#     updated_word = word[:number] + word[number + 1:]
#     output.append(updated_word)
    

# for i in range(0, len(output)):
#     word = output[i]
#     print(f"{i + 1} {word}")
    
#60 Mirrored pairs
# def check_mirrored_pairs():

#     print("Ready")

#     mirrored_pairs = {("b", "d"), ("d", "b"), ("p", "q"), ("q", "p") }
#     while True:
        
#         user_input = input()
#         if user_input == "  ":
#             break
#         if len(user_input) != 2:
#             continue
#         char1, char2 = user_input[0], user_input[1]

#         if (char1, char2) in mirrored_pairs:
#             print("Mirrored pair")
#         else:
#             print("Ordinary Pair")

# check_mirrored_pairs()

#61 Sorting
# n = int(input())

# lst = []
# def sort(n):
#     for i in range(n):
#         nr = int(input())
#         lst.append(nr)

#     for i in range(1, len(lst)):
#         key = lst[i]
#         j = i - 1
#         while j >= 0 and lst[j] > key:
#             lst[j + 1] = lst[j]
#             j -= 1
#         lst[j+1] = key 
    

# sort(n)

# for item in lst:
#     print(item)

#62 Alpaca shapes - aac1p1

# user_input = input().split(" ")
# user_input_num = list(map(int, user_input))

# length, radius = user_input_num[0], user_input_num[1]

# def area_sq(length):
#     area_sq = length*length
#     return area_sq

# def area_c(radius):
#     area_c = radius*radius*3.14
#     return area_c

# square = area_sq(length)
# circle = area_c(radius)

# if square > circle:
#     print("SQUARE")
# else:
#     print("CIRCLE")

#63 Koala Matchmaking

# usr_input = int(input())

# def max_int(usr_input):
#     num1 = (usr_input * 2 - 1)/2
#     num2 = (usr_input * 2 - 2)/2

#     if num1.is_integer():
#         print(int(num1))

#     if num2.is_integer():
#         print(int(num2))
    
# max_int(usr_input)

#64 Monkey Shopping

# usr_inpt = input().split(" ")
# num_inpt = list(map(int, usr_inpt))

# sugar = num_inpt[0]
# sugar_need = num_inpt[1]
# toothpaste = num_inpt[2]
# toothpaste_need = num_inpt[3]

# if sugar_need > sugar and toothpaste_need > toothpaste:
#     print("Go to the department store")

# elif sugar_need > sugar: 
#     print("Go to the grocery store")

# elif toothpaste_need > toothpaste:
#     print("Go to the pharmacy")

# else:
#     print("Stay home")

# 65 Bamboo cookies aac5p1

# n = int(input())
# cookies = input().split(" ")
# int_cookies = list(map(int, cookies))

# counter = 0
# i = 0

# while i < len(int_cookies)-1:
#     j=i+1
#     while int_cookies[i] > 0 and j < len(int_cookies):
#         if int_cookies[j] > 0 and (int_cookies[i] + int_cookies[j]) % 2 == 0:
#             counter += 1
#             int_cookies[j] = 0
#             int_cookies[i] = 0
#             break
#         else:
#             j += 1
#     i += 1

# print(counter)

#66 Squirrnect
# n = int(input())

# dimensions = []
# for _ in range(n):
#     line = input().split(" ")
#     dimensions.append(list(map(int, line)))

# output = []
# for w, h in dimensions:
#     if w < 4 and h < 4:
#         output.append("bad")
#     elif w == 1:
#         output.append("bad")
#     elif h == 1 and w < 7:
#         output.append("bad")
#     else:
#         output.append("good")

# print("\n".join(output))

#67 Darcy's debilitating demands ac19p1
# def read_input() -> list:
#     T = int(input())

#     sets = []
    
#     for _ in range(T):
#         subsets = []
#         for _ in range(4):
#             num = int(input())
#             subsets.append(num)
        
#         sets.append(subsets)
    
#     return sets

# def sum_to_n(set):
#     N, A, B, C = set[0], set[1], set[2], set[3]

#     if C >= N:
#         return [0, 0, N]
#     elif B + C >= N:
#         return [0, N-C, C]
#     elif A + B + C >= N:
#         return [N - B - C, B, C]
    
#     return [-1]

# user_input = read_input()

# for input in user_input:
#     results = sum_to_n(input)
#     results_str = (str(num) for num in results)
#     print(' '.join(results_str))




# -------------------------------------
# 68 Appleby Contest '20 P1 - Terrific Triangles ac20p1

# def read_input():

#     usr_inpt = int(input())

#     data = []
#     for _ in range(usr_inpt):
#         inpt = input().split(" ")
#         int_inpt = list(map(int, inpt))
#         data.append(int_inpt)

#     return data

# def type_triangle(data):
    
#     type_tri = []

#     for i in range(len(data)):
#         a, b, c = sorted(data[i])
#         if c**2 == (a**2 + b**2):
#             type_tri.append("R")
#         elif c**2 < (a**2 + b**2):
#             type_tri.append("A")
#         else:
#             type_tri.append("O")
#     return type_tri

# input_data = read_input()
# output = type_triangle(input_data)

# for i in output:
#     print(i)

# 69 Another Contest 5 Problem 1 - Goat Fence - acc5p1
# inpt = int(input())

# outpt = 2*inpt + 2
# print(outpt)

#70 Another Contest 7 Problem 1 - Lonely Users - acc7p1
# def read_input():    
#     inpt = int(input())

#     data = []
#     for _ in range(inpt):
#         n = int(input())
#         data.append(n)
    
#     return data

# def calculate_friends(data):
#     friends = []
#     for i in range(len(data)):
#         if data[i] == 2:
#             friends.append(2)
#         else:
#             friend_nr = data[i] - 1
#             friends.append(friend_nr)
#     return friends

# inpt = read_input()
# friends = calculate_friends(inpt)

# for f in friends:
#     print(f)


# ---------------------------------------------
#71 DMOJ problem crci06p1, Bard

# def find_all_song_knowers(number_of_villagers, evening_data):
#     all_songs = set()
#     villagers = {i:set() for i in range(1, number_of_villagers + 1)} 

#     for evening in evening_data:
#         present_villagers = evening[1:]
#         if 1 in present_villagers:
#             new_song = len(all_songs) + 1
#             all_songs.add(new_song)

#             for villager in present_villagers:
#                 villagers[villager].add(new_song)
#         else:
#             shared_songs = set()
#             for villager in present_villagers:
#                 shared_songs.update(villagers[villager])
#             for villager in present_villagers:
#                 villagers[villager].update(shared_songs)

#     know_all_songs = sorted([villager for villager, songs in villagers.items() if songs == all_songs])
    
#     return know_all_songs

# number_of_villagers = int(input())
# number_of_evenings = int(input())

# evening_data = []

# for _ in range(number_of_evenings):
#     data = list(map(int, input().split()))
#     evening_data.append(data)

# result = find_all_song_knowers(number_of_villagers, evening_data)
# for villager in result:
#     print(villager)



# ------------------------------------
#72 DMOJ problem dmopc19c5p1, Conspicuous Cryptic Checklist
# data = list(map(int, input().split()))

# number_of_items, number_of_assignments = data

# tzak_items = set()
# for _ in range(number_of_items):
#     item = input().strip()
#     tzak_items.add(item)


# completed_assignments = 0
# for _ in range(number_of_assignments):
#     required_items = int(input())
#     required_item_set = set()

#     for _ in range(required_items):
#         required_item_name = input().strip()
#         required_item_set.add(required_item_name)

#     if required_item_set <= tzak_items:
#         completed_assignments += 1

# print(completed_assignments)



# --------------------------------
# 73 DMOJ problem coci15c2p1, Marko
# number_of_words = int(input())
# lst_of_words = []

# for i in range(number_of_words):
#     word = input()
#     lst_of_words.append(word)

# t9_input = input()

# t9_map = {
#     'a': '2', 'b': '2', 'c': '2',
#     'd': '3', 'e': '3', 'f': '3',
#     'g': '4', 'h': '4', 'i': '4',
#     'j': '5', 'k': '5', 'l': '5',
#     'm': '6', 'n': '6', 'o': '6',
#     'p': '7', 'q': '7', 'r': '7', 's': '7',
#     't': '8', 'u': '8', 'v': '8',
#     'w': '9', 'x': '9', 'y': '9', 'z': '9'
# }

# def convert_to_t9(lst_of_words: list[str], t9_map: dict) -> list[str]:
#     t9_list = []
#     for word in lst_of_words:
#         t9_representation = ''.join(t9_map[letter] for letter in word)
#         t9_list.append(t9_representation)
#     return t9_list
    
# t9_converted = convert_to_t9(lst_of_words, t9_map)

# matching_words = sum(1 for t9_word in t9_converted if t9_word == t9_input)

# print(matching_words)



# ---------------------------------------
# 74 DMOJ problem ccc06s2, Attack of the CipherTexts

# plaintext = input()
# ciphertext = input()
# coded_message = input()

# def decode_cipher(plaintext:str, ciphertext:str, coded_message:str) -> str:
#     mapping = {}
#     all_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
    
#     for i in range(len(plaintext)):
#         pt_char = plaintext[i]
#         ct_char = ciphertext[i]
#         mapping[ct_char] = pt_char

#     # deduce missing mapping if one character is missing
#     mapped_keys = set(mapping.keys())
#     mapped_values = set(mapping.values())

#     if len(mapped_keys) == 26:
#         missing_cipher_char = list(all_chars - mapped_keys)[0]
#         missing_plain_char = list(all_chars - mapped_values)[0]
#         mapping[missing_cipher_char] = missing_plain_char

#     # decode coded_message
#     decoded_message = []

#     for char in coded_message:
#         if char in mapping:
#             decoded_message.append(mapping[char])
#         else:
#             decoded_message.append(".")

#     return "".join(decoded_message)
           
# decoded_message = decode_cipher(plaintext, ciphertext, coded_message)
# print(decoded_message)



# ------------------------------------
# 75 DMOJ problem dmopc19c3p1, Mode Finding

# n = int(input())
# num_list = list(map(int, input().split(" ")))

# numbers = {}
# for i in range(len(num_list)):
#     number = num_list[i]
#     if not number in numbers:
#         numbers[number] = 1
#     else:
#         numbers[number] += 1

# inverted_numbers = {}
# for key in numbers:
#     value = numbers[key]
#     if not value in inverted_numbers:
#         inverted_numbers[value] = [key]
#     else:
#         inverted_numbers[value].append(key)

# max_frequency = max(inverted_numbers.keys())

# modes = sorted(inverted_numbers[max_frequency])

# print(" ".join(map(str, modes)))


# ----------------------
# 76.DMOJ problem coci14c2p2, Utrka(using a dictionary, set and list)

# First solution, doesn't pass test caases where the same name is used more than once

# number_of_contestants = int(input())

# contestants = set()
# for i in range(number_of_contestants):
#     contestant = input().strip()
#     contestants.add(contestant)

# finishers = set()
# for i in range(number_of_contestants - 1):
#     finisher = input().strip()
#     finishers.add(finisher)

# difference = contestants - finishers
# if len(difference) == 1:
#     print(difference.pop())

# second solution which accouts for duplicate names
# def find_non_finisher(registered: list[str], finished: list[str]):
#     name_counts = {}

#     for name in registered:
#         name_counts[name] = name_counts.get(name, 0) + 1

#     for name in finished:
#         name_counts[name] -= 1

#     for name, count in name_counts.items():
#         if count == 1:
#             return name    

# number_of_contestants = int(input())
# registered = [input().strip() for _ in range(number_of_contestants)]
# finished = [input().strip() for _ in range(number_of_contestants - 1)]

# print(find_non_finisher(registered, finished))



# -----------------------------------
# 77.DMOJ problem coci17c2p2, ZigZag
# number_of_words, number_of_letters = map(int, input().strip(). split(" "))

# print(number_of_words, number_of_letters) 

# words = {}
# for i in range(number_of_words):
#     word = input().strip()
#     first_letter = word[0]
#     if first_letter not in words:
#         words[first_letter] = []

#     words[first_letter].append(word)

# for key in words:
#     words[key] = sorted(words[key])

# letters = []
# for i in range(number_of_letters):
#     letter = input().strip()
#     letters.append(letter)

# # create dictinary to keep track of number of times word was used
# words_counter = {key: 0 for key in words}

# for letter in letters:
#     if letter in words:
#         index = words_counter[letter]
#         print(words[letter][index])
#         words_counter[letter] = (index + 1) % len(words[letter])


#------------------------------
# 78. DMOJ problem coci20c1p1, Patkice
# cache = {}

# def find_path_length(startRow: int, startCol: int, ocean_map: list[str]) -> int:
#     known = cache.get((startRow, startCol))
#     if known is not None: 
#         return known

#     current = ocean_map[startRow][startCol]
#     nextRow = startRow
#     nextCol = startCol
#     if current == 'x':
#         return 0
#     elif current == '.':
#         return -1
#     elif current == '>':
#         nextRow = startRow
#         nextCol = startCol + 1
#     elif current == 'v':
#         nextRow = startRow + 1
#         nextCol = startCol
#     elif current == '<':
#         nextRow = startRow
#         nextCol = startCol - 1
#     elif current == '^':
#         nextRow = startRow - 1
#         nextCol = startCol
#     else:
#         return -1

#     nextPathLen = find_path_length(nextRow, nextCol, ocean_map)
#     cache[(nextRow, nextCol)] = nextPathLen

#     if nextPathLen == -1:
#         return -1

#     return nextPathLen + 1

# rows, col = map(int, input().split(' '))

# matrix = [input().strip() for _ in range(rows)]

# #find starting and ending points
# start = None
# for i in range(rows):
#     for j in range(col):
#         if matrix[i][j] == 'o':
#             start = (i, j)
#             break

# path_lengths = {}
# N_length = find_path_length(start[0] - 1, start[1], matrix)
# if N_length >= 0:
#     path_lengths['N'] = N_length
# E_length = find_path_length(start[0], start[1] + 1, matrix)
# if E_length >= 0:
#     path_lengths['E'] = E_length
# S_length = find_path_length(start[0] + 1, start[1], matrix)
# if S_length >= 0:
#     path_lengths['S'] = S_length
# W_length = find_path_length(start[0], start[1] - 1, matrix)
# if W_length >= 0:
#     path_lengths['W'] = W_length

# if len(path_lengths) == 0:
#     print(':(')
# else:
#     min_path = min(path_lengths.values())
#     min_keys = []
#     for key, value in path_lengths.items():
#         if value == min_path:
#             min_keys.append(key)
    
#     answer = min(min_keys)
#     print(f':)\n{answer}')


# ---------------------------------------------
# 79. DMOJ problem ccc09j2, Old Fishin’ Hole


# trout_pts = int(input())
# pike_pts = int(input())
# pickerel_pts = int(input())
# max_pts = int(input())

# total_combinations = 0

# for trout_count in range(max_pts // trout_pts + 1):
#     for pike_count in range(max_pts // pike_pts + 1):
#         for pickerel_count in range(max_pts // pickerel_pts + 1):
#             total_pts = ((trout_count * trout_pts) +
#                         (pike_count * pike_pts) +
#                         (pickerel_count * pickerel_pts))

#             if total_pts <= max_pts and (trout_count + pike_count + pickerel_count > 0):
#                 print(f'{trout_count} Brown Trout, {pike_count} Northern Pike, {pickerel_count} Yellow Pickerel')
#                 total_combinations += 1

# print(f'Number of ways to catch fish: {total_combinations}')


# --------------------------------------------
# 80. Another Contest 8 Problem 1 - Trash Push acc8p1
# T = int(input())

# data = []
# for _ in range(T):
#     N, K = list(map(int, input().split()))
#     if N % K  != 0:
#         data.append(N//K + 1)
#     else:    
#         answer = N // K
#         data.append(answer)

# for d in data:
#     print(d)


# ---------------------------------------------
# 81. Another Contest 8 Problem 2 - Unnecessary Trash Push - acc8p2

# nr_test_cases = int(input())

# trash_pushes = []
# for _ in range(nr_test_cases):
#     N, K = list(map(int, input().split()))
#     trash_daily = list(map(int, input().split()))

#     nr_of_trash_pushes = 0
#     leftovers = 0

#     for i in range(N):
#         leftovers += trash_daily[i]
#         if leftovers >= K:
#             nr_of_trash_pushes += 1
#             leftovers = 0

#     trash_pushes.append(nr_of_trash_pushes)


# for p in trash_pushes:
#     print(p)



# --------------------------------------------
# 82. DMOJ problem ecoo16r1p2, Spindie
# def is_possible_result(integers: list[int]) -> set[int]:
#     twoIntegersCombinations = set()
#     for i1 in range(len(integers)):
#         n1 = integers[i1]
#         for i2 in range(i1, len(integers)):
#             n2 = integers[i2]
#             twoIntegersCombinations.add(n1 * n2)
#             twoIntegersCombinations.add(n1 + n2)
        
#     threeIntegersCombinations = set()
#     for n in integers:
#         for combination in twoIntegersCombinations:
#             threeIntegersCombinations.add(n * combination)
#             threeIntegersCombinations.add(n + combination)
#     return threeIntegersCombinations
            
# input_sets = 10

# result = []

# for _ in range(input_sets):
#     n = int(input())
#     integers = list(set(map(int, input().split())))
#     targets = list(map(int, input().split()))

#     combinations = is_possible_result(integers)
#     current_result = []
#     for target in targets:
#         possible = 'T' if target in combinations else 'F'
#         current_result.append(possible)

#     result.append("".join(current_result))
                
# print("\n".join(result))


# -------------------------------------------
#83.  DMOJ problem acc9p1 Another Contest 9 Problem 1 - Black Room Boy
# nr_test_cases = int(input())

# answers = []
# for test_case in range(nr_test_cases):
#     dimensions = set()
#     data = list(map(int, input().split()))

#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             dimensions.add((data[i] + data[j], sum(data) - (data[i] + data[j])))

#     sorted_dimensions = sorted(dimensions)
#     answers.append((len(dimensions), sorted_dimensions))

# for number_of_dimensions, dimensions in answers:
#     print(number_of_dimensions)
#     for a,b in dimensions:
#         print(a,b)


# -------------------------------------------
#84. DMOJ problem acmtryouts0a ACM U of T Tryouts C0 A - Max Flow

# t = int(input()) # number of test cases

# answers = []
# for _ in range(t):
#     numbers = set()
#     n = int(input()) #number of integers
#     for _ in range(n):
#         num = int(input())
#         numbers.add(num) 
    
#     max_num = max(numbers)
#     answers.append(max_num)

# for answer in answers:
#     print(answer)


# -------------------------------------------
#85. DMOJ problem acmtryouts1a ACM U of T Tryouts C1 A - Rock Paper Scissors Fox

# n = int(input())

# turns = []
# for _ in range(n):
#     turn = input().strip()
#     turns.append(turn)

# answers = []
# for turn in turns:
#     if turn == "Scissors":
#         answers.append("Rock")
#     elif turn == "Rock":
#         answers.append("Paper")
#     elif turn == "Paper":
#         answers.append("Scissors")
#     elif turn == "Fox":
#         answers.append("Foxen")
#     else:
#         break

# for answer in answers:
#     print(answer)

# -------------------------------------------
#87. DMOJ problem acmtryouts3a ACM U of T Tryouts C3 A - A Research Project

# g = int(input())

# answers = []
# for _ in range(g):
#     smallest = 100
#     largest = 0
#     n = int(input())
#     scores = list(map(int, input().split()))
#     for i in range(n):
#         if scores[i] < smallest:
#             smallest = scores[i]
#         if scores[i] > largest:
#             largest = scores[i]

#     answers.append((smallest, largest))

# for answer in answers:
#     print(answer[0], answer[1])
    

# -------------------------------------------
#88. DMOJ problem acmtryouts3b ACM U of T Tryouts C3 B - A Careful Reply

# n = int(input())

# replies = []
# for _ in range(n):
#     line = input()
#     heart = line.count('<3')
#     if heart > 0:
#         reply = ' '.join(['<3'] * (heart + 1))
#     else:
#         reply = '<3'
#     replies.append(reply)      

# for reply in replies:
#     print(reply)


# -------------------------------------------
#88. DMOJ problem ahscc1p1 Arcadia Computing Contest 1 P1 - Test Anxiety

# current_score = int(input())
# nr_assignments = int(input())
# TARGET = 80

# answer = TARGET * (nr_assignments + 1) - (current_score * nr_assignments)
# if answer > 100:
#     print("-1")
# elif answer <= 0:
#     print("0")
# else: 
#     print(answer)

# -------------------------------------------
#89. DMOJ problem alphabetscore Alphabet Score

# word = input()
# alphabet_score = 0

# for letter in word:
#     alphabet_score += (ord(letter) - ord('a') + 1)

# -------------------------------------------
#90. DMOJ problem ampl2023p2 Amplitude Hackathon '23 Problem 2 - Gigatron Lag
# N = int(input())

# partition_lags = {}
# global_offset = 0
# output = []

# for i in range(N):
#     line = input().split()
#     operation = line[0]

#     if operation == "ADD":
#         p, x = int(line[1]), int(line[2])
#         if p not in partition_lags:
#             partition_lags[p] = 0
#         partition_lags[p] += x

#     elif operation == "ADDALL":
#         x = int(line[1])
#         global_offset += x
        
    
#     elif operation == "PROCESS":
#         p, x = int(line[1]), int(line[2])
#         if p not in partition_lags:
#             partition_lags[p] = 0
#         effective_lag = partition_lags[p] + global_offset
#         to_process = min(x, effective_lag)
#         partition_lags[p] -= to_process
    
#     elif operation == "PROCESSALL":
#         x = int(line[1])
#         global_offset -= x
#         if global_offset <= 0:
#             global_offset = 0
#         else:
#             for p in list(partition_lags.keys()):
#                 effective_lag = partition_lags[p] + global_offset
#                 if effective_lag <= 0:
#                     partition_lags[p] = 0
#                 else:
#                     partition_lags[p] = effective_lag - global_offset

#     elif operation == "LAG":
#         p = int(line[1])
#         effective_lag = partition_lags.get(p, 0) + global_offset
#         output.append(str(effective_lag))

#     elif operation == "MAXLAG":
#         if partition_lags:
#             max_lag = max(partition_lags.values()) + global_offset 
#         else:
#             max_lag = global_offset
#         output.append(str(max_lag))

# for o in output:
#     print(o)

# -------------------------------------------
#91. DMOJ problem ampl2023practicep1 Amplitude Hackathon '23 Practice Problem 1 - Gigatron EPS Modulo 998244353
# n = int(input())

# input = list(map(int, input().split()))

# total = 0
# for i in range(n):
#     total += input[i]

# ans = total % 998244353

# print(ans)


# -------------------------------------------
#91. DMOJ problem ampl2023practicep4 Amplitude Hackathon '23 Practice Problem 4 - Gigatron Autoscaling

# nr_requests, pods = map(int, input().split())
# MIN_PODS = 1
# MAX_PODS = 1024

# lst = []
# for _ in range(nr_requests):
#     line = input().split()
#     operation = line[0]
#     x = int(line[1])

#     if operation == "INC":
#         pods += x
#         if pods > MAX_PODS:
#             pods = 1024
#         lst.append(pods)
#     elif operation == "DEC":
#         pods -= x
#         if pods < MIN_PODS:
#             pods = 1https://dmoj.ca/problem/ampl2024sp1
#         lst.append(pods)


# for l in lst:
#     print(l)
        

# -------------------------------------------
#92. DMOJ problem 2024sp1 Amplitude Hackathon Summer '24 Problem 1 - Is Jeffrey in the Office?

# day = input()

# if day == 'Saturday' or day == 'Sunday':
#     print('NO')
# else:
#     print('YES')

# -------------------------------------------
#93. DMOJ problem ampl2024sp2 Amplitude Hackathon Summer '24 Problem 2 - Feature Requests

# n = int(input())

# feature_counts = {}

# for _ in range(n):
#     line = input().split()
#     for feature in line[1:]:
#         if feature not in feature_counts:
#             feature_counts[feature] = 1
#         else:
#             feature_counts[feature] += 1

# sorted_data = sorted(feature_counts.items(), key=lambda x: (-x[1], x[0]))

# for key, value in sorted_data:
#     print(key, value)

# -------------------------------------------
#93. DMOJ problem ampl2024spracticep1 Amplitude Hackathon Summer '24 Practice Problem 1 - Jeffrey's Favorite Integer

# random_guess = 50
# low, high = 1, 100
# print(random_guess)

# while True:
#     inpt = input()
#     if inpt == 'CORRECT':
#         break
#     elif inpt == 'GREATER':
#         low = random_guess + 1
#         random_guess = (low + high)//2
#         print(random_guess)
#     elif inpt == 'LESS':
#         high = random_guess - 1
#         random_guess = (low + high)//2
#         print(random_guess)
    
# -------------------------------------------
#94. DMOJ problem ampl2024wp1 Amplitude Hackathon Winter '24 Problem 1 - Twila's Walk

# inpt = int(input())
# result = inpt ** 2
# print(result)

# -------------------------------------------
#95. DMOJ problem ampl2024wp2 Amplitude Hackathon Winter '24 Problem 2 - Fog Machine

# import math

# def max_initial_v(y0):
#     root = (-1 + math.sqrt(1+8 * y0)) / 2
#     v_init = int(root)

#     while (v_init * (v_init + 1)) // 2 >= y0:
#         v_init -= 1
    
#     return v_init

# y0 = int(input())
# print(max_initial_v(y0))

# -------------------------------------------
# 96. DMOJ problem aplusb, A plus B

# n = int(input())

# answ = []
# for _ in range(n):
#     line = list(map(int, input().split()))
#     x, y = line[0], line[1]

#     answ.append(x + y)

# for a in answ:
#     print(a)

# -------------------------------------------
# 96. DMOJ problem art0, Art Academy 0: Prologue

# n = int(input())
# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# result = []
# for _ in range(n):
#     output = []
#     word = input().upper()
#     for i in range(len(word)):
#         if word[i] == "A":
#             output.append("Hi! ")
#         if word[i] == "E":
#             output.append("Bye! ")
#         if word[i] == "I":
#             output.append("How are you? ")
#         if word[i] == "O":
#             output.append("Follow me! ")
#         if word[i] == "U":
#             output.append("Help! ")
#         if word[i] in numbers:
#             output.append("Yes! ")
#         else:
#             pass
#     output_str = ''.join(output)
#     result.append(output_str)

# [print(r) for r in result]

# -------------------------------------------
# 97. DMOJ problem avatarearth, PEG Test '14 - Earth

# boulder = list(map(int, input().split()))
# bx, by = boulder[0], boulder[1]

# cage = list(map(int, input().split()))

# cx1, cy1, cx2, cy2 = cage[0], cage[1], cage[2], cage[3]

# if  cx1<= bx <= cx2 and cy1 <= by <= cy2:
#     print("Yes")
# else:
#     print("No") 

# -------------------------------------------
# 98. DMOJ problem avatarwater, PEG Test '14 - Water

# jars = []
# for _ in range(3):
#     j = int(input())
#     jars.append(j)

# fish = max(jars) - min(jars)
# print(fish)

# -------------------------------------------
# 99. DMOJ problem bf1, List Minimum - 2 solutions, one straghtforward, one through sort

# n = int(input())

# lst = []
# for _ in range(n):
#     nr = int(input())
#     lst.append(nr)

# minimums = []
# while len(lst) > 0:
#     minimum = min(lst)
#     minimums.append(minimum)
#     min_index = lst.index(minimum)
#     lst.pop(min_index)

# lst.sort()
        
# [print(l) for l in lst]

# -------------------------------------------
# 100. DMOJ problem bf1easy, List Minimum (Easy)

# n = int(input())

# i = 1
# while i < n:
#     print(i, end=' ')
#     i += 1

# print(n)


# -------------------------------------------
# ??. DMOJ problem cco96p2, SafeBreaker

