from Data.DestinationDL import DestinationDL
from Data.EmployeeDL import EmployeeDL
from Models.Employee import Employee
from Models.Destination import Destination

class DataLayer:
    def __init__(self):
        self.__data_employee = EmployeeDL()
        self.__data_employee_list = EmployeeDL()
        self.__data_destination = DestinationDL()
        self.__data_destination_list = DestinationDL()

    def save_employee(self, some_employee):
        self.__data_employee.save_employee(some_employee)

    def list_employee(self):
        self.__data_employee_list.list_employee()

    def save_destinations(self):
        self.__data_destination.save_destinations(some_destination)

    def list_destinations(self):
        self.__data_destination_list.list_destination()


# john = Employee('100382-2389', 'steb stebson', 'Pilot', 'Captain', 'Boeing', '5686802', 'Flugmannavegur 3', 'refur34@gmail.com')
# input("Press enter to save John to file: ")
# john.save_employee()
# Employee.list_employee()