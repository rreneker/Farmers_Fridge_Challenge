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
        self.stops.append(kiosk)
        kiosk.visit()