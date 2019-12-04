import csv
from Models.Destination import Destination
from Logic.LogicLayerAPI import LogicLayer



class DestinationDL:
    def __init__(self):
        pass


    def save_destinations(self, some_destination):
        '''Takes an instance of an employee and saves it in an employee file.
        If such file doesn't exist, it's created.'''
        self.some_employee = some_employee
        with open("CSVFiles\Employees.csv", "a") as employees:
            csv_writer = csv.writer(employees, lineterminator = "\r")
            #list_of_attributes = [self.some_employee.ssn, self.some_employee.name, self.some_employee.role, self.some_employee.rank, self.some_employee.licence, self.some_employee.address, self.some_employee.mobile, self.some_employee.email]
            csv_writer.writerow(some_employee.get_employee_attributes())

    def list_destinations(self):
        list_destinations = []
        with open('Destination.csv', newline='') as csvfile:
            reader = csv.DictWriter(csvfile)
            for row in reader: 
                destination = Destination(row['id'], row['destination'], row['emergency contact'],row['phonenumber'])
                list_destinations.append(destination)
            #return list_destinations
            print(list_destinations)