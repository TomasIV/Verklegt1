import datetime
import dateutil.parser

class Voyage:
    def __init__(self, destination, date, airplane, flight_numbers = [], employees = []):
        self.__flight_numbers = flight_numbers
        self.__destination_id = destination
        self.__departure = date
        self.__aircraft_id = airplane
        self.employees = employees
    
    def get_destination(self):
        return self.__destination_id

    def get_voyage_attributes(self):
        return [self.__flight_numbers[0], self.__flight_numbers[1], self.__destination_id, self.__departure, self.__aircraft_id, self.employees[0], self.employees[1], self.employees[2], self.employees[3], self.employees[4]]

    def add_employee_to_voyage(self, ssn):
        self.employees.append(ssn)

    def __eq__(self, comparison):
        if comparison in self.__flight_numbers \
        or self.__destination_id == comparison \
        or self.__departure == comparison \
        or self.__aircraft_id == comparison \
        or comparison in self.employees:
            return True
        else:
            return False