import datetime
import dateutil.parser

class FlighPath:
    def __init__(self, flightnumber, departing_location, destination):
        self.__flight_number = flightnumber
        self.__departing_id = departing_location
        self.__destination_id = destination
    
    def get_flightpath_attributes(self):
        return [self.__flight_number, self.__departing_id, self.__destination_id, ]
        # flightNumber,departingFrom,arrivingAt,departure,arrival