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
    
    def change_destination(self, the_destination, what_to_change, new_info):
        self.__logic_destination.change_destination(the_destination, what_to_change, new_info)

    def register_voyage(self, new_voyage):
        self.__logic_voyage.create_voyage(new_voyage)
    
    def add_employee_to_voyage(self, some_voyage, role, ssn):
        return self.__logic_voyage.add_employee_to_voyage(some_voyage, role, ssn, self.list_all_airplanes())
    
    def get_all_voyages_by_date(self, from_date, to_date):
        return self.__logic_voyage.get_all_voyages_by_date(from_date, to_date)

    def view_all_voyages(self):
        return self.__logic_voyage.get_all_voyages()

    def find_voyage(self, flight_num, date):
        return self.__logic_voyage.find_voyage(flight_num, date)

    def register_airplane(self, new_airplane):
        self.__logic_airplane.save_airplane(new_airplane)

    def register_destination(self, new_destination):
        return self.__logic_destination.save_destination(new_destination)
    
    def list_all_airplanes(self):
        return self.__logic_airplane.list_airplanes()
    
    def get_airplane_status(self, some_plane, some_date):
        return self.__logic_airplane.get_airplane_status(some_plane, some_date)

    def find_destination(self, search_word):
        return self.__logic_destination.find_destination(search_word)
    
<<<<<<< HEAD
    def get_employee_ssn(self, new_ssn = ""):
        return self.__logic_employee.get_ssn(True)

    def voyage_time(self, date_time):
        return self.__logic_voyage.voyage_time_check(date_time)
=======
    def get_employee_ssn(self, some_bool):
        return self.__logic_employee.get_ssn(some_bool)
>>>>>>> 23ddb512e9a68ba7e1500c9666b5886af38e8bba
