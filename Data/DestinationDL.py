import csv
from Models.DestinationMODEL import Destination

class DestinationDL:
    PATH = "CSVFiles/Destinations.csv"
    def __init__(self):
        pass


    def save_destinations(self, some_destination):
        with open(self.PATH, "a") as destination:
            csv_writer = csv.writer(destination)
            list_of_attributes = [some_destination.id, some_destination.destination, some_destination.emergency_contact, some_destination.phonenumber]
            csv_writer.writerow(list_of_attributes)

    def list_destinations(self):
        list_destinations = []
        with open(self.PATH, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader: 
                destination = Destination(row['id'], row['destination'], row['emergencycontact'],row['phonenumber'])
                list_destinations.append(destination)
            return list_destinations