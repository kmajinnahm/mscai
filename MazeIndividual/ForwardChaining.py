from Maze import Maze
class ForwardChaining():
    def __init__(self, maze: Maze):
        self.maze = maze
        self.knowledge = [] 

    def isReachable(self, x, y):
        return 0 <= x < len(self.maze.states) and 0 <= y < len(self.maze.states[0]) and not self.maze.states[x][y].blocked

    def findPath(self, start, goal): 
        # FOL facts: Reachable states
        facts = set([start])
        self.knowledge.append([f"Initial fact: Reachable{start}"])
        possibleActions = [(0,1),(0,-1),(1,0),(-1,0)]
        while True:
            new_inferred = set()
            for (x, y) in facts:
                # After performing each action apply rule: Reachable(x,y) → Reachable(neighbor)
                for dx, dy in possibleActions:
                    nx, ny = x + dx, y + dy 
                    if self.isReachable(nx, ny) and (nx, ny) not in facts:
                        new_inferred.add((nx, ny))
                        self.knowledge.append(f"Rule applied: Reachable({x},{y}) ∧ NotBlocked({nx},{ny}) → Reachable({nx},{ny})")
                        if (nx, ny) == goal:
                            self.knowledge.append(f"Goal reached: Reachable{goal}")
                            return True
            if not new_inferred:
                self.knowledge.append("No new states inferred. Goal not reachable.")
                return False
            facts.update(new_inferred)

    def printKnowledge(self):
        for step in self.knowledge:
            print(step)