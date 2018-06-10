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
    def kioskPrint(self):
        print self.description+" "+self.address



