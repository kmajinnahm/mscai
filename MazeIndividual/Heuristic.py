import heapq
import MazeState
import Maze
from MazeUtil import MazeUtil


class Heuristic():
    def __init__(self, maze: Maze):
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
        self.maze.costOfThePath = state.actualCostFromStart
        pathCoordinates.append((s.x, s.y))
        while s.parent is not None: 
            s = s.parent
            s.partOfPath = True
            pathCoordinates.append((s.x, s.y))
        self.maze.cellsOfThePath = pathCoordinates
        return pathCoordinates    

    def findPath(self, s, g): 
        startPoint = self.maze.states[s[0]][s[1]]
        goal = self.maze.states[g[0]][g[1]]
        startPoint.isStart = True
        goal.isEnd = True
        util = MazeUtil()
        statesToExplore = []
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
                heapq.heappush(statesToExplore, (f.heuristicCostToGoal, f))
        return None #No path found   


