import datetime
import dateutil.parser
from Models.VoyageMODEL import Voyage
from Data.DataLayerAPI import DataLayer

class VoyageLL:
    TIME = 60 # The time between landing and takeoff at some location (in sec)
    def __init__(self):
        self.__data_layer = DataLayer()

    def create_voyage(self, some_voyage): # Er að vinna í þessu
        all_voyages = self.__data_layer.list_voyages()
        new_voyage_date = dateutil.parser.parse(some_voyage)

        all_destinations = self.__data_layer.list_destinations()
        new_voyage_destination = some_voyage.get_destination()

        # Find colliding voyage indexes
        colliding_voyages = []
        for num in range(len(all_voyages)):
            voyage_date = dateutil.parser.parse(all_voyages[num].get_departure())
            if new_voyage_date.year == voyage_date.year \
            and new_voyage_date.month == voyage_date.month \
            and new_voyage_date.day == voyage_date.day:
                if all_voyages[num].get_destination() == new_voyage_destination:
                    colliding_voyages.append(num)

        # Change flight numbers for the colliding voyages
        last_num = 0
        for num in colliding_voyages:
            voyage_date = dateutil.parser.parse(all_voyages[num].get_departure())
            if voyage_date < new_voyage_date:
                last_num += 2
            elif voyage_date > new_voyage_date:
                all_voyages[num].change_flight_numbers()
    
        # Get the destination number
        for destination in all_destinations:
            if destination == new_voyage_destination:
                destination_number = destination.get_destiantion_number()

        # Assemble the flight numbers
        flight_num_1 = 'NA' + destination_number + str(last_num)
        flight_num_2 = 'NA' + destination_number + str(last_num + 1)

        # Add flight numbers to the new voyage
        some_voyage.add_flight_numbers_to_voyage(flight_num_1, flight_num_2)

        all_voyages.append(some_voyage)
        self.__data_layer.overwrite_voyages(all_voyages)

    def voyage_time_check(self, some_voyage):
        all_voyages = self.__data_layer.list_voyages()
        for voyage in all_voyages:
            if voyage.get_departure() == some_voyage.get_departure():
                return False
        return True

    def find_voyage(self, search_word):
        all_voyages = self.__data_layer.list_voyages()
        found_voyages = []
        for voyage in all_voyages:
            if voyage == search_word:
                found_voyages.append(voyage)
        return found_voyages

    def get_all_voyages(self):
        return self.__data_layer.list_voyages()

    def add_employee_to_voyage(self, ssn): # Þarf að skrifa
        pass