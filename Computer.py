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

class Computer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def nextMove(self, board):
        for i in range(0,8):
        	for j in range(0,8):
        		if(board[i][j] == ' ' and self.checkFlip(board, [i,j]) == True):
        			return [i,j]

    def checkFlip(self,board, move):
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