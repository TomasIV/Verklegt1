from Logic.EmployeeLL import EmployeeLL
from Logic.DestinationLL import DestinationLL

class LogicLayer:
    def __init__(self):
        self.__logic_employee = EmployeeLL()
        self.__logic_destination = DestinationLL()

    def register_employee(self, new_employee):
        self.__logic_employee.save_employee(new_employee) # Sends information about employee to Data
    
    def list_all_employees(self):
        return self.__logic_employee.get_all_employees()

    def find_employees(self, search_word):
        return self.__logic_employee.find_employee(search_word)
    
    def list_all_destinations(self):
        return self.__logic_destination.list_all_destinations()