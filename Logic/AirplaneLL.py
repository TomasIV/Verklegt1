from Models.AirplaneMODEL import Airplane
from Data.DataLayerAPI import DataLayer

class AirplaneLL:
    def __init__(self):
        self.__data_layer = DataLayer()

    def save_airplane(self, new_airplane):
        self.__data_layer.save_airplane(new_airplane)

    def list_airplanes(self):
        return self.__data_layer.list_airplanes()

    def change_airplane(self, planeInsignia, what_to_change, new_info):
        all_airplanes = self.__data_layer.list_airplanes()
        for num in range(len(all_airplanes)):
            if all_airplanes[num] == planeInsignia:
                if what_to_change == 'planeInsignia':
                    all_airplanes[num].name = new_info
                elif what_to_change == 'PlaneTypeId':
                    all_airplanes[num].model = new_info
                self.__data_layer.overwrite_airplane_file(all_airplanes)
            else:
                input("Airplane not found, press enter to return to main menu...")