import csv
#from Logic.LogicLayerAPI import LogicLayer
from Models.AirplaneMODEL import Airplane

class AirplaneDL:
    PATH = "CSVFiles/Aircraft.csv"
    def __init__(self):
        pass

    def list_all_airplanes(self):
            '''Takes an aircraft file and reads all airplanes from it.
                Returns a list of all airplanes.'''        
            list_airplanes = []
            with open(self.PATH, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    airplane = Airplane(row['planeInsignia'], row['planeTypeId'], row['capacity'])
                    list_airplanes.append(airplane)
                return list_airplanes

    def save_airplane(self, some_airplane):
        '''Takes an instance of an airplane and saves it in an aircraft file.
        If such file doesn't exist, it's created.'''
        with open(self.PATH, "a", encoding="utf-8") as airplane:
            csv_writer = csv.writer(airplane, lineterminator ="\r")
            csv_writer.writerow(some_airplane.get_airplane_attributes())

    def overwrite_file(self, list_of_airplanes):
        '''Opens Aircraft file and writes new info into Aircraft file'''
        with open(self.PATH, "w", encoding="utf-8") as cleared_file:
            overwriter = csv.writer(cleared_file, lineterminator= "\r")
            overwriter.writerow(["planeInsignia", "planeTypeId"], ['capacity'])
            for airplane in list_of_airplanes:
                overwriter.writerow(airplane.get_airplane_attributes())


