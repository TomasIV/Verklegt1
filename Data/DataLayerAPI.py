import csv
from Models.Employee import Employee
import os

class DataLayer:
    def __init__(self):
        pass
    def save_employee(self, some_employee):
        '''Takes an instance of an employee and saves it in an employee file.
        If such file doesn't exist, it's created.'''
        self.some_employee = some_employee
        with open("Data\Crew.csv", "a") as employees:
            csv_writer = csv.writer(employees)
            #list_of_attributes = [self.some_employee.ssn, self.some_employee.name, self.some_employee.role, self.some_employee.rank, self.some_employee.licence, self.some_employee.address, self.some_employee.mobile, self.some_employee.email]
            csv_writer.writerow(some_employee)

    def list_employee(self):
        list_employee = []
        with open('employees.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                employee = Employee(row['ssn'], row['name'], row['role'], row['rank'], row['licence'], row['address'], row['phonenumber'], row['email'])
                list_employee.append(employee)
            #return list_employee
            print(list_employee)

    def save_destinations():
        pass

    def list_destinations(self):
        list_destinations = []
        with open('Destination.csv', newline='') as csvfile:
            reader = csv.DictWriter(csvfile)
            for row in reader: 
                destination = Destination(row['id'], row['destination'], row['emergency contact'],row['phonenumber'])
                list_destinations.append(destination)
            #return list_destinations
            print(list_destinations)


# john = Employee('100382-2389', 'steb stebson', 'Pilot', 'Captain', 'Boeing', '5686802', 'Flugmannavegur 3', 'refur34@gmail.com')
# input("Press enter to save John to file: ")
# john.save_employee()
# Employee.list_employee()