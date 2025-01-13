
# USACO 2016 US Open Contest, Bronze
# Problem 1. Diamond Collector

# Complete search algorithm, this implementation times out in test case 9 and 10
# diamonds = []
# with open('diamond.in') as input_file:
#     number_of_diamonds, max_difference = map(int, input_file.readline().strip().split(' '))

#     for _ in range(number_of_diamonds):
#         diamond = int(input_file.readline().strip())
#         diamonds.append(diamond)

# diamonds_sorted = sorted(diamonds)


# max_diamonds_counter = 0
# for i in range(len(diamonds_sorted)):
#     range_list = list(range(diamonds_sorted[i], diamonds_sorted[i] + max_difference + 1))
    

#     numbers_filtered = [diamond for diamond in diamonds if diamond in range_list]

#     if len(numbers_filtered) > max_diamonds_counter:
#         max_diamonds_counter = len(numbers_filtered)
        

#     if diamonds_sorted[i] - max_difference >= 0:
#         range_list = list(range(diamonds_sorted[i] - max_difference, diamonds_sorted[i] + 1))
        

#         numbers_filtered = [diamond for diamond in diamonds if diamond in range_list]
#         if len(numbers_filtered) > max_diamonds_counter:
#             max_diamonds_counter = len(numbers_filtered)
            
# with open('diamond.out', 'w') as output_file:
#     output_file.write(str(max_diamonds_counter))


# this version passes all judge tests
diamonds = []
with open('diamond.in', 'r') as input_file:

    N, K = map(int, input_file.readline().strip().split())
    for _ in range(N):
        diamonds.append(int(input_file.readline().strip()))

diamonds.sort()

max_count = 0
start = 0

for end in range(len(diamonds)):
    while diamonds[end] - diamonds[start] > K:
        start += 1

    max_count = max(max_count, end - start + 1)


with open('diamond.out', 'w') as output_file:
    output_file.write(str(max_count))

