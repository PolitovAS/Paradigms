# Создаем доску для игры
board = [" " for _ in range(9)]

# Функция для отображения доски
def display_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")

# Функция для проверки победителя
def check_winner(player):
    # Проверяем строки, столбцы и диагонали
    for i in range(3):
        if all([board[i*3+j] == player for j in range(3)]) or all([board[i+3*j] == player for j in range(3)]):
            return True
    if all([board[i*4] == player for i in range(3)]) or all([board[2*i+2] == player for i in range(3)]):
        return True
    return False

# Функция для хода игрока
def player_move(player):
    while True:
        move = int(input(f"Player {player}, введите номер клетки для вашего хода (1-9): ")) - 1
        if move >= 0 and move < 9 and board[move] == " ":
            board[move] = player
            break
        else:
            print("Некорректный ход. Попробуйте еще раз.")

# Основной игровой цикл
def play_game():
    display_board()
    for turn in range(9):
        player = "X" if turn % 2 == 0 else "O"
        player_move(player)
        display_board()
        if check_winner(player):
            print(f"Игрок {player} победил!")
            return
    print("Ничья!")

# Запускаем игру
play_game()