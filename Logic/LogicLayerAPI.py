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
        """Finds employee/s by ssn and returns as list"""
        return self.__logic_employee.find_employee(search_word)
    
    def list_all_destinations(self):
        return self.__logic_destination.list_all_destinations()
    
    def change_destination(self, all_destinations, what_to_chagne, new_info):
        self.__logic_destination.change_destination(all_destinations, what_to_chagne, new_info)

    def get_voyage_to_add_employee_on(self, search_word):
        return self.__logic_voyage.get_voyage_to_add_employee_on(search_word)
    
    def add_employee_to_voyage(self, ssn):
        return self.__logic_voyage.add_employee_to_voyage(ssn)

    def register_airplane(self, new_airplane):
        self.__logic_airplane.save_airplane(new_airplane)

    def register_destination(self, new_destination):
        return self.__logic_destination.save_destination(new_destination)
    
    def list_all_airplanes(self):
        return self.__logic_airplane.list_airplanes()
    
    def change_airplane(self, plane_insignia, what_to_change, new_info):
        self.__logic_airplane.change_airplane(plane_insignia, what_to_change, new_info)

    def register_voyage(self, new_voyage, departure_sold_seats, arrival_sold_seats):
        self.__logic_voyage.create_voyage(new_voyage, departure_sold_seats, arrival_sold_seats)

    def find_destination(self, search_word):
        return self.__logic_destination.find_destination(search_word)
