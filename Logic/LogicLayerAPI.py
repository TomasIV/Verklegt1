from Logic.EmployeeLL import EmployeeLL
from Logic.DestinationLL import DestinationLL
from Logic.AirplaneLL import AirplaneLL
from Logic.VoyageLL import VoyageLL

class LogicLayer:
    def __init__(self):
        self.__logic_employee = EmployeeLL()
        self.__logic_destination = DestinationLL()
        self.__logic_voyage = VoyageLL()
        self.__logic_airplane = AirplaneLL()

    def register_employee(self, new_employee):
        self.__logic_employee.save_employee(new_employee) # Sends information about employee to Data
    
    def list_all_employees(self):
        return self.__logic_employee.get_all_employees()
    
    def change_employee(self, ssn, what_to_change, new_info):
        self.__logic_employee.change_employee(ssn, what_to_change, new_info)

    def find_employees(self, search_word):
        return self.__logic_employee.find_employee(search_word)
    
    def list_all_destinations(self):
        return self.__logic_destination.list_all_destinations()
    
    def get_voyage_to_add_employee_on(self, search_word):
        return self.__logic_voyage.get_voyage_to_add_employee_on(search_word)
    
    def add_employee_to_voyage(self, ssn):
        return self.__logic_voyage.add_employee_to_voyage(ssn)

    def register_airplane(self, new_airplane):
        self.__logic_airplane.save_airplane(new_airplane)

    def register_destination(self, new_destination):
        return self.__logic_destination.save_destination(new_destination)

    
