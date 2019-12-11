import csv


class PlaneModel:
    PATH = "CSVFiles/AircraftType.csv"
    def __init__(self):
        pass

    def save_model(self, some_aircraftType):
         with open(self.PATH, "a", encoding="utf-8") as aircraftType:
            csv_writer = csv.writer(aircraftType, lineterminator= "\r" )
            csv_writer.writerow(some_aircraftType.get_aircraftType_attributes())

#planeTypeId,manufacturer,model,capacity,emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan


    def list_all_airplane_models(self):
        list_aircraftType = []
        with open(self.PATH, 'r', encoding="utf-8") as csvfile:
            reader = csv.DictWriter(csvfile)
            for row in reader: 
                aircraftType = aircraftType(row['planeTypeId'], row['manufacturer'], row['model'],row['capacity'], row['emptyWheight'], row['maxTakeoffWeight'], row['unitThrust'], row['serviceCeiling'], row['length'], row['height'], row['wingspan'])
                list_aircraftType.append(aircraftType)
            return list_aircraftType