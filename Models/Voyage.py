import datetime
import dateutil.parser

class Voyage:
    def __init__(self, status, sold_seats, airplain, employee_ssn, date):
        self.status = status
        self.sold_seats = sold_seats
        self.airplain = airplain
        self.employee_ssn = employee_ssn
        self.date = dateutil.parser.parse(date)


    def add_voyage(self):
        print("Please enter the details of the new voyage")
        status = input("Status: ")
        sold_seats = input("Sold Seats: ")
        airplain = input("Plane Insignia: ")
        employee_ssn = input("Employee SSN: ")
        year = input("Year: ")
        month = input("Month: ")
        day = input("Day: ")
        hour = input("Hour: ")
        minute = input("Minute: ")
        date = datetime.datetime(year,month,day,hour,minute,0).isoformat()
        return Voyage(status, sold_seats, airplain, employee_ssn, date)
        print("Wow! you created an voyage!")


