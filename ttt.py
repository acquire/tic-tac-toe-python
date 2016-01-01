from board import Board
from players import Players

game_over = False


def win(cell):

    # check for horizontal, vertical, or diagonal win
    # cell values can be either a position or player mark

    if \
    cell[0].value == cell[1].value == cell[2].value or \
    cell[3].value == cell[4].value == cell[5].value or \
    cell[6].value == cell[7].value == cell[8].value or \
    cell[0].value == cell[3].value == cell[6].value or \
    cell[1].value == cell[4].value == cell[7].value or \
    cell[2].value == cell[5].value == cell[8].value or \
    cell[0].value == cell[4].value == cell[8].value or \
    cell[2].value == cell[4].value == cell[6].value:
        return True


def draw(board):
    all_played = True # start by assuming it's all been played
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
    players = Players()
    players.current = players.create_player('x')
    players.create_player('o')

    while game_over is False:
        board.console_print()

        # check for win
        if win(board.cells):
            print("Player {} wins!".format(players.current.mark))
            exit()
        else:
            players.switch_players()
        
        # check for draw
        if draw(board.cells):
            print("It's a draw!")
            exit()
        
        # continue to get input
        print("Player {} turn:".format(players.current.mark))
        position = int(input())
        board.mark_board(position,players.current.mark)

mainloop()
