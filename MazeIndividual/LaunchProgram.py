import Maze as ma
import Heuristic as h

def main(): 
    m = ma.Maze(4,4,2)
    start = (0, 0)
    goal = (3, 3)
    print("Maze Representation\n") 
    m.printMaze()
    print("Heuristic based search from starting point ")
    ha = h.Heuristic(m)
    ha.findPath(m.states[start[0]][start[1]], m.states[goal[0]][goal[1]])
    m.printMaze()
    
if __name__ == "__main__":
    main()