from Data.DestinationDL import DestinationDL
from Data.EmployeeDL import EmployeeDL
from Data.VoyageDL import VoyageDL
from Data.AirplainDL import AirplainDL
from Data.ModelDL import ModelDL
from Models.Employee import Employee
from Models.Destination import Destination
from Models.Voyage import Voyage
from Models.Airplane import Airplane
from Models.Model import Model

class DataLayer:
    def __init__(self):
        self.__data_employee = EmployeeDL()
        #self.__data_employee_list = EmployeeDL()
        self.__find_all_employees = EmployeeDL()
        self.__data_destination = DestinationDL()
        self.__data_destination_list = DestinationDL()

    def save_employee(self, some_employee):
        self.__data_employee.save_employee(some_employee)

    def find_employee(self):
        self.__find_all_employees.find_employee()

    
    # def list_employee(self):
    #     self.__data_employee_list.list_employee()

    def save_destinations(self,some_destination):
        self.__data_destination.save_destinations(some_destination)

    def list_destinations(self):
        self.__data_destination_list.list_destinations()

    


# john = Employee('100382-2389', 'steb stebson', 'Pilot', 'Captain', 'Boeing', '5686802', 'Flugmannavegur 3', 'refur34@gmail.com')
# input("Press enter to save John to file: ")
# john.save_employee()
# Employee.list_employee()