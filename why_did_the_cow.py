
# While the age-old question of why chickens cross roads has been addressed in great depth by the scientific community, surprisingly little has been published in the research literature on the related subject of cow crossings. Farmer John, well-aware of the importance of this issue, is thrilled when he is contacted by a local university asking for his assistance in conducting a scientific study of why cows cross roads. He eagerly volunteers to help.

# As part of the study, Farmer John has been asked to document the number of times each of his cows crosses the road. He carefully logs data about his cows' locations, making a series of N
# observations over the course of a single day. Each observation records the ID number of a cow (an integer in the range 1…10

# , since Farmer John has 10 cows), as well as which side of the road the cow is on.

# Based on the data recorded by Farmer John, please help him count the total number of confirmed crossings. A confirmed crossing occurs when a consecutive sightings of a cow place it on different sides of the road.

# INPUT FORMAT (file crossroad.in):
# The first line of input contains the number of observations, N
# , a positive integer at most 100. Each of the next N
# lines contains one observation, and consists of a cow ID number followed by its position indicated by either zero or one (zero for one side of the road, one for the other side).

# OUTPUT FORMAT (file crossroad.out):
# Please compute the total number of confirmed crossings.

# SAMPLE INPUT:

# 8
# 3 1
# 3 0
# 6 0
# 2 1
# 4 1
# 3 0
# 4 0
# 3 1

# SAMPLE OUTPUT:

# 3

# In this example, cow 3 crosses twice -- she first appears on side 1, then later appears on side 0, and then later still appears back on side 1. Cow 4 definitely crosses once. Cows 2 and 6 do not appear to cross.

# Problem credits: Brian Dean 
from collections import defaultdict

with open('crossroad.in', 'r') as input_file:
    num_lines = int(input_file.readline().strip())

    cows = defaultdict(list)

    for _ in range(num_lines):
        cow_id, state = map(int, input_file.readline().strip().split())
        key = f"cow_{cow_id}"
        cows[key].append(state)

def count_pairs(cows: dict) -> dict:
    """
    Count the number of (1, 0) pairs for each animal.

    Args:
        animals (dict): A dictionary where keys are animal IDs and values are lists of states.

    Returns:
        dict: A dictionary where keys are animal IDs and values are the count of (1, 0) pairs.
    """
    pair_counts = {}

    for cow, states in cows.items():
        count = 0
        for i in range(len(states) - 1):
            if (states[i] == 1 and states[i + 1] == 0) or (states[i] == 0 and states[i + 1] == 1):
                count += 1
        pair_counts[cow] = count
    
    return pair_counts

result_pairs = count_pairs(cows)
total_pairs = str(sum(result_pairs.values()))

with open('crossroad.out', 'w') as output_file:
    output_file.write(total_pairs)




