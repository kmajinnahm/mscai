class MazeUtil():
    def getManhattanDist(self, currentState, goalState):
        return abs(currentState.x - goalState.x) + abs(currentState.y - goalState.y)