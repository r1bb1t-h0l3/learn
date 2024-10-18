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

num_days = int(input())
net_change = input()

current_row_num = 0
grid = [['.']*num_days]
for day in range(num_days):
    if net_change[day] == "+":
        grid[current_row_num][day] = "/"
    elif net_change[day]  == "-":
        grid[current_row_num][day] = "\\"
    elif net_change[day] == "=":
        grid[current_row_num][day] = "_"
    if day + 1 < num_days:
        if net_change[day] == "+" and net_change[day + 1] == "+":
            current_row_num -= 1
        elif net_change[day] == "-" and net_change[day + 1] == "-":
            current_row_num += 1
        elif net_change[day] == "+" and net_change[day + 1] == "=":
            current_row_num -= 1
        elif net_change[day] == "=" and net_change[day + 1] == "-":
            current_row_num += 1    
        if current_row_num < 0:
            grid.insert(0, ['.']*num_days) 
            current_row_num = 0
        elif current_row_num >= len(grid):
            grid.append(["."]*num_days)

str_grid = list(map(''.join, grid))
str_grid = [ st.strip() for st in str_grid ]
print("\n".join(str_grid))




