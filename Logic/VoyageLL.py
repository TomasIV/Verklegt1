from Models.VoyageMODEL import Voyage
from Data.DataLayerAPI import DataLayer

class VoyageLL:
    def __init__(self):
        self.__data_layer = DataLayer()

    def get_voyage_to_add_employee_on(self, search_word):
        all_voyages = self.__data_layer.list_voyage()
        found_voyages = []
        for person in all_voyages:
            if person == search_word:
                found_voyages.append(person)
        return found_voyages

    def add_employee_to_voyage(self, ssn):
        pass

    
