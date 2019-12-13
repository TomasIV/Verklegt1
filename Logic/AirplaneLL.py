from Models.AirplaneMODEL import Airplane
from Data.DataLayerAPI import DataLayer

class AirplaneLL:
    def __init__(self):
        self.__data_layer = DataLayer()

    def save_airplane(self, new_airplane):
        self.__data_layer.save_airplane(new_airplane)

    def list_airplanes(self):
        return self.__data_layer.list_airplanes()

