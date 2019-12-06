import csv
#from Logic.LogicLayerAPI import LogicLayer
from Models.AirplaneMODEL import Airplane

class AirplainDL:
    PATH = "CSVFiles/Aircraft.csv"
    def __init__(self):
        pass
    
def list_airplanes(self):
        list_airplanes = []
        with open(PATH, 'r') as csvfile:
            reader = csv.DictWriter(csvfile)
            for row in reader:
                airplane = Airplane(row['planeInsignia'], row['planeTypeId'])
                list_airplanes.append(airplane)
            #return list_airplane
            print(list_airplanes)

def save_airplane(self, some_airplane):
    '''Takes an instance of an airplane and saves it in an airplane file.
    If such file doesn't exist, it's created.'''
    with open(PATH, "a") as airplane:
        csv_writer = csv.writer(some_airplane, lineterminator= "\r" )
        csv_writer.writerow(some_airplane.get_airplane_attributes())


