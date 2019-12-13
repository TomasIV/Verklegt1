import csv


class PlaneModel:
    PATH = "CSVFiles/AircraftType.csv"
    def __init__(self):
        pass

    def save_model(self, some_aircraftType):
        '''Takes an instance of an aircrafttype and saves it in file.
            If such file doesn't exist, it's created.'''
        with open(self.PATH, "a", encoding="utf-8") as aircraftType:
            csv_writer = csv.writer(aircraftType, lineterminator= "\r")
            csv_writer.writerow(some_aircraftType.get_aircraftType_attributes())

    def list_all_airplane_models(self):
        '''Takes an aircraftType file and reads all aircraftModels from it.
        Returns a list of all aircraftModels.'''
        list_aircraftType = []
        with open(self.PATH, 'r', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader: 
                aircraftType = [row['planeTypeId'], row['manufacturer'], row['model'],row['capacity'], row['emptyWeight'], row['maxTakeoffWeight'], row['unitThrust'], row['serviceCeiling'], row['length'], row['height'], row['wingspan']]
                list_aircraftType.append(aircraftType)
            return list_aircraftType