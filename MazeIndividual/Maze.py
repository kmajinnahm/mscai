import random
import MazeState as ms
class Maze():
    def __init__(self, rows, cols, noOfBlockedCell):
        self.rows = rows
        self.cols = cols
        self.noOfBlockedCell = noOfBlockedCell
        self.states = self.generateStates()
        self.costOfThePath = 0
        self.cellsOfThePath = []
    
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
    
    def printMaze(self, printCostAndPath):
        print('-----------------')
        for r in self.states:
            print("|"+"|".join(" S " if s.isStart else " E " if s.isEnd else ' * ' if s.blocked else " - " if s.partOfPath else "   " for s in r) + "|")
            print('-----------------')
        if printCostAndPath:
            print('Cost of the Path : {0}'.format(self.costOfThePath))
            print('Path : {0}'.format(self.cellsOfThePath[::-1]))

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
    
    def resetMaze(self):
        for cell in [(x, y) for x in range(self.rows) for y in range(self.cols)]:
            c = self.states[cell[0]][cell[1]]
            c.parent = None
            c.actualCostFromStart = 0
            c.heuristicCostToGoal = 0
            c.partOfPath = False
            c.isStart = False
            c.isEnd = False
        self.costOfThePath = 0
        self.cellsOfThePath = []