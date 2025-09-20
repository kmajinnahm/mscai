class MazeState():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.blocked = False
        self.parent = None
        self.actualCostFromStart = 0
        self.heuristicCostToGoal = 0
        self.partOfPath = False
        self.isStart = False
        self.isEnd = False

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return self.x < other.x or self.y < other.y
    
    def __gt__(self, other):
        return self.x > other.x or self.y > other.y
    
    def __le__(self, other):
        return self.x <= other.x or self.y <= other.y
    
    def __ge__(self, other):
        return self.x > other.x or self.y >= other.y
