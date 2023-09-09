import numpy as np
import math
from copy import copy

class Agent():
    def __init__(self, board):
        self.board = self.convertBoard(board)
        self.boardSize = len(self.board)
        self.boardWidth = math.floor(math.sqrt(self.boardSize))
    
    def run(self):
        words = open('words_alpha.txt','r')
        solutionWords = self.findSolutionWords(words)
        print(solutionWords)
        print(len(solutionWords))
    
    def findSolutionWords(self, words):
        solutionWords = []
        for word in words:
            word = word.strip()
            if self.isPlayable(0, word, -1, []):
                solutionWords.append(word)
                print("Appended " + word + ".")
        return solutionWords
    
    def isPlayable(self, location, word, charIndex, usedTiles):
        if charIndex == -1:
            for tile in range(len(self.board)):
                if self.isPlayable(tile, word, charIndex + 1, copy(usedTiles)):
                    return True
                
            return False
        else:
            if self.board[location].lower() != word[charIndex] or (location in usedTiles):
                return False
            elif charIndex == len(word) - 1:
                return True
            
            usedTiles.append(location)

            row = self.row(location)
            column = self.column(location)

            # NW
            if row - 1 > 0 and column - 1 > 0:
                if self.isPlayable(location - self.boardWidth - 1, word, charIndex + 1, copy(usedTiles)):
                    return True
            
            # N
            if row - 1 > 0:
                if self.isPlayable(location - self.boardWidth, word, charIndex + 1, copy(usedTiles)):
                    return True
                
            # NE
            if row - 1 > 0 and column + 1 <= self.boardWidth:
                if self.isPlayable(location - self.boardWidth + 1, word, charIndex + 1, copy(usedTiles)):
                    return True
            
            # W
            if column - 1 > 0:
                if self.isPlayable(location - 1, word, charIndex + 1, copy(usedTiles)):
                    return True
                
            # E
            if column + 1 <= self.boardWidth:
                if self.isPlayable(location + 1, word, charIndex + 1, copy(usedTiles)):
                    return True
            
            # SW
            if row + 1 <= self.boardWidth and column - 1 > 0:
                if self.isPlayable(location + self.boardWidth - 1, word, charIndex + 1, copy(usedTiles)):
                    return True
            
            # S
            if row + 1 <= self.boardWidth:
                if self.isPlayable(location + self.boardWidth, word, charIndex + 1, copy(usedTiles)):
                    return True
                
            # SE
            if row + 1 <= self.boardWidth and column + 1 <= self.boardWidth:
                if self.isPlayable(location + self.boardWidth + 1, word, charIndex + 1, copy(usedTiles)):
                    return True

            return False
        
    def row(self, location):
        return math.floor(location / self.boardWidth) + 1
    
    def column(self, location):
        return location % self.boardWidth + 1          

    def convertBoard(self, board):
        convertedBoard = []
        for tile in range(len(board)):
            if board[tile].isupper():
                if tile + 1 < len(board) and board[tile + 1].islower():
                    convertedBoard.append(board[tile] + board[tile + 1])
                else:
                    convertedBoard.append(board[tile])
        print(convertedBoard)
        return convertedBoard
                

boggleSolver = Agent(
    "EHAWSTTIEITASTTTIAWURETBW"
)
boggleSolver.run()