# USACO 2016 January Contest, Bronze
# Problem 2. Angry Cows
def exploded_in_direction(start, bales, direction):
    radius = 1
    prev = start
    while True:
        next_ = prev
        while (
            0 <= next_ + direction < len(bales)
            and abs(bales[next_ + direction] - bales[prev]) <= radius
        ):
            next_ += direction
        
        if next_ == prev:
            break

        prev = next_
        radius += 1

    return abs(prev - start)


def exploded_num(start, bales):
    left_explos = exploded_in_direction(start, bales, -1)
    right_explos = exploded_in_direction(start, bales, 1)
    return left_explos + right_explos + 1


with open('angry.in', 'r') as input_file:
    n = int(input_file.readline().strip())
    bales = [int(input_file.readline().strip()) for _ in range(n)]

bales.sort()

max_exploded = 0

for i in range(len(bales)):
    exploded = exploded_num(i, bales)
    max_exploded = max(max_exploded, exploded)

with open('angry.out', 'w') as output_file:
    output_file.write(str(max_exploded))
