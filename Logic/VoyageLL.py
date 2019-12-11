from Models.VoyageMODEL import Voyage
from Data.DataLayerAPI import DataLayer

class VoyageLL:
    def __init__(self):
        self.__data_layer = DataLayer()

    def create_voyage(self, some_voyage, departure_sold_seats, arrival_sold_seats):
        pass

    def get_voyage_to_add_employee_on(self, search_word):
        all_voyages = self.__data_layer.list_voyages()
        found_voyages = []
        for voyage in all_voyages:
            if voyage == search_word:
                found_voyages.append(voyage)
        return found_voyages

    def get_all_voyages(self):
        return self.__data_layer.list_voyages()

    def add_employee_to_voyage(self, ssn):
        pass