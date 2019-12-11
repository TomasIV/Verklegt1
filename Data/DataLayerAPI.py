from Data.DestinationDL import DestinationDL
from Data.EmployeeDL import EmployeeDL
from Data.VoyageDL import VoyageDL
from Data.AirplaneDL import AirplaneDL
from Models.EmployeeMODEL import Employee
from Models.DestinationMODEL import Destination
from Models.VoyageMODEL import Voyage
from Models.AirplaneMODEL import Airplane
from Data.DestinationDL import DestinationDL
from Data.AircraftModelDL import PlaneModel

class DataLayer:
    def __init__(self):
        self.__data_employee = EmployeeDL()
        self.__data_destination = DestinationDL()
        self.__data_voyage = VoyageDL()
        self.__data_airplane = AirplaneDL()
        self.__data_airplane_model = PlaneModel()

    def save_employee(self, some_employee):
        self.__data_employee.save_employee(some_employee)
    
    def overwrite_employee_file(self, list_of_employees):
        self.__data_employee.overwrite_file(list_of_employees)

    def list_employee(self):
        return self.__data_employee.list_employee()

    def save_destinations(self,some_destination):
        self.__data_destination.save_destinations(some_destination)

    def list_destinations(self):
        return self.__data_destination.list_destinations()

    def list_voyages(self):
        return self.__data_voyage.list_voyages()
    
    def overwrite_voyages(self, list_of_voyages):
        self.__data_voyage.overwrite_file(list_of_voyages)

    def save_airplane(self, some_airplane):
        self.__data_airplane.save_airplane(some_airplane)

    def list_airplanes(self):
        return self.__data_airplane.list_all_airplanes()
    
    def overwrite_airplane_file(self, list_of_airplanes):
        self.__data_airplane.overwrite_file(list_of_airplanes)