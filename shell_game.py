# USACO 2019 January Bronze Contest problem Shell Game

with open('shell.in', 'r') as input_file:
    number_of_swaps = int(input_file.readline().strip())

    swaps_and_guesses = [tuple(map(int, input_file.readline().split())) for _ in range(number_of_swaps)]

def simulate_game(starting_position, swaps_and_guesses):
    pebble_position = starting_position
    score = 0

    for a, b, g in swaps_and_guesses:
        if pebble_position == a:
            pebble_position = b
        elif pebble_position == b:
            pebble_position = a

        if pebble_position == g:
            score += 1

    return score

max_score = max(simulate_game(starting_position, swaps_and_guesses) for starting_position in [1, 2, 3])

with open('shell.out', 'w') as output_file:
    output_file.write(str(max_score))