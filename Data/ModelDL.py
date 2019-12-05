import csv
from Logic.LogicLayerAPI import LogicLayer


class Model:
    def __init__(self):
        pass

    def save_model(self, some_aircraftType):
         with open("AircraftType.csv", "a") as aircraftType:
            csv_writer = csv.writer(aircraftType)
            list_of_attributes = [some_aircraftType.planeTypeId, some_aircraftType.manufacturer , some_aircraftType.model, some_aircraftType.capacity, some_aircraftType.emptyWeight, some_aircraftType.maxTakeoffWeight, some_aircraftType.unitThrust , some_aircraftType.serviceCeiling , some_aircraftType.length , some_aircraftType.height , some_aircraftType.wingspan]
            csv_writer.writerow(list_of_attributes)

#planeTypeId,manufacturer,model,capacity,emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan


    def list_model(self):