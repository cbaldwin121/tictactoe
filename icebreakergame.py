""" Tic Tac Toe
----------------------------------------
"""
import random
import sys

# create the array of the spots indexed at (0-9)
board=[i for i in range(0,9)]

# creates two players
player, computer = '',''

# Corners spots- index, Center, Others on board
moves=((1,7,3,9),(5,),(2,4,6,8))

# Winner combinations
winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

# Table
tab=range(1,10)

# This function prints out the user's board
def print_board():
    x=1

    # iterate over i values total in range board
    for i in board:
        # define end value
        end = ' | '

        # if statement to determine when the board output should go to the next paragraph in the terminal
        if x%3 == 0:
            end = ' \n'

            # end is when x%3 and i is not equal to 1
            if i != 1: end+='---------\n';

        char=' '

        if i in ('X','O'): char=i;

        x+=1

        print(char,end=end)

# this function selects character- either X or O
# returns either X or O
def select_char():
    chars=('X','O')
    if random.randint(0,1) == 0:
        return chars[::-1]
    return chars

# this function determines if a player can make a certain move
# returns boolean value
def can_move(brd, player, move):
    if move in tab and brd[move-1] == move-1:
        return True
    return False

# this functions determines if a player can win
# returns boolean
def can_win(brd, player, move):
    places=[]
    x=0

    for i in brd:
        if i == player: places.append(x);
        x+=1
    win=True

    for tup in winners:
        win=True
        for ix in tup:
            if brd[ix] != player:
                win=False
                break
        if win == True:
            break

    return win

# this functions makes a players move
# returns boolean
def make_move(brd, player, move, undo=False):
    if can_move(brd, player, move):
        brd[move-1] = player
        win=can_win(brd, player, move)

        if undo:
            brd[move-1] = move-1
        return (True, win)

    return (False, False)

# this function makes the computer move
# this is where you can add more AI to make the computer a harder opponent
# returns -- make move function with the move that the computer makes
def computer_move():
    move=-1
    # If I can win, others do not matter.
    for i in range(1,10):
        if make_move(board, computer, i, True)[1]:
            move=i
            break
    if move == -1:
       # If player can win, block him.
        for i in range(1,10):
            if make_move(board, player, i, True)[1]:
                move=i
                break
    if move == -1:
        # Otherwise, try to take one of desired places.
        for tup in moves:
            for mv in tup:
                if move == -1 and can_move(board, computer, mv):
                    move=mv
                    break
    return make_move(board, computer, move)

# this determines if a space exists
def space_exist():
    return board.count('X') + board.count('O') != 9



### this is the main code that runs everytime (in the beginning)
player, computer = select_char()
print('Player is [%s] and computer is [%s]' % (player, computer))
result='%%% Deuce ! %%%'

# while loop that the game runs in
while space_exist():
    print_board()

    # Ice breaker questions to get to know the kids
    print('What is your name?', end='')
    name = str(input())
    print('Where are you zoomin from? \n', end='')
    entered = input()
    print('What is something you like in tech?', end='')
    entered = input()


    print( name + '! Welcome, what is your move [1-9]', end='')
    move = int(input())
    moved, won = make_move(board, player, move)
    if not moved:
        print(' >> Invalid number ! Try again !')
        continue
    #
    if won:
        result='*** Congratulations ! You won ! ***'
        break
    elif computer_move()[1]:
        result='=== You lose ! =='
        break

print_board()
print(result)