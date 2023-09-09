import numpy as np
import math
from copy import copy

class Agent():
    def __init__(self, board, minimumWordLength):
        self.board = self.convertBoard(board)
        self.boardSize = len(self.board)
        self.boardWidth = math.floor(math.sqrt(self.boardSize))
        self.nonexistentLetters = self.findNonexistentLetters()
        self.minimumWordLength = minimumWordLength
    
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
            if len(word) < self.minimumWordLength:
                return False
            for char in word:
                if char in self.nonexistentLetters:
                    return False
            for tile in range(len(self.board)):
                if self.isPlayable(tile, word, charIndex + 1, copy(usedTiles)):
                    return True
                
            return False
        else:
            if len(self.board[location]) == 1:
                tileLength = 1
            else:
                tileLength = 2

            if (self.board[location].lower() != word[charIndex] or (location in usedTiles)) and not (charIndex + 1 < len(word) and self.board[location].lower() == word[charIndex] + word[charIndex + 1]):
                return False
            elif charIndex + tileLength - 1 == len(word) - 1:
                return True
            
            usedTiles.append(location)

            row = self.row(location)
            column = self.column(location)

            # NW
            if row - 1 > 0 and column - 1 > 0:
                if self.isPlayable(location - self.boardWidth - 1, word, charIndex + tileLength, copy(usedTiles)):
                    return True
            
            # N
            if row - 1 > 0:
                if self.isPlayable(location - self.boardWidth, word, charIndex + tileLength, copy(usedTiles)):
                    return True
                
            # NE
            if row - 1 > 0 and column + 1 <= self.boardWidth:
                if self.isPlayable(location - self.boardWidth + 1, word, charIndex + tileLength, copy(usedTiles)):
                    return True
            
            # W
            if column - 1 > 0:
                if self.isPlayable(location - 1, word, charIndex + tileLength, copy(usedTiles)):
                    return True
                
            # E
            if column + 1 <= self.boardWidth:
                if self.isPlayable(location + 1, word, charIndex + tileLength, copy(usedTiles)):
                    return True
            
            # SW
            if row + 1 <= self.boardWidth and column - 1 > 0:
                if self.isPlayable(location + self.boardWidth - 1, word, charIndex + tileLength, copy(usedTiles)):
                    return True
            
            # S
            if row + 1 <= self.boardWidth:
                if self.isPlayable(location + self.boardWidth, word, charIndex + tileLength, copy(usedTiles)):
                    return True
                
            # SE
            if row + 1 <= self.boardWidth and column + 1 <= self.boardWidth:
                if self.isPlayable(location + self.boardWidth + 1, word, charIndex + tileLength, copy(usedTiles)):
                    return True

            return False
    
    def findNonexistentLetters(self):
        nonexistentLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        for tile in self.board:
            for char in tile:
                if char.lower() in nonexistentLetters:
                    nonexistentLetters.remove(char.lower())
        print(nonexistentLetters)
        return nonexistentLetters
        
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
                

boggleSolver = Agent("OEBTECOUNESESAEQuSDTNNAOEN", 5)
boggleSolver.run()