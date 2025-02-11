# USACO 2013 December Bronze Contest problem Cow Baseball.

from bisect import bisect_left, bisect_right

input_file = open('baseball.in', 'r')
output_file = open('baseball.out', 'w')

n = int(input_file.readline())

positions = []

for i in range(n):
    positions.append(int(input_file.readline()))

positions.sort()

total = 0

# [1, 6, 11, 14, 16, 18, 23]
for i in range(n):
    for j in range(i + 1, n):
        first_two_diff = positions[j] - positions[i]
        low = positions[j] + first_two_diff
        high = positions[j] + first_two_diff * 2
        left = bisect_left(positions, low)
        right = bisect_right(positions, high)
        total += right - left

output_file.write(str(total) + '\n')

input_file.close()
output_file.close()