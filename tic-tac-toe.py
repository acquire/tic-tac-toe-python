board = [0,1,2,3,4,5,6,7,8]
players = ['x','o'] 
currentPlayer = 'x'
game_over = False

def switchplayer():
    global currentPlayer
    index = players.index(currentPlayer)
    index = (index + 1) % 2 
    currentPlayer = players[index] 

#prints a board by taking the board list as parameter
def printboard(b):
    print(" {} | {} | {}".format(b[0],b[1],b[2]))
    print("===+===+===")
    print(" {} | {} | {}".format(b[3],b[4],b[5]))
    print("===+===+===")
    print(" {} | {} | {}".format(b[6],b[7],b[8]))

def mainloop():
    while(game_over == False):
        printboard(board) 
        print("Player {} turn:".format(currentPlayer))
        position = int(input()) 
        board[position] = currentPlayer 
        switchplayer()

mainloop()
