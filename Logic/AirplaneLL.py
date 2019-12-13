import datetime
import dateutil.parser
from Models.AirplaneMODEL import Airplane
from Models.VoyageMODEL import Voyage
from Data.DataLayerAPI import DataLayer

class AirplaneLL:
    def __init__(self):
        self.__data_layer = DataLayer()

    def save_airplane(self, new_airplane):
        ''' Takes an instanse of airplane and saves it'''
        all_models = self.__data_layer.list_aircraft_models()
        for model in all_models:
            if model[0] == new_airplane:
                new_airplane.add_seats(model[3])
        self.__data_layer.save_airplane(new_airplane)

    def list_airplanes(self):
        ''' Takes info and returns list of airplanes'''
        return self.__data_layer.list_airplanes()
    
    def get_airplane_status(self, some_plane, some_date):
        ''' Takes an instance of airplane status if avalible then returns 'Avalible for the day else returns un'''
        all_voyages = self.__data_layer.list_voyages()
        some_date = dateutil.parser.parse(some_date)
        for voyage in all_voyages:
            voyage_date = dateutil.parser.parse(voyage.get_voyage_depart_time())
            if voyage_date.date() == some_date.date() and some_plane.get_name() == voyage.get_voyage_plane_id():
                departure_1, arrival_1, departure_2, arrival_2 = voyage.get_takeoff_dates()
                departure_1 = dateutil.parser.parse(departure_1)
                arrival_1 = dateutil.parser.parse(arrival_1)
                departure_2 = dateutil.parser.parse(departure_2)
                arrival_2 = dateutil.parser.parse(arrival_2)

                next_available_date = departure_1.date() + datetime.timedelta(days= 1)

                if some_date < departure_1:
                    return 'Unavailable (Pending flight)\n{:<20}Next available at {}'.format('', next_available_date)
                elif departure_1 <= some_date <= arrival_1:
                    des = voyage.get_destination()
                    return 'Unavailable (In flight to {})\n{:<20}Next available at {}'.format(des, '', next_available_date)
                elif arrival_1 < some_date < departure_2:
                    des = voyage.get_destination()
                    return 'Unavailable (Standby at {})\n{:<20}Next available at {}'.format(des, '', next_available_date)
                elif departure_2 <= some_date <= arrival_2:
                    des = voyage.get_home_airport()
                    return 'Unavailable (In flight to {})\n{:<20}Next available at {}'.format(des, '', next_available_date)
                elif arrival_2 < some_date:
                    return 'Unavailable\n{:<20}Next available at {}'.format('', next_available_date)

        return 'Available for the day'
