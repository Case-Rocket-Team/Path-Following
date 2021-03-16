# class stores common math methods
class util: 

    @staticmethod
    def clamp(value, max, min):
        if(value < min):
            return min
        if(value > max): 
            return max
        return value
    
    #deltaT: distance between points; func: function(t), range: [0,1]
    @staticmethod
    def generateWayPoints(deltaT, func, range):
        t = range[0]
        waypoints = []
        while(t <= range[1]):
            waypoints.append([t, func(t)])
            t += deltaT
        return waypoints