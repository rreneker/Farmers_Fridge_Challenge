from kiosk import Kiosk, DeliveryDriver
import csv

NorthKioskList = []
SouthKioskList = []

depot = Kiosk("Starting Depo","1376 W Lake Street" ,41.8851024,-87.6618988)

with open('KioskCoords.csv','rb') as csvfile:
    reader = csv.reader(csvfile,delimiter=',',quotechar='"')
    next(reader)
    for row in reader:
        if float(row[2]) >= depot.latitude:
            NorthKioskList.append(Kiosk(row[0],row[1],float(row[2]),float(row[3])))
        else:
            SouthKioskList.append(Kiosk(row[0],row[1],float(row[2]),float(row[3])))
        

routeOne = DeliveryDriver(depot)
routeTwo = DeliveryDriver(depot)

NorthKioskList.sort(key=lambda x: x.latitude, reverse=True)
SouthKioskList.sort(key=lambda x: x.latitude, reverse=True)

print len(NorthKioskList)
print len(SouthKioskList)

for stop in NorthKioskList:
    print stop.description+"|"+str(stop.latitude)+"|"+str(stop.longitude)
print "----------------"
for stop in SouthKioskList:
    print stop.description+"|"+str(stop.latitude)+"|"+str(stop.longitude)



