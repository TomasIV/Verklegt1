import datetime
import dateutil.parser

class Voyage:
    '''Voyage class.
    It has 17 attributes but only takes 16 variables (besides "self"),
    11 of which have a default value.
    All of the defaulted variables can be assigned via functions within the class.'''
    def __init__(self, airplane, destination, sold_seats_out, sold_seats_back, \
            first_departure_date, first_arrival_date = '', second_departure_date = '', second_arrival_date = '', \
            home_airport = 'KEF', flight_number_1 = '', flight_number_2 = '', captain = '', copilot = '', fsm = '', fa1 = '', fa2 = ''):
        self.__aircraft_id = airplane
        self.__home_id = home_airport
        self.__destination_id = destination
        self.__first_departure = first_departure_date
        self.__first_arrival = first_arrival_date
        self.__second_departure = second_departure_date
        self.__second_arrival = second_arrival_date
        self.first_sold_seats = sold_seats_out
        self.second_sold_seats = sold_seats_back
        self.first_flight_number = flight_number_1
        self.second_flight_number = flight_number_2
        self.captain = captain
        self.copilot = copilot
        self.fsm = fsm
        self.fa1 = fa1
        self.fa2 = fa2
        self.seats = 0

    def __str__(self):
        '''Returnes all attributes on a very readable string format'''
        if self.captain != '' and self.copilot != '' and self.fsm != '':
            manned_or_not = 'Fully manned'
        else:
            manned_or_not = 'Not fully manned!'

        attributes = ['Aircraft ID:', 'Flight number:', 'Departure:', 'Arrival:', 'Available seats:', 'Sold seats:', 'Captain:', 'Copilot:', 'Flight service manager:', 'Flight attendant:']
        return "{:<24s}{:<15s}{:<17s}{:<25s}{:<17s}{}\n{:<39s}{} to {:<35s}{} to {}\n{:<24s}{:<15s}{:<17s}{:<25s}{:<17s}{}\n{:<24s}{:<15s}{:<17s}{:<25s}{:<17s}{}\n{:<24s}{:<15s}{:<17s}{:<25s}{:<17s}{}\n{:<24s}{:<15s}{:<17s}{:<25s}{:<17s}{}\n{:<24s}{:<15s}\n".\
            format(attributes[0], self.__aircraft_id, attributes[1], self.first_flight_number, attributes[1], self.second_flight_number, \
            manned_or_not, self.__home_id, self.__destination_id, self.__destination_id, self.__home_id, \
            attributes[6], self.captain, attributes[2], self.__first_departure, attributes[2], self.__second_departure, \
            attributes[7], self.copilot, attributes[3], self.__first_arrival, attributes[3], self.__second_arrival, \
            attributes[8], self.fsm, attributes[4], str(self.seats - int(self.first_sold_seats)), attributes[4], str(self.seats - int(self.second_sold_seats)), \
            attributes[9], self.fa1, attributes[5], self.first_sold_seats, attributes[5], self.second_sold_seats, \
            attributes[9], self.fa2)

    def __eq__(self, comparison):
        if self.__aircraft_id == comparison \
        or self.__destination_id == comparison \
        or self.__first_departure == comparison \
        or self.first_flight_number == comparison \
        or self.second_flight_number == comparison \
        or self.captain == comparison \
        or self.copilot == comparison \
        or self.fsm == comparison \
        or self.fa1 == comparison \
        or self.fa2 == comparison:
            return True
        else:
            return False

    def get_identification(self):
        one = ("\n{:<30s}{:<30s}{:<30s}{:<30s}{:<30s}".format("From/To", "Flight number", "Departure", "Arrival", "Sold seats"))
        two = ("{:<30s}{:<30s}{:<30s}{:<30s}{:<30s}".format("From ICE To " + self.__destination_id, self.first_flight_number, self.__first_departure, self.__first_arrival, self.first_sold_seats))
        three = ("{:<30s}{:<30s}{:<30s}{:<30s}{:<30s}\n".format("From " + self.__destination_id + " To ICE", self.second_flight_number, self.__second_departure, self.__second_arrival, self.second_sold_seats))
        return (one, two, three)

    def get_voyage_attributes(self):
        '''Returnes the voyage attributes in a list'''
        return [self.__aircraft_id, self.__home_id, self.__destination_id, \
            self.first_flight_number, self.first_sold_seats, self.__first_departure, self.__first_arrival, \
            self.second_flight_number, self.second_sold_seats, self.__second_departure, self.__second_arrival, \
            self.captain, self.copilot, self.fsm, self.fa1, self.fa2]

    def get_employees_on_voyage(self):
        '''Returnes the employee social security numbers in a list'''
        return [self.captain, self.copilot, self.fsm, self.fa1, self.fa2]

    def get_destination(self):
        '''Returnes the destination id of a voyage'''
        return self.__destination_id
    
    def get_home_airport(self):
        '''Returnes the home airport'''
        return self.__home_id

    def get_voyage_flight_numbers(self):
        '''Returnes the flight numbers of a voyage'''
        return (self.first_flight_number, self.second_flight_number)
    
    def get_voyage_plane_id(self):
        '''Returnes the plane id of a voyage'''
        return self.__aircraft_id

    def get_voyage_depart_time(self):
        '''Returnes the first departure time of a voyage on iso format'''
        return self.__first_departure

    def get_takeoff_dates(self):
        '''Returnes the takeoff dates in a list'''
        return [self.__first_departure, self.__first_arrival, self.__second_departure, self.__second_arrival]

    def get_arrival(self):
        '''Returnes the second arrival of a voyage on iso format'''
        return self.__second_arrival

    def get_airplane_name(self):
        '''Returnes the plane id of a voyage'''
        return self.__aircraft_id
    
    def add_dates_to_voyage(self, first_arrival_date, second_departure_date, second_arrival_date):
        '''Takes three dates on iso format and assigns it to the date variables'''
        self.__first_arrival = first_arrival_date
        self.__second_departure = second_departure_date
        self.__second_arrival = second_arrival_date
    
    def add_flight_numbers_to_voyage(self, num1, num2):
        '''Takes two flight numbers on string format and assigns it to the flight number variables'''
        self.first_flight_number = num1
        self.second_flight_number = num2
    
    def add_number_of_seats(self, number_of_seats):
        '''Takes a number of seats for a plane on string format and assigns it to the seat variable'''
        self.seats = number_of_seats

    def change_flight_numbers(self):
        '''Takes an instance of a Voyage and raises the last number in the flight numbers by 2'''
        last_num_1 = int(self.first_flight_number[4])
        last_num_2 = int(self.second_flight_number[4])

        last_char_1 = str(last_num_1 + 2)
        last_char_2 = str(last_num_2 + 2)

        self.first_flight_number = self.first_flight_number[:4] + last_char_1
        self.second_flight_number = self.second_flight_number[:4] + last_char_2