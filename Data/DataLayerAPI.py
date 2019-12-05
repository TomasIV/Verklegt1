from Data.DestinationDL import DestinationDL
from Data.EmployeeDL import EmployeeDL
#from Data.VoyageDL import VoyageDL
#from Data.AirplaneDL import AirplaneDL
#from Data.ModelDL import ModelDL
from Models.EmployeeMODEL import Employee
from Models.DestinationMODEL import Destination
from Models.VoyageMODEL import Voyage
from Models.AirplaneMODEL import Airplane
#from Models.Model import Model

class DataLayer:
    def __init__(self):
        self.__data_employee = EmployeeDL()
        self.__data_destination = DestinationDL()
        #self.__data_voyage = VoyageDL()
        #self.__data_airplane = AirplaneDL()
        #self.__data_model = ModelDL()

    def save_employee(self, some_employee):
        self.__data_employee.save_employee(some_employee)

    def list_employee(self):
        return self.__data_employee.list_employee()

    def save_destinations(self,some_destination):
        self.__data_destination.save_destinations(some_destination)

    def list_destinations(self):
        return self.__data_destination.list_destinations()

    def save_voyage(self, some_voyage):
        self.__data_voyage.save_voyage(some_voyage)

    def list_voyage(self):
        return self.__data_voyage.list_voyage()

    def save_airplane(self, some_airplane):
        self.__data_airplane.save_airplane(some_airplane)

    def list_airplanes(self):
        return self.__data_airplane.list_airplanes()

    def save_model(self, some_model):
        self.__data_model.save_model(some_model)

    def list_model(self):
        return self.__data_model.list_model()



    

    


# john = Employee('100382-2389', 'steb stebson', 'Pilot', 'Captain', 'Boeing', '5686802', 'Flugmannavegur 3', 'refur34@gmail.com')
# input("Press enter to save John to file: ")
# john.save_employee()
# Employee.list_employee()