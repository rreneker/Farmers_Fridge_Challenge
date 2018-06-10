from kiosk import Kiosk
from random import shuffle
import csv, math

def findDistance(next,prev):
        lat_diff = abs(next.latitude - prev.latitude)
        long_diff = abs(next.longitude - prev.longitude)

        cost = math.sqrt((lat_diff ** 2)+(long_diff ** 2))

        return cost

def findTotalDistance(KioskList):
    cost = 0
    for i in range(1,len(KioskList)):
        cost = cost + findDistance(KioskList[i-1],KioskList[i])
    return cost

def TwoOpt(KioskList):
    bestPath = []
    bestPath = KioskList
    bestCost = findTotalDistance(bestPath)

    improved = True
    while improved == True:
        improved = False
    print "Still in Progress"
    return bestPath


KioskList = []


depot = Kiosk("Starting Depo","1376 W Lake Street" ,41.8851024,-87.6618988)

with open('KioskCoords.csv','rb') as csvfile:
    reader = csv.reader(csvfile,delimiter=',',quotechar='"')
    next(reader)
    for row in reader:
        KioskList.append(Kiosk(row[0],row[1],float(row[2]),float(row[3])))
        
KioskList.append(depot)
shuffle(KioskList)

KioskList.insert(0,depot)
KioskList.append(depot)

solution = TwoOpt(KioskList)

routeOne = []
routeTwo = []

for i in range(1,len(solution)-1):
    if solution[i] == depot:
        routeOne = solution[:i+1]
        routeTwo = solution[i:]



for kiosk in routeOne:
    kiosk.kioskPrint()
print "-------------"
for kiosk in routeTwo:
    kiosk.kioskPrint()
