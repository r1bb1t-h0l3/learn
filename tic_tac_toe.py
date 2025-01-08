with open('tttt.in', 'r') as input_file:
    board = [line.strip() for line in input_file] #represent bard as list of strings
    
row_sets = [set(row) for row in board]
column_sets = [set(board[row][col] for row in range(3)) for col in range(3)]
diagonal_1 = set(board[i][i] for i in range(3))
diagonal_2 = set(board[i][2 - i] for i in range(3))

diagonal_sets = [diagonal_1, diagonal_2]

winners_single = 0
winners_pairs = 0

all_sets = row_sets + column_sets + diagonal_sets

winners1_set = set()
winners2_set = set()

for set in all_sets:
    if len(set) == 1:
        winners1_set.add(tuple(sorted(set)))
    elif len(set) == 2:
        winners2_set.add(tuple(sorted(set)))

with open('tttt.out', 'w') as output_file:
    output_file.write(f"{len(winners1_set)}\n")
    output_file.write(f"{len(winners2_set)}")
    


# from typing import List, Tuple, Set


# WIDTH = 3


# def cow_contrib(game: List[str], pts: List[Tuple[int, int]]) -> Set[str]:
# 	contained = set()
# 	for pt in pts:
# 		row = pt[0]
# 		col = pt[1]
# 		contained.add(game[row][col])
# 	return contained

# def insertToWinners(winners, cowsSet):
# 	sortedCows = tuple(sorted(cowsSet))
# 	winners[len(cowsSet)].add(sortedCows)


# with open("tttt.in") as read:
# 	board = [read.readline() for _ in range(WIDTH)]

# winners = [set() for _ in range(WIDTH + 1)]
# # Function which adds a winning team to the winners array
# insert = lambda playersSet: winners[len(playersSet)].add(tuple(sorted(playersSet)))

# # Insert all the rows
# for r in range(WIDTH):
# 	allRowCoords = [(r, c) for c in range(WIDTH)]
# 	cowsInARow = cow_contrib(board, allRowCoords)
# 	insert(cowsInARow)

# # Do the same for the columns
# for c in range(WIDTH):
# 	allColCoords = [(r, c) for r in range(WIDTH)]
# 	cowsInACol = cow_contrib(board, allColCoords)
# 	insert(cowsInACol)

# # And finally the diagonals
# insert(cow_contrib(board, [(i, i) for i in range(WIDTH)]))
# insert(cow_contrib(board, [(i, WIDTH - i - 1) for i in range(WIDTH)]))

# with open("tttt.out", "w") as written:
# 	print(len(winners[1]), file=written)
# 	print(len(winners[2]), file=written)