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
        self.employees = employees

    def __str__(self):
        """Very very long string"""
        a_str = "{:<30s}: {}\t{:<30s}: {}\n{:<30s}: {}\t{:<30s}: {}\n{:<30s}: {}\t{:<30s}: {}\n{:<30s}: {}\t{:<30s}: {}\n{:<30s}: {}\t{:<30s}: {}\n{:<30s}: {}".format(
        "Aircraft ID", self.__aircraft_id,
        "Home Airport", self.__home_id, "Destination ID", self.__destination_id, "Departure date", self.__first_departure,
        "Arrival date", self.__first_arrival, "Departure from destination", self.__second_departure, "Arrival from destination", self.__second_arrival,
        "Sold seats to destination", self.first_sold_seats, "Sold seats from destination", self.second_sold_seats, 
        "First flight number", self.first_flight_number, "Second flight number", self.second_flight_number)
        try:
            a_str += "\n{:<30s}: {}\n".format("Employees on this voyage", self.employees.get_ssn())
        except:
            a_str += "\n{:<30s}: {}\n".format("Employees on this voyage", "None")
        return a_str

    def get_identification(self):
        one = ("\n{:<30s}{:<30s}{:<30s}{:<30s}{:<30s}".format("From/To", "Flight number", "Departure", "Arrival", "Sold seats"))
        two = ("{:<30s}{:<30s}{:<30s}{:<30s}{:<30s}".format("From ICE To " + self.__destination_id, self.first_flight_number, self.__first_departure, self.__first_arrival, self.first_sold_seats))
        three = ("{:<30s}{:<30s}{:<30s}{:<30s}{:<30s}\n".format("From " + self.__destination_id + " To ICE", self.second_flight_number, self.__second_departure, self.__second_arrival, self.second_sold_seats))
        return (one, two, three)
    def get_destination(self):
        return self.__destination_id
    
    def get_home_airport(self):
        return self.__home_id
    
    def get_departure(self):
        return self.__first_departure

    def get_takeoff_dates(self):
        return [self.__first_departure, self.__first_arrival, self.__second_departure, self.__second_arrival]

    def get_voyage_attributes(self):
        list_of_attributes = [self.__aircraft_id, self.__home_id, self.__destination_id, \
            self.first_flight_number, self.first_sold_seats, self.__first_departure, self.__first_arrival, \
            self.second_flight_number, self.second_sold_seats, self.__second_departure, self.__second_arrival]
        list_of_attributes.extend(self.employees)
        return list_of_attributes

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
    
    def clean_employee_list(self):
        for num in range(len(self.employees)-1, -1, -1):
            if self.employees[num] == '':
                self.employees.pop(num)

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
    def get_voyage_flight_numbers(self):
        return (self.first_flight_number, self.second_flight_number)
    def get_voyage_depart_time(self):
        return self.__first_departure