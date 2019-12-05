from Models.EmployeeMODEL import Employee
from Data.DataLayerAPI import DataLayer

class EmployeeLL:
    def __init__(self):
        self.__data_layer = DataLayer()

    def save_employee(self, new_employee):
        self.__data_layer.save_employee(new_employee)
    
    def find_employee(self, search_word):
        all_employees = self.__data_layer.list_employee()
        found_employees = []
        for person in all_employees:
            if person == search_word:
                found_employees.append(person)
        return found_employees
    
    def get_all_employees(self):
        return self.__data_layer.list_employee()