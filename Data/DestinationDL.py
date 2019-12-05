import csv
from Models.DestinationMODEL import Destination

class DestinationDL:
    def __init__(self):
        pass


    def save_destinations(self, some_destination):
        with open("Destination.csv", "a") as destination:
            csv_writer = csv.writer(destination)
            list_of_attributes = [some_destination.id, some_destination.destination, some_destination.emergency_contact, some_destination.phonenumber]
            csv_writer.writerow(list_of_attributes)

    def list_destinations(self):
        list_destinations = []
        with open('Destination.csv', newline='') as csvfile:
            reader = csv.DictWriter(csvfile)
            for row in reader: 
                destination = Destination(row['id'], row['destination'], row['emergency contact'],row['phonenumber'])
                list_destinations.append(destination)
            #return list_destinations
            print(list_destinations)