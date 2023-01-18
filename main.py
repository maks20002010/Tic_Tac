board = [field for field in range(1,10)]


def move_board(): #Функция отображении доски
    print("-------------")
    for i in range(3):
        print(f"| {board[i * 3]} | {board[i * 3 + 1]} | {board[i * 3 + 2]} |")
    print("-------------")

def motion_input(player): #Ходы игроков
    while True:
        motion = input("Введите номер поля:")
        if motion.isdigit() and int(motion) <= 9:
            motion = int(motion)
            if motion in board:
                board[motion - 1] = player
                break
            else:
                print("Данное поле уже занято")
            continue
        else:
            print("Извините, такого поля не существует")

def check_win(): #Проверка на выйгрышные комбинации
    win_combs = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
    for comb in win_combs:
        if board[comb[0] - 1] == board[comb[1] - 1] == board[comb[2] - 1]:
            print(f"Игрок {player} выйграл!")
            return True



count = 0
while True:
    if count % 2 == 0:
        player = "X"
    else:
        player = "0"
    print(f"Ход игрока {player}")
    move_board()
    motion_input(player)
    count += 1
    if count > 8:
        move_board()
        print("Ничья!")
        break
    if check_win():
        move_board()
        break
