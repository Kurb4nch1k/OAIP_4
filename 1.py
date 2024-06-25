def get_possible_moves(position):
    letters = 'abcdefgh'
    numbers = '12345678'

    col = position[0]
    row = int(position[1])

    moves = []

    for i in range(-2, 3):
        for j in range(-2, 3):
            if abs(i * j) == 2:
                new_col = letters.find(col) + i
                new_row = row + j

                if 0 <= new_col < len(letters) and 0 < new_row <= len(numbers):
                    moves.append(letters[new_col] + str(new_row))

    return moves

def display_possible_moves(position, possible_moves):
    print(f'Возможные ходы коня из позиции {position}: {possible_moves}')

def main():
    position = input()
    possible_moves = get_possible_moves(position)
    display_possible_moves(position, possible_moves)

if __name__ == "__main__":
    main()
