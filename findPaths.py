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

def findMaxSplitDistance(KioskList, depot):
    routeOne = []
    routeTwo = []
    for i in range(1,len(KioskList)-1):
        if KioskList[i] == depot:
            routeOne = KioskList[:i+1]
            routeTwo = KioskList[i:]
            break
    routeOneCost = findTotalDistance(routeOne)
    routeTwoCost = findTotalDistance(routeTwo)
    return max(routeOneCost,routeTwoCost)

def TwoOptHelper(KioskList):
    bestPath = []
    bestPath = list(KioskList)
    bestCost = findTotalDistance(bestPath)

    improved = True
    while improved == True:
        improved = False
        for i in range(1,len(bestPath)-1):
            for j in range(i+1,len(bestPath)-1):
                tempList = list(bestPath)
                tempList[i], tempList[j] = tempList[j], tempList[i]
                tempCost = findTotalDistance(tempList)
                if tempCost < bestCost:
                    #print str(i)+" "+str(bestCost)+"|"+str(tempCost)
                    bestPath = list(tempList)
                    bestCost = tempCost
                    improved = True
                  
    return bestPath,bestCost

def TwoOpt(KioskList,depot):
    bestPath = []
    bestCost = float('inf')
        shuffle(KioskList)
        currentPath = list(KioskList)
        currentPath.insert(0,depot)
        currentPath.append(depot)
        result,cost = TwoOptHelper(currentPath)
        if cost < bestCost:
            bestPath = list(result)
            bestCost = cost
    return bestPath



KioskList = []


depot = Kiosk("Starting Depo","1376 W Lake Street Chicago, IL" ,41.8851024,-87.6618988)

with open('KioskCoords.csv','rb') as csvfile:
    reader = csv.reader(csvfile,delimiter=',',quotechar='"')
    next(reader)
    for row in reader:
        KioskList.append(Kiosk(row[0],row[1],float(row[2]),float(row[3])))
        
KioskList.append(depot)

solution = TwoOpt(KioskList,depot)

routeOne = []
routeTwo = []

for i in range(1,len(solution)-1):
    if solution[i] == depot:
        routeOne = solution[:i+1]
        routeTwo = solution[i:]
        break

print "ROUTE ONE:"
for kiosk in routeOne:
    kiosk.kioskPrint()
print "Route One Cost: "+str(findTotalDistance(routeOne))
print "-------------"
print "ROUTE TWO:"
for kiosk in routeTwo:
    kiosk.kioskPrint()
print "Route Two Cost: "+str(findTotalDistance(routeTwo))
