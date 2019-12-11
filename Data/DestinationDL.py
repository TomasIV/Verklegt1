import csv
from Models.DestinationMODEL import Destination

class DestinationDL:
    PATH = "CSVFiles/Destinations.csv"
    def __init__(self):
        pass

    def save_destinations(self, some_destination):
        with open(self.PATH, "a", encoding="utf-8") as destination:
            csv_writer = csv.writer(destination)
            csv_writer.writerow(some_destination.get_destiantion_attributes())

    def list_destinations(self):
        list_destinations = []
        with open(self.PATH, 'r', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, lineterminator = "\r")
            for row in reader:
                destination = Destination(row['id'], row['destination'], row['destinationNumber'], row['emergencycontact'],row['phonenumber'], row['flighttime'], row['kilometers'])
                list_destinations.append(destination)
            return list_destinations