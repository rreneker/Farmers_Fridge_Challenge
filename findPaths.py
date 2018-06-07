from kiosk import Kiosk
import csv

kioskList = []

with open('KioskCoords.csv','rb') as csvfile:
    reader = csv.reader(csvfile,delimiter=',',quotechar='"')
    next(reader)
    for row in reader:
        kioskList.append(Kiosk(row[0],row[1],row[2],row[3]))
        

for kiosk in kioskList:
    print kiosk.description+"|"+kiosk.address+"|"+kiosk.latitude+"|"+kiosk.longitude+"|"+str(kiosk.visited)