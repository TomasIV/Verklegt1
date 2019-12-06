import datetime
import dateutil.parser

class Voyage:
    def __init__(self, status = "", sold_seats = "", airplane = "", date = ""):
        #self.status = status
        self.sold_seats = sold_seats
        self.airplane = airplane
        self.employees = []
        self.date = date


    def create_voyage(self):
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
        #status

    def add_employee_to_voyage(self, ssn):
        self.employees.append(ssn)

    def __eq__(self, comparison):
        if self.sold_seats == comparison \
        or self.airplane == comparison \
        or self.date == comparison: 
            return True
        else:
            return False


