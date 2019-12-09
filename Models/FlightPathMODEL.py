import datetime
import dateutil.parser

class FlighPath:
    def __init__(self, departing_location, destination, departure_year, departure_month, departure_day, departure_hour, departure_minute):
        self.__flight_number = ''
        self.__departing_id = departing_location
        self.__destination_id = destination
        self.__departure_timestamp = datetime.datetime(int(departure_year), int(departure_month), int(departure_day), int(departure_hour), int(departure_minute), 0).isoformat
        self.__arrival_timestamp = ''
    
    def set_arrival_time(self, length_of_fight):
        minutes = int(length_of_fight)
        self.__arrival_timestamp = self.__departure_timestamp + datetime.timedelta(minutes,0)
    
    def set_flight_number(self, flight_number):
        self.__flight_number = flight_number

    def get_flightpath_attributes(self):
        return [self.__flight_number, self.__departing_id, self.__destination_id, self.__departure_timestamp, self.__arrival_timestamp]

    def __str__(self):
        the_line = "Flightnumber: {}   Departing from: {}   Arriving at: {}\nDeparture: {}   Arrival: {}".format(self.__flight_number, self.__departing_id, self.__destination_id, self.__departure_timestamp, self.__arrival_timestamp)
        return the_line