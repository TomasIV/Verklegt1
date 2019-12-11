import datetime
import dateutil.parser
from Models.VoyageMODEL import Voyage
from Data.DataLayerAPI import DataLayer
from Models.FlightPathMODEL import FlighPath

class VoyageLL:
    def __init__(self):
        self.__data_layer = DataLayer()

    def create_voyage(self, some_voyage, departure_sold_seats, arrival_sold_seats):
        all_voyages = self.__data_layer.list_voyages()
        new_voyage_date = dateutil.parser.parse(some_voyage)
        colliding_voyages = []
        for voyage in all_voyages:
            voyage_date = dateutil.parser.parse(voyage.get_departure)
            if new_voyage_date.year == voyage_date.year \
            and new_voyage_date.month == voyage_date.month \
            and new_voyage_date.day == voyage_date.day:
                if voyage.get_destination() == some_voyage.get_destination():
                    colliding_voyages.append(voyage)
        # Ekki búið

    def voyage_time_check(self):
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