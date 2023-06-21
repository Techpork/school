maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#']
]

def print_maze(maze, knight_pos):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if (i, j) == knight_pos:
                print('K', end=' ')
            else:
                print(cell, end=' ')
        print()

def move_knight(direction, knight_pos):
    row, col = knight_pos

    if direction == 'up':
        new_pos = (row - 1, col)
    elif direction == 'down':
        new_pos = (row + 1, col)
    elif direction == 'left':
        new_pos = (row, col - 1)
    elif direction == 'right':
        new_pos = (row, col + 1)
    else:
        return knight_pos

    if maze[new_pos[0]][new_pos[1]] != '#':
        return new_pos
    else:
        return knight_pos

def game_loop():
    knight_pos = (1, 1)  # Starting position of the knight

    while True:
        print_maze(maze, knight_pos)

        if knight_pos == (7, 7):  # Exit position
            print("Congratulations! You escaped the maze!")
            break

        direction = input("Enter your move (up/down/left/right): ")

        knight_pos = move_knight(direction, knight_pos)

        print("\n")

game_loop()
