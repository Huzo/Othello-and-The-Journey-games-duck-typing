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
# Name : Huzeyfe KIRAN
# Student ID : 1155104019
# Email Addr : 1155104019@link.cuhk.edu.hk
from Player import Player

class Human(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def nextMove(self,board):
        validMove = False
        while validMove == False:
            validMove = False
            inp = input("Type the row and col to put the disc:")
            l = inp.split(' ')

            #check if input is valid
            if(len(l) != 2):
                validMove = False
            else:
                l[0] = int(l[0]) - 1
                l[1] = int(l[1]) - 1
                if(l[0] < 0 or l[0] > 7 or l[1] <0 or l[1] > 7):
                    validMove = False
                elif(board[l[0]][l[1]] != ' '):
                    validMove = False
                else:
                    if(self.checkFlip(board, l) == False):
                        validMove = False
                    else:
                        validMove = True
            if(validMove == False):
                print("Invalid Input")
                print("Player %s's turn." % self.playerSymbol)
        return [l[0], l[1]]

    def checkFlip(self,board, move):
        # checks if the move is valid
        if(self.playerSymbol == 'O'):
            anti_symbol = 'X'
        else:
            anti_symbol = 'O'
        symbol = self.playerSymbol
        m = move[0]
        n = move[1]
        while(m <= 6 and board[m+1][n] == anti_symbol):
            m = m + 1
            if(m + 1 <= 7 and board[m+1][n] == symbol):
                return True
        m = move[0]
        while(m >= 1 and board[m-1][n] == anti_symbol):
            m = m - 1
            if(m - 1 >= 0 and board[m-1][n] == symbol):
                return True
        m = move[0]
        while(n <= 6 and board[m][n+1] == anti_symbol):
            n = n + 1
            if(n + 1 <= 7 and board[m][n+1] == symbol):
                return True
        n = move[1]
        while(n >= 1 and board[m][n-1] == anti_symbol):
            n = n - 1
            if(n - 1 >= 0 and board[m][n-1] == symbol):
                return True
        n = move[1]
        while(m <= 6 and n <= 6 and board[m+1][n+1] == anti_symbol):
            m = m + 1
            n = n + 1
            if(m + 1 <= 7 and n + 1 <= 7 and board[m+1][n+1] == symbol):
                return True
        m = move[0]
        n = move[1]
        while(m >= 1 and n <= 6 and board[m-1][n+1] == anti_symbol):
            m = m - 1
            n = n + 1
            if(m - 1 >= 0 and n + 1 <= 7 and board[m-1][n+1] == symbol):
                return True
        m = move[0]
        n = move[1]
        while(m <= 6 and n >= 1 and board[m+1][n-1] == anti_symbol):
            m = m + 1
            n = n - 1
            if(m + 1 <= 7 and n - 1 >= 0 and board[m+1][n-1] == symbol):
                return True
        m = move[0]
        n = move[1]
        while(m >= 1 and n >= 1 and board[m-1][n-1] == anti_symbol):
            m = m - 1
            n = n - 1
            if(m - 1 >= 1 and n - 1 >= 0 and board[m-1][n-1] == symbol):
                return True
        m = move[0]
        n = move[1]
        return False
