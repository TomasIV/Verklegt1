import csv
from Models.VoyageMODEL import Voyage

class VoyageDL:
    PATH = "CSVFiles/Voyages.csv"
    def __init__(self):
        pass

    def list_voyages(self):
        list_of_voyages = []
        with open(self.PATH, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                voyage = Voyage(row['destination'], row['departure'], row['aircraftID'], [row['flightNumber1'], row['flightNumber2']], [row['captain'], row['copilot'], row['fsm'], row['fa1'], row['fa2']])
                list_of_voyages.append(voyage)
            return list_of_voyages
    
    def overwrite_file(self, list_of_voyages):
        with open(self.PATH, "w") as cleared_file:
            overwriter = csv.writer(cleared_file, lineterminator= "\r")
            overwriter.writerow(['flightNumber1', 'flightNumber2', 'destination', 'departure', 'aircraftID', 'soldSeats', 'captain', 'copilot', 'fsm', 'fa1', 'fa2'])
            for path in list_of_voyages:
                overwriter.writerow(path.get_voyage_attributes())
