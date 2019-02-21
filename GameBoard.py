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

class GameBoard:
    def __init__(self):
        self.board = None

    def init_gameBoard(self):
        self.board = [[' ' for i in range(8)] for j in range(8)]
        self.board[3][4] = 'O'
        self.board[4][3] = 'O'
        self.board[3][3] = 'X'
        self.board[4][4] = 'X'

    def check_ending(self):
        #check whether the game is over or not
        #return True or False
        if(self.check_legal_move('O') == False and self.check_legal_move('X') == False):
            return True
        else:
            return False


    def check_legal_move(self,symbol):
	    #check if their is a legal move given symbol
        #return True or False
        if symbol == 'O':
            anti_symbol = 'X'
        else:
            anti_symbol = 'O'

        for i in range(0,8):
            for j in range(0,8):
                if(self.board[i][j] == ' '):
                    m = i
                    n = j
                    while(m <= 6 and self.board[m+1][n] == anti_symbol):
                        m = m + 1
                        if(m + 1 <= 7 and self.board[m+1][n] == symbol):
                            return True
                    m = i
                    while(m >= 1 and self.board[m-1][n] == anti_symbol):
                        m = m - 1
                        if(m - 1 >= 0 and self.board[m-1][n] == symbol):
                            return True
                    m = i
                    while(n <= 6 and self.board[m][n+1] == anti_symbol):
                        n = n + 1
                        if(n + 1 <= 7 and self.board[m][n+1] == symbol):
                            return True
                    n = j
                    while(n >= 1 and self.board[m][n-1] == anti_symbol):
                        n = n - 1
                        if(n - 1 >= 0 and self.board[m][n-1] == symbol):
                            return True
                    n = j
                    while(m <= 6 and n <= 6 and self.board[m+1][n+1] == anti_symbol):
                        m = m + 1
                        n = n + 1
                        if(m + 1 <= 7 and n + 1 <= 7 and self.board[m+1][n+1] == symbol):
                            return True
                    m = i
                    n = j
                    while(m >= 1 and n <= 6 and self.board[m-1][n+1] == anti_symbol):
                        m = m - 1
                        n = n + 1
                        if(m - 1 >= 0 and n + 1 <= 7 and self.board[m-1][n+1] == symbol):
                            return True
                    m = i
                    n = j
                    while(m <= 6 and n >= 1 and self.board[m+1][n-1] == anti_symbol):
                        m = m + 1
                        n = n - 1
                        if(m + 1 <= 7 and n - 1 >= 0 and self.board[m+1][n-1] == symbol):
                            return True
                    m = i
                    n = j
                    while(m >= 1 and n >= 1 and self.board[m-1][n-1] == anti_symbol):
                        m = m - 1
                        n = n - 1
                        if(m - 1 >= 1 and n - 1 >= 0 and self.board[m-1][n-1] == symbol):
                            return True
                    m = i
                    n = j
        return False

    def check_winner(self):
        #return a list[s1,s2], represent the total number for O and X
        counts = [0,0]
        for i in range(8):
            for j in range(8):
                if(self.board[i][j] == 'O'):
                    counts[0] = counts[0] + 1
                else:
                    counts[1] = counts[1] + 1
        return counts

    def execute_flip(self, pos, symbol):
        i , j = pos[0], pos[1]
        self.board[i][j] = symbol
        directions = self.find_direcion_to_flip(i, j, symbol)
        self.execute_directional_flips(i,j,directions, symbol)

    def find_direcion_to_flip(self, i, j, symbol):
        if(symbol == 'O'):
            anti_symbol = 'X'
        else:
            anti_symbol = 'O'

        directions_to_flip = []
        m = i
        n = j
        while(m <= 6 and self.board[m+1][n] == anti_symbol):
            m = m + 1
            if(m + 1 <= 7 and self.board[m+1][n] == symbol):
                directions_to_flip.append(1)
        m = i
        while(m >= 1 and self.board[m-1][n] == anti_symbol):
            m = m - 1
            if(m - 1 >= 0 and self.board[m-1][n] == symbol):
                directions_to_flip.append(2)
        m = i
        while(n <= 6 and self.board[m][n+1] == anti_symbol):
            n = n + 1
            if(n + 1 <= 7 and self.board[m][n+1] == symbol):
                directions_to_flip.append(3)
        n = j
        while(n >= 1 and self.board[m][n-1] == anti_symbol):
            n = n - 1
            if(n - 1 >= 0 and self.board[m][n-1] == symbol):
                directions_to_flip.append(4)
        n = j
        while(m <= 6 and n <= 6 and self.board[m+1][n+1] == anti_symbol):
            m = m + 1
            n = n + 1
            if(m + 1 <= 7 and n + 1 <= 7 and self.board[m+1][n+1] == symbol):
                directions_to_flip.append(5)
        m = i
        n = j
        while(m >= 1 and n <= 6 and self.board[m-1][n+1] == anti_symbol):
            m = m - 1
            n = n + 1
            if(m - 1 >= 0 and n + 1 <= 7 and self.board[m-1][n+1] == symbol):
                directions_to_flip.append(6)
        m = i
        n = j
        while(m <= 6 and n >= 1 and self.board[m+1][n-1] == anti_symbol):
            m = m + 1
            n = n - 1
            if(m + 1 <= 7 and n - 1 >= 0 and self.board[m+1][n-1] == symbol):
                directions_to_flip.append(7)
        m = i
        n = j
        while(m >= 1 and n >= 1 and self.board[m-1][n-1] == anti_symbol):
            m = m - 1
            n = n - 1
            if(m - 1 >= 1 and n - 1 >= 0 and self.board[m-1][n-1] == symbol):
                directions_to_flip.append(8)
        return directions_to_flip

    def execute_directional_flips(self,i,j,directions, symbol):
        if(symbol == 'O'):
            anti_symbol = 'X'
        else:
            anti_symbol = 'O'

        m = i
        n = j

        for z in directions:
            if(z == 1):
                while(m <= 6 and self.board[m+1][n] == anti_symbol):
                    m = m + 1
                    self.board[m][n] = symbol
                m = i
            elif(z == 2):
                while(m >= 1 and self.board[m-1][n] == anti_symbol):
                    m = m - 1
                    self.board[m][n] = symbol
                m = i
            elif(z == 3):
                while(n <= 6 and self.board[m][n+1] == anti_symbol):
                    n = n + 1
                    self.board[m][n] = symbol
                n = j
            elif (z == 4):
                while(n >= 1 and self.board[m][n-1] == anti_symbol):
                    n = n - 1
                    self.board[m][n] = symbol
                n = j
            elif (z == 5):
                while(m <= 6 and n <= 6 and self.board[m+1][n+1] == anti_symbol):
                    m = m + 1
                    n = n + 1
                    self.board[m][n] = symbol
                m = i
                n = j
            elif (z == 6):
                while(m >= 1 and n <= 6 and self.board[m-1][n+1] == anti_symbol):
                    m = m - 1
                    n = n + 1
                    self.board[m][n] = symbol
                m = i
                n = j
            elif (z == 7):
                while(m <= 6 and n >= 1 and self.board[m+1][n-1] == anti_symbol):
                    m = m + 1
                    n = n - 1
                    self.board[m][n] = symbol
                m = i
                n = j
            elif (z == 8):
                while(m >= 1 and n >= 1 and self.board[m-1][n-1] == anti_symbol):
                    m = m - 1
                    n = n - 1
                    self.board[m][n] = symbol
                m = i
                n = j



    def printGameBoard(self):
        for i in range(9):
            for j in range(9):
                if(i > 0 and j == 0):
                    print(str(i) + ' | ',end='')
                    continue
                if(i == 0 and j > 0):
                    print(str(j) + ' | ',end='')
                    continue
                print(self.board[i-1][j-1] + ' | ',end='')
            print('')
            print('-' * 35)


