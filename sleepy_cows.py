with open('herding.in', 'r') as input_file:
    cow_1, cow_2, cow_3 = sorted(map(int, input_file.readline().strip().split()))

print(cow_1, cow_2, cow_3)

distance_1 = cow_2 - cow_1
distance_2 = cow_3 - cow_2

print(distance_1, distance_2)
min_moves = 0
max_moves = 0

if  distance_2 == 2 or distance_1 == 2:
    min_moves = 1
elif distance_1 == 1 and distance_2 == 1:
    min_moves = 0
    max_moves = 0
else:
    min_moves = 2

gap_1 = cow_2 - cow_1 - 1
gap_2 = cow_3 - cow_2 - 1

max_moves = max(gap_1, gap_2)

print(min_moves, max_moves)
with open('herding.out', 'w') as output_file:
    output_file.write(f"{min_moves}\n")
    output_file.write(f"{max_moves}")