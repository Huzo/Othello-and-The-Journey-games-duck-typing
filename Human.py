# CSCI3180 Principles of Programming Languages
#
# --- Declaration ---
#
# I declare that the assignment here submitted is original except for source
# material explicitly acknowledged. I also acknowledge that I am aware of
# University policy and regulations on honesty in academic work, and of the
# disciplinary guidelines and procedures applicable to breaches of such policy
# and regulations, as contained in the website
# http://www.cuhk.edu.hk/policy/academichonesty/
#
# Assignment 2
# Name : ***
# Student ID : **
# Email Addr : ***
from Player import Player

class Human(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def nextMove(self,board):
        while validMove == False:
            print("Player %s's turn.",self.symbol)
            validMove = False
            inp = input("Type the row and col to put the disc:")
            l = inp.split(' ')
            if(l[0] < 1 or l[0] > 8 or l[1] <1 or l[1] > 8):
                validMove = False
            if(board[l[0]][l[1]] != ' '):
                validMove = False
            else:
                if(checkFlip(board, l) == False):
                    validMove = False
                else:
                    validMove = True
            if(validMove == False):
                print("Invalid Input")

        return [l[0], l[1]]

    def checkFlip(self,board, move):
# to be filled
