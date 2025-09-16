import heapq
import MazeState
from MazeUtil import MazeUtil


class Heuristic():
    def __init__(self, maze):
        self.maze = maze

    def isItPartOfExploredList(self, exploredStates, state):
        for s in exploredStates:
            if s.x == state.x and s.y == state.y:
                return True
        return False

    def constructPath(self, state: MazeState):
        pathCoordinates = []
        s = state
        s.partOfPath = True
        pathCoordinates.append((s.x, s.y))
        while s.parent is not None: 
            s = s.parent
            s.partOfPath = True
            pathCoordinates.append((s.x, s.y))
        return pathCoordinates    
        
    def initializeMaze(self):
        for r in self.maze.states:
            for c in r:
                c.parent = None
                c.actualCostFromStart = 0
                c.heuristicCostToGoal = 0
                c.partOfPath = False

    def findPath(self, startPoint, goal): 
        ##print(heapq.heappop(customer))
        self.initializeMaze()
        util = MazeUtil()
        statesToExplore = []
        #heapq.heapify(statesToExplore)
        startPoint.parent = None
        startPoint.actualCostFromStart = 0
        startPoint.heuristicCostToGoal = util.getManhattanDist(startPoint, goal)
        heapq.heappush(statesToExplore, (startPoint.heuristicCostToGoal, startPoint)) 
        exploredStates = []
        while len(statesToExplore) > 0:
            currState = heapq.heappop(statesToExplore)[1]
            if currState.x == goal.x and currState.y == goal.y:
                return self.constructPath(currState)
            frontiers = self.maze.getFrontiers(currState)
            exploredStates.append(currState)
            for f in frontiers:
                if self.isItPartOfExploredList(exploredStates, f):
                    continue 
                f.parent = currState
                f.actualCostFromStart = currState.actualCostFromStart + 1
                f.heuristicCostToGoal = util.getManhattanDist(f, goal)
                #if f.heuristicCostToGoal > currState.heuristicCostToGoal:
                    #continue ##not a valid path
                heapq.heappush(statesToExplore, (f.heuristicCostToGoal, f))
        return None #No path found   


