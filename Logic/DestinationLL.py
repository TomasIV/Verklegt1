from Data.DataLayerAPI import DataLayer
from Models.DestinationMODEL import Destination

class DestinationLL:
    def __init__(self):
        self.__data_layer = DataLayer()

    def list_all_destinations(self):
        return self.__data_layer.list_destinations()

    def save_destination(self, new_destination):
        self.__data_layer.save_destinations(new_destination)

    def change_destination(self, destination_name, what_to_change, new_info):
        all_destinations = self.__data_layer.list_destinations()
        for num in range(len(all_destinations)):
            if all_destinations[num] == destination_name:
                if what_to_change == 'emergencycontact':
                    all_destinations[num].emergency_contact = new_info
                elif what_to_change == 'phonenumber':
                    all_destinations[num].emergency_phone = new_info
        self.__data_layer.overwrite_destination_file(all_destinations)

    def list_most_popular_destination(self):
        '''Returns a tuple'''
        all_voyages = self.__data_layer.list_voyages()
        all_destination_ids = []
        for voyage in all_voyages:
            all_destination_ids.append(voyage.get_destination())
        destination_dict = {}
        for destination in all_destination_ids:
            if destination in destination_dict:
                destination_dict[destination] += 1
            else:
                destination_dict[destination] = 1
        list_of_tuples = []
        for k, v in destination_dict.items():
            list_of_tuples.append((v, k))
        list_of_tuples.sort()
        pop_des = self.find_destination(list_of_tuples[-1][1])
        return (pop_des.get_name(), list_of_tuples[-1][0])

    def find_destination(self, search_word):
        all_destinations = self.__data_layer.list_destinations()
        for place in all_destinations:
            if place == search_word:
                return place
