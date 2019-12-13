import csv
from Models.DestinationMODEL import Destination

class DestinationDL:
    PATH = "CSVFiles/Destinations.csv"
    def __init__(self):
        pass

    # We needed to be able to save all new info for destinations 
    '''Takes an instance of a destination and saves it in a destination file.
        If such file doesn't exist, it's created.'''
    def save_destinations(self, some_destination):
        with open(self.PATH, "a", encoding="utf-8") as destination:
            csv_writer = csv.writer(destination, lineterminator = "\r")
            csv_writer.writerow(some_destination.get_destination_attributes())

    def list_destinations(self):
        '''Takes an destination file and reads all destinations from it.
            Returns a list of all destinations.'''
        list_destinations = []
        with open(self.PATH, 'r', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, lineterminator = "\r")
            for row in reader:
                destination = Destination(row['id'], row['destination'], row['destinationNumber'], row['emergencycontact'],row['phonenumber'], row['flighttime'], row['kilometers'])
                list_destinations.append(destination)
        return list_destinations
    
    def overwrite_destination_file(self, list_of_destinations):
        '''Opens destination file and overwrites new info into destination file'''
        with open(self.PATH, "w", encoding="utf-8") as cleared_file:
            overwriter = csv.writer(cleared_file, lineterminator= "\r")
            overwriter.writerow(['id', 'destination', 'destinationNumber', 'emergencycontact', 'phonenumber', 'flighttime', 'kilometers'])
            for place in list_of_destinations:
                overwriter.writerow(place.get_destination_attributes())