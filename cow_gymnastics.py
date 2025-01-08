# In order to improve their physical fitness, the cows have taken up gymnastics! Farmer John designates his favorite cow Bessie to coach the N other cows and to assess their progress as they learn various gymnastic skills.

# In each of K
# practice sessions (1≤K≤10), Bessie ranks the N cows according to their performance (1≤N≤20

# ). Afterward, she is curious about the consistency in these rankings. A pair of two distinct cows is consistent if one cow did better than the other one in every practice session.

# Help Bessie compute the total number of consistent pairs.

# INPUT FORMAT (file gymnastics.in):
# The first line of the input file contains two positive integers K
# and N. The next K lines will each contain the integers 1…N in some order, indicating the rankings of the cows (cows are identified by the numbers 1…N). If A appears before B in one of these lines, that means cow A did better than cow B
# .

# OUTPUT FORMAT (file gymnastics.out):
# Output, on a single line, the number of consistent pairs.

# SAMPLE INPUT:

# 3 4
# 4 1 2 3
# 4 1 3 2
# 4 2 1 3

# SAMPLE OUTPUT:

# 4

# The consistent pairs of cows are (1,4), (2,4), (3,4), and (1,3)

# sequences = []

# with open('gymnastics.in', 'r') as input_file:
#     num_lines, cows = map(int, input_file.readline().strip().split())  # Read first line with num_lines and cows

#     for _ in range(num_lines):  # Read the next num_lines lines from the file
#         line = input_file.readline().strip()  # Read the line and strip whitespace
#         sequence = list(map(int, line.split()))  # Convert line to a list of integers
#         sequences.append(sequence)  # Append the sequence to the list

# print(sequences)  # Debug: Check the parsed input


sequences = []

with open('gymnastics.in', 'r') as input_file:
    num_lines, cows = map(int, input_file.readline().strip().split())

    for _ in range(num_lines):
        line = input_file.readline().strip()
        sequence = list(map(int, line.split()))
        sequences.append(sequence)

def find_consistent_pairs(sequences):
    n = len(sequences[0])
    elements = sequences[0]
    index_dicts = []

    for seq in sequences:
        index_dict = {value: i for i, value in enumerate(seq)}
        index_dicts.append(index_dict)

    consistent_pairs = 0

    for i in range(n):
        for j in range(i + 1, n):
            a, b = elements[i], elements[j]
            is_consistent = all(index_dict[a] < index_dict[b] for index_dict in index_dicts)
            if is_consistent:
                consistent_pairs += 1
    
    return consistent_pairs

consistent_pairs = find_consistent_pairs(sequences)

with open('gymnastics.out', 'w') as output_file:
    output_file.write(str(consistent_pairs))

