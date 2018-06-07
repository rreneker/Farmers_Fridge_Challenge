from kiosk import Kiosk, DeliveryDriver
import csv

kioskList = []

depot = Kiosk("Starting Depo","1376 W Lake Street" ,41.8851024,-87.6618988)

with open('KioskCoords.csv','rb') as csvfile:
    reader = csv.reader(csvfile,delimiter=',',quotechar='"')
    next(reader)
    for row in reader:
        kioskList.append(Kiosk(row[0],row[1],float(row[2]),float(row[3])))

routeOne = DeliveryDriver(depot)
routeTwo = DeliveryDriver(depot)

routeOne.addStop(kioskList[0])
print routeOne.cost

for kiosk in kioskList:
    print kiosk.description+"|"+kiosk.address+"|"+str(kiosk.latitude)+"|"+str(kiosk.longitude)+"|"+str(kiosk.visited)