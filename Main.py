#IMPORTS
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math
#homemade shit
from Path import Path
from util import util

def main():
    print('initializing')
    #Constant Speed
    speed = 0.1
    direction = 0
    local = [-0.1,-0.1]
    coordsx = []
    coordsy = []
    #initialize w/ set of waypoints
    waypoints = util.generateWayPoints(1, (lambda x: 5*math.sin(x)), [0,10])
    path = Path(waypoints, 10)
    pathX = []
    pathY = []
    for point in waypoints:
        pathX.append(point[0])
        pathY.append(point[1])
    
    itter = 0
    while(not path.isEndOfPath(local)):
        itter += 1
        coordsx.append(local[0])
        coordsy.append(local[1])
        waypoint = path.getWaypoint(local)
        #calculate heading
        direction = path.getHeading(waypoint[0]-local[0], waypoint[1] - local[1])
        #calculate new position
        local = [local[0] + speed * math.cos(direction), local[1] + speed * math.sin(direction)]
    plt.plot(coordsx, coordsy, label = "Path")
    plt.scatter(pathX, pathY, label = "waypoints", color = '#88c999')
    plt.xlabel("X(m)")
    plt.ylabel("Y(m)")
    plt.title("Path Pursuit Algorithm")
    plt.legend()
    plt.show()
main()