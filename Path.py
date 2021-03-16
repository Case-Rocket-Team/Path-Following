import numpy as np
import math

class Path:
    def __init__(self, way_points, max_turn):
        self.itter = 0
        self.coords = way_points
        self.MAX_TURN = max_turn
        
    def getWaypoint(self, vehicle_coords):
        #distance from vehicle to waypoint
        d1 = self.getDistance(self.coords[self.itter][0], vehicle_coords[0], self.coords[self.itter][1], vehicle_coords[1])

        #distance from current waypoint to next
        if(self.itter < len(self.coords) -1 ):
            d2 = self.getDistance(self.coords[self.itter][0], self.coords[self.itter+1][0], self.coords[self.itter][1], self.coords[self.itter+1][1])
        else:
            d2 = self.getd2()
        print(d2, self.coords[self.itter], d1, d1 < 0.4*d2 and self.itter < len(self.coords) - 1,vehicle_coords )
        if d1 < 0.4*d2 and self.itter < len(self.coords) - 1:
            #Close to waypoint, so advance to next one
            self.itter += 1
            return self.coords[self.itter]
        else:
            return self.coords[self.itter]

    def getDistance(self, x1, x2, y1, y2):
        return math.sqrt((x2-x1)**2 +(y2-y1)**2)

    def getHeading(self, deltaX, deltaY):
        angle = math.atan(deltaY/deltaX)
        if(deltaY > 0):
            if(deltaX < 0):
                angle *= -1
                angle += (3.1415)/2
        else: 
            if(deltaX < 0):
                angle += (3.1415)
            else: 
                angle = 2*(3.1415) + angle
        return angle

    def isEndOfPath(self, vehicle_coords):
        d1 = self.getDistance(self.coords[self.itter][0], vehicle_coords[0], self.coords[self.itter][1], vehicle_coords[1])
        d2 = self.getd2()
        if d1 < 0.05*d2 and self.itter == len(self.coords) - 1:
            return True
        else:
            return False
    
    def getd2(self):
        nextpoint = []
        if(self.itter < len(self.coords)-1):
            nextpoint = self.coords[self.itter+1]
        else:
            nextpoint = self.coords[self.itter - 1]
        return self.getDistance(self.coords[self.itter][0], nextpoint[0], self.coords[self.itter][1], nextpoint[1])
    