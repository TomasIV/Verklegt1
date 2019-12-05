import csv
#from Logic.LogicLayerAPI import LogicLayer


class Model:
    def __init__(self):
        pass

    def save_model(self, some_aircraftType):
         with open("CSVFiles\AircraftType.csv", "a") as aircraftType:
            csv_writer = csv.writer(aircraftType, lineterminator= "\r" )
            csv_writer.writerow(some_aircraftType.get_aircraftType_attributes())

#planeTypeId,manufacturer,model,capacity,emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan


    def list_model(self):
        