import csv
from Logic.LogicLayerAPI import LogicLayer


class Model:
    def __init__(self):
        pass

    def save_model(self, some_airplaneType):
         with open("AircraftType.csv", "a") as aircraftType:
            csv_writer = csv.writer(aircraftType)
            list_of_attributes = [some_aircraftType].planeTypeId, some_destination.destination, some_destination.emergency_contact, some_destination.phonenumber]
            csv_writer.writerow(list_of_attributes)

    def list_model(self):