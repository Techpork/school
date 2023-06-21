import random

def create_board(size, num_mines):
    board = [[' ' for _ in range(size)] for _ in range(size)]
    mines = set()

    while len(mines) < num_mines:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        mines.add((x, y))
        board[x][y] = 'X'

    return board

def count_adjacent_mines(board, row, col):
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            x = row + dx
            y = col + dy
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 'X':
                count += 1
    return count

def reveal_cell(board, revealed, row, col):
    if board[row][col] == 'X':
        return False
    if revealed[row][col]:
        return True

    revealed[row][col] = True

    if board[row][col] == ' ':
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                x = row + dx
                y = col + dy
                if 0 <= x < len(board) and 0 <= y < len(board[0]):
                    reveal_cell(board, revealed, x, y)

    return True

def print_board(board, revealed):
    size = len(board)
    print('   ' + ' '.join(str(i) for i in range(size)))
    print('  +' + '-' * size * 2 + '+')
    for i in range(size):
        print(f'{i} |', end=' ')
        for j in range(size):
            if revealed[i][j]:
                if board[i][j] == 'X':
                    print('X', end=' ')
                else:
                    count = count_adjacent_mines(board, i, j)
                    print(count if count > 0 else ' ', end=' ')
            else:
                print('.', end=' ')
        print('|')
    print('  +' + '-' * size * 2 + '+')

def play_game():
    size = int(input('Enter the size of the board: max 15 '))
    num_mines = int(input('Enter the number of mines:max 15 '))

    board = create_board(size, num_mines)
    revealed = [[False for _ in range(size)] for _ in range(size)]
    game_over = False

    while not game_over:
        print_board(board, revealed)

        row = int(input('Enter the row:`1` '))
        col = int(input('Enter the column:`2` '))

        if board[row][col] == 'X':
            print('Game over! You hit a mine.')
            game_over = True
        else:
            if not reveal_cell(board, revealed, row, col):
                print('Game over! You hit a mine.')
                game_over = True
            elif all(all(revealed[i][j] or board[i][j] == 'X' for j in range(size)) for i in range(size)):
                print('Congratulations! You win!')
                game_over = True

play_game() 
