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

def mainloop():
    while(game_over == False):
        print_board(board) 
        print("Player {} turn:".format(current_player))
        position = int(input()) 
        board[position] = current_player 
        switch_player()

mainloop()
