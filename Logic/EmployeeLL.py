from Models.EmployeeMODEL import Employee
from Data.DataLayerAPI import DataLayer

class EmployeeLL:
    def __init__(self):
        self.__data_layer = DataLayer()

    def save_employee(self, new_employee):
        self.__data_layer.save_employee(new_employee)
    
    def find_employee(self, search_key="rank", some_variable=["Captain", "Copilot", "Flight Service Manager", "Flight Attendant"]):
        '''Takes a ssn and finds the corresponding line in the employees.csv file.
        Returns the line in an instance of Employee.'''
        # Anna: Er að breyta þessu falli
        with open("Crew.csv", "r") as employees:
            employee_reader = csv.DictReader(employees)
            list_of_employees = []
            for row in employee_reader:
                if row[search_key] in some_variable:
                    list_of_employees.append(Employee(row['ssn'], row['name'], row['role'], row['rank'], row['licence'], row['address'], row['phonenumber'], row['email']))
            return list_of_employees