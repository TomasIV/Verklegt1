import datetime
import dateutil.parser

class Voyage:
    def __init__(self, airplane, destination, sold_seats_out, sold_seats_back, first_departure_date, first_arrival_date = '', second_departure_date = '', second_arrival_date = '', home_airport = 'KEF', flight_number_1 = '', flight_number_2 = '', employees = []):
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
        self.employees = []
    
    def get_destination(self):
        return self.__destination_id
    
    def get_departure(self):
        return self.__first_departure

    def get_voyage_attributes(self):
        return [self.__aircraft_id, self.__home_id, self.__destination_id, \
            self.first_flight_number, self.first_sold_seats, self.__first_departure, self.__first_arrival, \
            self.second_flight_number, self.second_sold_seats, self.__second_departure, self.__second_arrival, \
            self.employees[0], self.employees[1], self.employees[2], self.employees[3], self.employees[4]]

    def add_employee_to_voyage(self, ssn):
        self.employees.append(ssn)
    
    def add_dates_to_voyage(self, first_arrival_date, second_departure_date, second_arrival_date):
        self.__first_arrival = first_arrival_date
        self.__second_departure = second_departure_date
        self.__second_arrival = second_arrival_date
    
    def add_flight_numbers_to_voyage(self, num1, num2):
        self.first_flight_number = num1
        self.second_flight_number = num2

    def change_flight_numbers(self):
        '''Takes an instance of a Voyage and raises the last number in the flight numbers by 2'''
        last_num_1 = int(self.first_flight_number[4])
        last_num_2 = int(self.second_flight_number[4])

        last_char_1 = str(last_num_1 + 2)
        last_char_2 = str(last_num_2 + 2)

        self.first_flight_number = self.first_flight_number[:4] + last_char_1
        self.second_flight_number = self.second_flight_number[:4] + last_char_2

    def __eq__(self, comparison):
        if self.__aircraft_id == comparison \
        or self.__destination_id == comparison \
        or self.__first_departure == comparison \
        or self.first_flight_number == comparison \
        or self.second_flight_number == comparison \
        or comparison in self.employees:
            return True
        else:
            return False