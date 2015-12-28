board = [0,1,2,3,4,5,6,7,8]
players = ['x','o']
current_player = 'x'
game_over = False

def switch_player():
    global current_player
    players.reverse()
    current_player = players[0]

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

def draw(board):
    all_played = True #start by assuming it's all been played
    for i in board:
        all_played *= is_played(i) 
    return all_played

def is_played(char):
    if type(char) is str:
        return True
    else:
        return False      

def mainloop():
    while(game_over == False):
        print_board(board)
        
        #check for win
        if(win(board)):
            print("Player {} wins!".format(current_player))
            exit()
        else:
            switch_player()
        
        #check for draw
        if(draw(board)):
            print("It's a draw!")
            exit()
        
        #continue to get input
        print("Player {} turn:".format(current_player))
        position = int(input())
        board[position] = current_player

mainloop()
