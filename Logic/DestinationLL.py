from Data.DataLayerAPI import DataLayer

class DestinationLL:
    def __init__(self):
        self.__data_layer = DataLayer()

    def list_all_destinations(self):
        return self.__data_layer.list_destinations()
    def save_destination(self, new_destination):
        self.__data_layer.save_destinations(new_destination)
