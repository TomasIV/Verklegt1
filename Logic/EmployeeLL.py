from Models.EmployeeMODEL import Employee
from Data.DataLayerAPI import DataLayer

class EmployeeLL:
    def __init__(self):
        self.__data_layer = DataLayer()

    def save_employee(self, new_employee):
        self.__data_layer.save_employee(new_employee)
    
    def find_employee(self, search_word):
        all_employees = self.__data_layer.list_employee()
        found_employees = []
        for person in all_employees:
            if person == search_word:
                found_employees.append(person)
        return found_employees
    
    def get_all_employees(self):
        return self.__data_layer.list_employee()
    
    def change_employee(self, SSN_number, what_to_change, new_info):
        all_employees = self.__data_layer.list_employee()
        for num in range(len(all_employees)):
            if all_employees[num] == SSN_number:
                if what_to_change == 'license':
                    all_employees[num].licence = new_info
                elif what_to_change == 'address':
                    all_employees[num].address = new_info
                elif what_to_change == 'phone':
                    all_employees[num].mobile = new_info
                elif what_to_change == 'email':
                    all_employees[num].email = new_info
        self.__data_layer.overwrite_employee_file(all_employees)