import datetime
import dateutil.parser

class Voyage:
    def __init__(self, status, sold_seats, airplane, date):
        self.status = status
        self.sold_seats = sold_seats
        self.airplane = airplane
        self.employees = []
        self.date = dateutil.parser.parse(date)


    def add_voyage(self):
        print("Please enter the details of the new voyage")
        status = input("Status: ")
        sold_seats = input("Sold Seats: ")
        airplane = input("Plane Insignia: ")
        year = input("Year: ")
        month = input("Month: ")
        day = input("Day: ")
        hour = input("Hour: ")
        minute = input("Minute: ")
        date = datetime.datetime(year,month,day,hour,minute,0).isoformat()
        return Voyage(status, sold_seats, airplane, date)
        print("Wow! you created an voyage!")


    def add_employee_to_voyage(self, ssn):
        self.employees.append(ssn)

