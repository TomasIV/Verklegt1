import datetime
import dateutil.parser

class FlighPath:
    def __init__(self, departing_location, destination, departure_time, sold_seats, arrival_time = '', flight_number = ''):
        self.__flight_number = flight_number
        self.__departing_id = departing_location
        self.__destination_id = destination
        self.__departure_timestamp = departure_time
        self.__sold_seats = sold_seats
        self.__arrival_timestamp = arrival_time
    
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