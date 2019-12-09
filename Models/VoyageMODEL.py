import datetime
import dateutil.parser

class Voyage:
    def __init__(self, destination, date, airplane, sold_seats, flight_numbers = [], employees = []):
        self.__flight_numbers = flight_numbers
        self.__destination_id = destination
        self.__departure = date
        self.__aircraft_id = airplane
        self.sold_seats = sold_seats
        self.employees = employees

    def get_voyage_attributes(self):
        return [self.__flight_numbers[0], self.__flight_numbers[1], self.__destination_id, self.__departure, self.__aircraft_id, self.sold_seats, self.employees[0], self.employees[1], self.employees[2], self.employees[3], self.employees[4]]

    # Þetta fall á að vera í interfacinu
    '''def create_voyage(self):
        print("Please enter the details of the new voyage")
        #status = input("Status: ") Status á nýju voyage????
        sold_seats = input("Sold Seats: ")
        airplane = input("Plane Insignia: ")
        year = int(input("Year: "))
        month = int(input("Month: "))
        day = int(input("Day: "))
        hour = int(input("Hour: "))
        minute = int(input("Minute: "))
        date = dateutil.parser.parse(datetime.datetime(year,month,day,hour,minute,0).isoformat())
        input ("{} :)".format(date))
        return Voyage(sold_seats, airplane, date)
        #status'''

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