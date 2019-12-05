from Logic.EmployeeLL import EmployeeLL

class LogicLayer:
    def __init__(self):
        self.__employee_worker = EmployeeLL()

    def register_employee(self, new_employee):
        self.__employee_worker.save_employee(new_employee) # Sends information about employee to Data