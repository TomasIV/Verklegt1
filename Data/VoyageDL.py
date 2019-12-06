import csv
from Models.VoyageMODEL import Voyage

class VoyageDL:
    def __init__(self):
        pass

    def save_voyage(self, some_voyage):
        with open("CSVFiles\Voyages.csv", "a") as voyage:
            csv_writer = csv.writer(voyage, lineterminator= "\r" )
            csv_writer.writerow(some_voyage.get_voyage_attributes())

    def list_voyages(self):
        list_aircraftType = []
        with open('CSVFiles\Voyages.csv', 'r') as csvfile:
            reader = csv.Dictreader(csvfile)
            for row in reader: 
                voyage = Voyage(row['planeTypeId'], row['manufacturer'], row['model'],row['capacity'], row['emptyWheight'], row['maxTakeoffWeight'], row['unitThrust'], row['serviceCeiling'], row['length'], row['height'], row['wingspan'])
                list_aircraftType.append(voyage)
            #þarf að laga // vantar enþá nokkrar upplýsingar 
            #return list_aircraftType
            print(list_aircraftType)
