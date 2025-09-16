import Maze as ma
import Heuristic as h
m = ma.Maze(4,4,2)
m.printMaze()
# f = m.getFrontiers(m.states[2][2])
# for s in f:
#     print(str(s.x) + ','+ str(s.y))
h = h.Heuristic(m)
h.findPath(m.states[0][0], m.states[3][3])
m.printMaze()