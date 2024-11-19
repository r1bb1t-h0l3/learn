
def rows_columns_input() -> list:    
    rows_columns = input().split(" ")
    return list(map(int, rows_columns))


def seat_matrix_input(rows: int) -> list:
    seat_matrix = []
    for _ in range(rows):
        seat_matrix_input = input()
        line = []
        for char in seat_matrix_input:
            line.append(char)
        seat_matrix.append(line)
    return seat_matrix

def handshakes(seat_matrix_input: list, rows: int, cols: int) -> int:
    handshakes = 0

    for i in range(rows):
        for j in range(cols):
            current_seat = seat_matrix_input[i][j]
            if current_seat == '.':
                continue
            if j + 1 < cols and seat_matrix_input[i][j+1] == "o":
                handshakes += 1
            if j + 1 < cols and i + 1 < rows and seat_matrix_input[i+1][j+1] == "o":
                handshakes += 1
            if i + 1 < rows and seat_matrix_input[i+1][j] == "o":
                handshakes += 1
            if j - 1 >= 0 and i + 1 < rows and seat_matrix_input[i+1][j-1] == "o":
                handshakes += 1

    return handshakes

def mirko_handshakes(seat_matrix_input: list, rows: int, cols: int) -> int:
    max_handshakes = 0

    for i in range(rows):
        for j in range(cols):
            handshakes = 0
            current_seat = seat_matrix_input[i][j]
            if current_seat == 'o':
                continue
            if j + 1 < cols and seat_matrix_input[i][j+1] == "o":
                handshakes += 1
            if j + 1 < cols and i + 1 < rows and seat_matrix_input[i+1][j+1] == "o":
                handshakes += 1
            if i + 1 < rows and seat_matrix_input[i+1][j] == "o":
                handshakes += 1
            if j - 1 >= 0 and i + 1 < rows and seat_matrix_input[i+1][j-1] == "o":
                handshakes += 1
            if j - 1 >= 0 and seat_matrix_input[i][j - 1] == "o":
                handshakes += 1
            if j - 1 >= 0 and i - 1 >= 0 and seat_matrix_input[i-1][j-1] == "o":
                handshakes += 1
            if i - 1>= 0 and seat_matrix_input[i - 1][j] == "o":
                handshakes += 1
            if i - 1 >= 0 and j + 1 < cols and seat_matrix_input[i -1][j - 1] == "o":
                handshakes += 1

            if handshakes > max_handshakes:
                max_handshakes = handshakes   

    return max_handshakes

def main():
    rows, cols = rows_columns_input()

    matrix = seat_matrix_input(rows)
    print(matrix)
    
    no_mirko_hand = handshakes(matrix, rows, cols)

    mirko_hand = mirko_handshakes(matrix, rows, cols)

    if "." not in rows:
        print(no_mirko_hand)
    else:
        print(mirko_hand)

if __name__ == "__main__":
    main()
            


