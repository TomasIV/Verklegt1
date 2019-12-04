from Models.Employee import Employee
from Logic.EmployeeLL import EmployeeLL
from UserInterface.HRInterface import HRInterface

class LogicLayer:
    def __init__(self):
        self.__employee_worker = EmployeeLL()

    def register_employee(self, new_employee):
        self.__employee_worker.save_employee(new_employee)