import numpy as np
import math

class Agent():
    def __init__(self, board):
        self.board = board
        self.boardSize = len(board)
    
    def run(self):
        words = open('words_alpha.txt','r')
        solutionWords = self.findSolutionWords(words)
        print(solutionWords)
        print(len(solutionWords))
    
    def findSolutionWords(self, words):
        solutionWords = []
        for word in words:
            word = word.strip()
            for char in word:
                for tile in self.board:
                    if char == tile.lower():
                        solutionWords.append(word)
                        print("Appended " + word + ".")
                        break
        return solutionWords



boggleSolver = Agent([
    "X"
])
boggleSolver.run()