board = [0,1,2,3,4,5,6,7,8]
player = {0:'x',1:'O'} 
game_over = False

#prints a board by taking the board list as parameter
def printboard(b):
    print("{} | {} | {}".format(b[0],b[1],b[2]))
    print("===+====+===")
    print("{} | {} | {}".format(b[3],b[4],b[5]))
    print("===+====+===")
    print("{} | {} | {}".format(b[6],b[7],b[8]))

def switchplayer(p):
    p = (p + 1) % 2 
    player = player[p] 

def mainloop():
    #let first player be x
    p = 0
    while(game_over == False):
        printboard(board) 
        print("Player {} position:".format(player))
        pos = int(input()) #get position
        board[pos] = player  
        switchplayer(p)

mainloop()
