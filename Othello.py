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

import sys
import random

from GameBoard import GameBoard
from Human import Human
from Computer import Computer

class Othello:

    def __init__(self):
        self.gameBoard = GameBoard()
        self.player1 = None
        self.player2 = None
        self.turn = 0


    def createPlayer(self, symbol, playerNum):
        if symbol == 'O':
            if playerNum == '1':
                return Human(symbol)
            else:
                return Computer(symbol)
        else:
            if playerNum == '1':
                return Human(symbol)
            else:
                return Computer(symbol)

    def startGame(self):
	    #basic logic
        self.player1 = self.createPlayer('O', choice1)
        self.player2 = self.createPlayer('X', choice2)
        self.gameBoard.init_gameBoard()
        self.gameBoard.printGameBoard()

        while not self.gameBoard.check_ending():
            current_player = [self.player1,self.player2][self.turn]
            print("Player %s's turn." % current_player.playerSymbol)

            if self.gameBoard.check_legal_move(current_player.playerSymbol):
                pos = current_player.nextMove(self.gameBoard.board)
                self.gameBoard.execute_flip(pos, current_player.playerSymbol)
            else:
                print("There is no valid move for Player %s." % current_player.playerSymbol)
            self.turn = 1 - self.turn

            self.gameBoard.printGameBoard()

        s1, s2 = self.gameBoard.check_winner()
        if s1 > s2:
            winner = 'O'  # Black
        elif s1 < s2:
            winner = 'X'  # White
        elif s1 == s2:
            winner = ' '  # Tie

        print('Count O : {}'.format(s1))
        print('Count X : {}'.format(s2))
        if winner != ' ':
            print('Player {} won!\n'.format(winner))
        else:
            print('A tie')


if __name__ == "__main__":
    print('Please choose player 1 (O):')
    print('1. Human\n2. Computer Player')
    choice1 = input('Your choice is: ')
    if(choice1 == '1'):
        print('Player O is Human.')
    else:
        print('Player O is Computer.')

    print('Please choose player 2 (X):')
    print('1. Human\n2. Computer Player')
    choice2 = input('Your choice is: ')
    if(choice2 == '1'):
        print('Player X is Human.')
    else:
        print('Player X is Computer.')

    othello = Othello()
    othello.startGame()

