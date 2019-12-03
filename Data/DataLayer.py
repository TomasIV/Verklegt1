import csv
from Models.Employee import Employee

class DataLayer:
    def __init__(self):
        pass

    def save_employee(self, some_employee):
        '''Takes an instance of an employee and saves it in an employee file.
        If such file doesn't exist, it's created.'''
        with open("Crew.csv", "a") as employees:
            csv_writer = csv.writer(employees)
            list_of_attributes = [some_employee.__ssn, some_employee.__name, some_employee.__role, some_employee.__rank, some_employee.licence, some_employee.address, some_employee.mobile, some_employee.email]
            csv_writer.writerow(list_of_attributes)