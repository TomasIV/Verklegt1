import csv
from Logic.LogicLayerAPI import LogicLayer


class Model:
    def __init__(self):
        pass

    def save_model(self, some_aircraftType):
         with open("AircraftType.csv", "a") as aircraftType:
            csv_writer = csv.writer(aircraftType, lineterminator= "\r" )
            csv_writer.writerow(some_aircraftType.get_aircraftType_attributes())

#planeTypeId,manufacturer,model,capacity,emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan


    def list_model(self):
        list_aircraftType = []
        with open('AircraftTypes.csv', 'r') as csvfile:
            reader = csv.DictWriter(csvfile)
            for row in reader: 
                aircraftType = aircraftType(row['planeTypeId'], row['manufacturer'], row['model'],row['capacity'], row['emptyWheight'], row['maxTakeoffWeight'], row['unitThrust'], row['serviceCeiling'], row['length'], row['height'], row['wingspan'])
                list_aircraftType.append(aircraftType)
            #return list_aircraftType
            print(list_aircraftType)