from Logic.EmployeeLL import EmployeeLL

class LogicLayer:
    def __init__(self):
        self.__logic_employee = EmployeeLL()

    def register_employee(self, new_employee):
        self.__logic_employee.save_employee(new_employee) # Sends information about employee to Data
    
    def list_all_employees(self):
        return self.__logic_employee.get_all_employees()