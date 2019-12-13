import csv
from Models.VoyageMODEL import Voyage

class VoyageDL:
    PATH = "CSVFiles/Voyages.csv"
    def __init__(self):
        pass

    def list_voyages(self):
        '''Opens an voyages file and reads all voyages from it.
        Returns a list of all voyages.'''
        list_of_voyages = []
        with open(self.PATH, 'r', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, lineterminator = "\r")
            for row in reader:
                voyage = Voyage(row['aircraftID'], row['destination'], row['soldseats1'], row['soldseats2'], \
                        row['departure1'], row['arrival1'], row['departure2'], row['arrival2'], row['homeairport'], \
                        row['flightnumber1'], row['flightnumber2'], row['captain'], row['copilot'], row['fsm'], row['fa1'], row['fa2'])
                list_of_voyages.append(voyage)
            return list_of_voyages

    def overwrite_file(self, list_of_voyages):
        '''Opens employee file and writes new info into employee file'''
        with open(self.PATH, "w", encoding="utf-8") as cleared_file:
            overwriter = csv.writer(cleared_file, lineterminator= "\r", )
            overwriter.writerow(['aircraftID', 'homeairport', 'destination', \
                'flightnumber1', 'soldseats1', 'departure1', 'arrival1', \
                'flightnumber2', 'soldseats2', 'departure2','arrival2', \
                'captain', 'copilot', 'fsm', 'fa1','fa2'])
            for path in list_of_voyages:
                overwriter.writerow(path.get_voyage_attributes())
