import math

class Kiosk():
    def __init__(self,desc="",addr="",lat=0.0,longt=0.0):
        self.description = desc
        self.address = addr
        self.latitude = lat
        self.longitude = longt
        self.visited = False
    
    def visit(self):
        self.visited = True

class DeliveryDriver():
    def __init__(self,k = Kiosk()):
        self.stops = []
        self.stops.append(k)
        self.cost = 0

    def addStop(self,kiosk):
        
        kiosk.visit()
        self.cost = self.cost + findDistance(kiosk,self.stops[-1])
        self.stops.append(kiosk)


def findDistance(next,prev):
    lat_diff = abs(next.latitude - prev.latitude)
    long_diff = abs(next.longitude - prev.longitude)

    cost = math.sqrt((lat_diff ** 2)+(long_diff ** 2))

    return cost