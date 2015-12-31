from board import Board

players = ['x','o']
current_player = 'x'
game_over = False

def switch_player():
    global current_player
    players.reverse()
    current_player = players[0]

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
    board = Board(3)
    while(game_over == False):

        board.console_print()

        #check for win
        if(win(board.cells)):
            print("Player {} wins!".format(current_player))
            exit()
        else:
            switch_player()
        
        #check for draw
        if(draw(board.cells)):
            print("It's a draw!")
            exit()
        
        #continue to get input
        print("Player {} turn:".format(current_player))
        position = int(input())
        board.cells[position] = current_player

mainloop()
