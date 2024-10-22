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


#56 From 1987 to 2013 ccc13s1

# def digit_same(year) -> bool:
#     return len(set(year)) != len(year)

# input_year = int(input())
# year = str(input_year + 1)

# while digit_same(year):
#     num_year = int(year)
#     num_year += 1
#     year = str(num_year)

# print(year)

number = '762'

for digit1 in number:
    for digit2 in number:
        if digit1 == digit2:
            print(digit1, digit2)