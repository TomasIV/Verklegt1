import csv
from Models.Employee import Employee

class DataLayer:
    def __init__(self):
        self.employee = Employee(self)

    def save_employee(self):
        '''Takes an instance of an employee and saves it in an employee file.
        If such file doesn't exist, it's created.'''
        with open("employees.csv", "a") as employees:
            list_of_attributes = [self.employee(self.__ssn, self.__name, self.__role, self.__rank, self.licence, self.address, self.mobile, self.email)]
            employees.write(','.join(list_of_attributes) + '\n')