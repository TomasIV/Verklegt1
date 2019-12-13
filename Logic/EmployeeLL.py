from Models.EmployeeMODEL import Employee
from Models.VoyageMODEL import Voyage
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
    
    def get_all_employees_from_voyages(self, list_of_voyages):
        found_employees = []
        for voyage in list_of_voyages:
            employees = voyage.get_employees_on_voyage()
            for ssn in employees:
                person = self.find_employee(ssn)
                found_employees.extend(person)
        if found_employees == []:
            return ['No employees found...']
        else:
            return found_employees
    
    def get_all_employees(self):
        return self.__data_layer.list_employee()
    
    def change_employee(self, SSN_number, what_to_change, new_info):
        all_employees = self.__data_layer.list_employee()
        for num in range(len(all_employees)):
            if all_employees[num] == SSN_number:
                if what_to_change == 'license':
                    all_employees[num].license = new_info
                elif what_to_change == 'address':
                    all_employees[num].address = new_info
                elif what_to_change == 'phonenumber':
                    all_employees[num].mobile = new_info
                elif what_to_change == 'email':
                    all_employees[num].email = new_info
        self.__data_layer.overwrite_employee_file(all_employees)

    def get_ssn(self, some_bool):
        num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        ssn = 99
        while ssn:
            ssn = input("SSN: ").strip()
            new_ssn = ""
            for char in ssn:
                if char in num:
                    new_ssn += char
            if len(new_ssn) == 10:
                d = int(str(new_ssn[0] + new_ssn[1])) # takes the first and second int in the string as a day
                m = int(str(new_ssn[2] + new_ssn[3])) # takes third and second int in the string as a month
                y = int(str(new_ssn[4] + new_ssn[5])) # takes the fifth and sixth int in the string as a year
                last = int(new_ssn[-1]) # takes the last int in the string as a century
                if last == 0: #if year == 2000
                    if ((32 > d > 0 ) and ( 13 > m > 0) and (y < 20)):
                        if some_bool:
                            if not self.check_ssn(new_ssn):
                                return new_ssn
                            else:
                                print ("SSN already exists")
                        else:
                            return new_ssn
                    else:
                        print("SSN not valid")
                elif str(last) == "9": #if year == 1900
                    if (( 32 > d > 0 ) and (13 > m > 0)):
                        if some_bool:
                            if not self.check_ssn(new_ssn):
                                return new_ssn
                            else:
                                print ("SSN already exists")
                        else:
                            return new_ssn
                    else:
                        print("SSN not valid")
                else:
                    print ("SSN not valid")
            else:
                print ("SSN not valid")

    def check_ssn(self, ssn):
        """Checks if ssn is already registered to some employee"""
        ssn_list = []
        for employee in self.get_all_employees():
             ssn_list.append(employee.get_ssn())
        if ssn in ssn_list:
            return True
        else:
            return False