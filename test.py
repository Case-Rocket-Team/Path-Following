from Path import Path
from util import util
import math

waypoints = util.generateWayPoints(0.1, (lambda x: x*x), [0, 10])
print(waypoints)
'''
path = Path([[0,0],[1,1], [2,2], [3,3], [4,4]], 10)

var = path.getWaypoint([-1,-1])

print(path.getHeading(1, -1))
'''