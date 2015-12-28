board = [0,1,2,3,4,5,6,7,8]
players = ['x','o']
current_player = 'x'
game_over = False

def switch_player():
    global current_player
    index = players.index(current_player)
    index = (index + 1) % 2
    current_player = players[index]

#prints a board by taking the board list as parameter
def print_board(b):
    print(" {} | {} | {}".format(b[0],b[1],b[2]))
    print("===+===+===")
    print(" {} | {} | {}".format(b[3],b[4],b[5]))
    print("===+===+===")
    print(" {} | {} | {}".format(b[6],b[7],b[8]))

#check for horizontal, vertical, or diagonal win
def win(b):
    if \
b[0] == b[1] == b[2] or \
b[3] == b[4] == b[5] or \
b[6] == b[7] == b[8] or \
b[0] == b[3] == b[6] or \
b[1] == b[4] == b[7] or \
b[2] == b[5] == b[8] or \
b[0] == b[4] == b[8] or \
b[2] == b[4] == b[6] :
        return True

def mainloop():
    while(game_over == False):
        print_board(board)
        if(win(board)):
            print("Player {} wins!".format(current_player))
            exit()
        else:
            switch_player()
        print("Player {} turn:".format(current_player))
        position = int(input())
        board[position] = current_player

mainloop()
