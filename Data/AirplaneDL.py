import csv
#from Logic.LogicLayerAPI import LogicLayer
from Models.AirplaneMODEL import Airplane

class AirplaneDL:
    PATH = "CSVFiles/Aircraft.csv"
    def __init__(self):
        pass
    
    def list_airplanes(self):
            list_airplanes = []
            with open(self.PATH, 'r') as csvfile:
                reader = csv.DictWriter(csvfile)
                for row in reader:
                    airplane = Airplane(row['planeInsignia'], row['planeTypeId'])
                    list_airplanes.append(airplane)
                #return list_airplane
                print(list_airplanes)

    def save_airplane(self, some_airplane):
        '''Takes an instance of an airplane and saves it in an airplane file.
        If such file doesn't exist, it's created.'''
        with open(self.PATH, "a") as airplane:
            csv_writer = csv.writer(airplane)
            list_of_attributes = [some_airplane.name, some_airplane.model]
            csv_writer.writerow(list_of_attributes)


