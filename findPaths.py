from kiosk import Kiosk
import csv

with open('KioskCoords.csv','rb') as csvfile:
    reader = csv.reader(csvfile,delimiter=',',quotechar='"')
    for row in reader:
        print ', '.join(row)

kiosks = Kiosk("home","123 Fake Street")

print kiosks.address