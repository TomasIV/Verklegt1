import csv
from Models.VoyageMODEL import Voyage

class VoyageDL:
    PATH = "CSVFiles/Voyages.csv"
    def __init__(self):
        pass

    def list_voyages(self):
        list_of_voyages = []
        with open(self.PATH, 'r', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, lineterminator = "\r")
            for row in reader:
                voyage = Voyage(row['aircraftID'], row['destination'], row['soldseats1'], row['soldseats2'], \
                        row['departure1'], row['arrival1'], row['departure2'], row['arrival2'], row['homeairport'], \
                        row['flightnumber1'], row['flightnumber2'], [row['em1'], row['em2'], row['em3'], row['em4'], row['em5']])
                list_of_voyages.append(voyage)
            return list_of_voyages
    
    def overwrite_file(self, list_of_voyages):
        with open(self.PATH, "w", encoding="utf-8") as cleared_file:
            overwriter = csv.writer(cleared_file, lineterminator= "\r", )
            overwriter.writerow(['aircraftID', 'homeairport', 'destination', \
                'flightnumber1', 'soldseats1', 'departure1', 'arrival1', \
                'flightnumber2', 'soldseats2', 'departure2','arrival2', \
                'em1', 'em2', 'em3', 'em4', 'em5'])
            for path in list_of_voyages:
                overwriter.writerow(path.get_voyage_attributes())
