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
n = int(input())

lst = []
def sort(n):
    for i in range(n):
        nr = int(input())
        lst.append(nr)

    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j+1] = key 
    

sort(n)

for item in lst:
    print(item)


