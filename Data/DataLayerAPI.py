from Data.DestinationDL import DestinationDL
from Data.EmployeeDL import EmployeeDL
from Data.VoyageDL import VoyageDL
from Data.AirplainDL import AirplainDL
from Data.ModelDL import ModelDL
from Models.EmployeeMODEL import Employee
from Models.DestinationMODEL import Destination
from Models.VoyageMODEL import Voyage
from Models.Airplane import Airplane
from Models.Model import Model

class DataLayer:
    def __init__(self):
        self.__data_employee = EmployeeDL()
        #self.__data_employee_list = EmployeeDL()
        self.__data_destination = DestinationDL()
        self.__data_destination_list = DestinationDL()
        self.__data_voyage = VoyageDL()
        self.__data_voyage_list = VoyageDL()
        self.__data_airplane = AirplainDL()
        self.__data_airplanes_list = AirplainDL()
        self.__data_model = ModelDL()
        self.__data_model_list = ModelDL()

    def save_employee(self, some_employee):
        self.__data_employee.save_employee(some_employee)

    def find_employee(self):
        self.__data_employee.find_employee()

    # def list_employee(self):
    #     self.__data_employee_list.list_employee()

    def save_destinations(self,some_destination):
        self.__data_destination.save_destinations(some_destination)

    def list_destinations(self):
        self.__data_destination_list.list_destinations()

    def save_voyage(self, some_voyage):
        self.__data_voyage.save_voyage(some_voyage)

    def list_voyage(self):
        self.__data_voyage_list.list_voyage()

    def save_airplane(self, some_airplane):
        self.__data_airplane.save_airplane(some_airplane)

    def list_airplanes(self):
        self.__data_airplanes_list(self):

    def save_model(self, some_model):
        self.__data_model.save_model(some_model)

    def list_model(self):
        self.__data_model_list.list_model()



    

    


# john = Employee('100382-2389', 'steb stebson', 'Pilot', 'Captain', 'Boeing', '5686802', 'Flugmannavegur 3', 'refur34@gmail.com')
# input("Press enter to save John to file: ")
# john.save_employee()
# Employee.list_employee()