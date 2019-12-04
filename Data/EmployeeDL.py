from Models.Employee import Employee
from Data.DataLayerAPI import DataLayer

class EmployeeDL:
    def __init__(self):
        self.__data_layer = DataLayer()

    def save_employee(self, some_employee):
        '''Takes an instance of an employee and saves it in an employee file.
        If such file doesn't exist, it's created.'''
        self.some_employee = some_employee
        with open("Data\employees.csv", "a") as employees:
            csv_writer = csv.writer(employees)
            #list_of_attributes = [self.some_employee.ssn, self.some_employee.name, self.some_employee.role, self.some_employee.rank, self.some_employee.licence, self.some_employee.address, self.some_employee.mobile, self.some_employee.email]
            csv_writer.writerow(some_employee)
