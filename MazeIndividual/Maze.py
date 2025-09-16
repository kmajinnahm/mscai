import random
import MazeState as ms
class Maze():
    def __init__(self, rows, cols, noOfBlockedCell):
        self.rows = rows
        self.cols = cols
        self.noOfBlockedCell = noOfBlockedCell
        self.states = self.generateStates()
    
    def generateStates(self):
        states = []
        for r in range(self.rows):
            states.append([])
            for c in range(self.cols):
                states[r].append(ms.MazeState(r, c))
        for b in range(self.noOfBlockedCell):
            x = random.randint(0, self.rows-1)
            y = random.randint(0, self.cols-1)
            (states[x][y]).blocked=True
        return states
    
    def printMaze(self):
        print('----------------')
        for r in self.states:
            print("|"+"|".join('*' if s.blocked else "-" if s.partOfPath else " " for s in r) + "|")
            print('----------------')

    def getFrontiers(self, currentState):
        frontiers = []
        possiblePos = [-1, 1]
        for p in possiblePos:
            if currentState.x + p < 0 or currentState.x + p >= self.cols:
                continue
            if not (self.states[currentState.x+p][currentState.y]).blocked:
                frontiers.append(self.states[currentState.x+p][currentState.y])
        for p in possiblePos:
            if currentState.y + p < 0 or currentState.y + p >= self.rows:
                continue
            if not (self.states[currentState.x][currentState.y+p]).blocked:
                frontiers.append(self.states[currentState.x][currentState.y+p])
        return frontiers   