from Data.DataLayerAPI import DataLayer

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

    def list_most_popular_destination(self): # Þarf að skrifa
        pass

    def find_destination(self, search_word):
        all_destinations = self.__data_layer.list_destinations()
        for place in all_destinations:
            if place == search_word:
                return place
