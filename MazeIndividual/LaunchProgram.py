import Maze as ma
import Heuristic as h
from ForwardChaining import ForwardChaining

def main(): 
    m = ma.Maze(4,4,2)
    start = (0, 0)
    goal = (3, 3)
    
    print("Maze Representation") 
    m.printMaze(False)
    
    ha = h.Heuristic(m)
    ha.findPath(start, goal)

    print("Heuristic based search from starting point ")
    print('Start : {}, Goal : {}'.format(start, goal))
    m.printMaze(True)
 
    m.resetMaze()
    fc = ForwardChaining(m)
    fc.findPath(start, goal)
    print("\nForward Chaining Inference") 
    fc.printKnowledge()

if __name__ == "__main__":
    main()