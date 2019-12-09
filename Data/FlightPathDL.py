import csv
from Models.FlightPathMODEL import FlighPath

class FlightPathDL:
    PATH = "CSVFiles/UpcomingFlights.csv"
    def __init__(self):
        pass

    def list_flight_paths(self):
        list_of_flight_paths = []
        with open(self.PATH, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                flight_path = FlighPath(row['departingFrom'], row['arrivingAt'], row['departure'], row['arrival'], row['flightNumber'])
                list_of_flight_paths.append(flight_path)
            return list_of_flight_paths
    
    def overwrite_file(self, list_of_flight_paths):
        with open(self.PATH, "w") as cleared_file:
            overwriter = csv.writer(cleared_file, lineterminator= "\r")
            overwriter.writerow(['flightNumber', 'departingFrom', 'arrivingAt', 'departure', 'arrival'])
            for path in list_of_flight_paths:
                overwriter.writerow(path.get_flightpath_attributes())