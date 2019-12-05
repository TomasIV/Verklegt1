from Models.EmployeeMODEL import Employee
from Logic.LogicLayerAPI import LogicLayer

class HRInterface:
    def __init__(self, interface):
        self.__interface = interface
        self.__logicapi = LogicLayer()

        self.__menu_list = ["Back",
        "Register new employee - COMPLETE", "All employees - ALMOST COMPLETED(smá formatting)", "Edit employees",
        "Captains", "Co-Pilots",
        "Flight service managers", "Flight attendants",
        "Register employees on voyage"]

        self.__menu_helper = self.__interface.menu_helper
        self.__clear = self.__interface.clear

    def menu(self):
        command_str = self.__menu_helper("Human Resources", self.__menu_list)
        if command_str == "0":
            return
        elif command_str == "1":
            print ("Please enter the details of the new employee")
            self.ssn = self.get_employee_ssn()
            self.name = self.get_employee_name()
            self.role = self.get_employee_role()
            if self.role == "Pilot":
                self.pilot_license = self.get_pilot_license()
                self.rank = self.get_pilot_rank()       
            elif self.role == "Cabincrew":
                self.rank = self.get_cabincrew_rank()
            self.address = self.get_employee_address()
            self.mobile_phone = self.get_employee_num()
            self.email = self.get_employee_email()
            input("Wow! you created an employee, press enter to continue")
            self.new_employee = Employee(self.ssn, self.name, self.role, self.pilot_license, self.rank, self.address, self.mobile_phone, self.email)
            self.__logicapi.register_employee(self.new_employee) # sends the employee to LLAPI
        elif command_str == "2":
            all_employees = self.__logicapi.list_all_employees()
            for employee in all_employees:
                print (employee)
            input ("press enter to continue")
           
    def get_employee_ssn(self):
        num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        ssn = 99
        while ssn:
            ssn = input("SSN: ").strip()
            new_ssn = ""
            for char in ssn:
                if char in num:
                    new_ssn += char
            if len(new_ssn) == 10:
                d = int(str(new_ssn[0] + new_ssn[1]))
                m = int(str(new_ssn[2] + new_ssn[3]))
                y = int(str(new_ssn[4] + new_ssn[5]))
                last = int(new_ssn[-1])
                if last == 0: #if year == 2000
                    if ((32 > d > 0 ) and ( 13 > m > 0) and (y < 20)):
                        return new_ssn
                    else:
                        print("SSN not valid")
                elif str(last) == "9": #if year == 1900
                    if (( 32 > d > 0 ) and (13 > m > 0)):
                        return new_ssn
                    else:
                        print("SSN not valid")
                else:
                    print ("SSN not valid")
            else:
                print ("SSN not valid")
            
                
    def get_employee_name(self):
        return input("Name: ")

    def get_employee_role(self):
        role = input("1. Pilot\t2. CabinCrew\tSelect a role: ")
        options = ["1", "2"]
        while role not in options:
            print ("Invalid input! Please try again")
            new_role = input("1. Pilot\t2. CabinCrew\tSelect a role: ")
            role = new_role
        if role =="1":
            role = "Pilot"
        elif role == "2":
            role = "Cabin crew"
        return role
    
    def get_pilot_license(self):
        return input("License: ") #VANTAR LISTA AF FLUGVÉLUM Í OKKAR EIGU
        
    def get_pilot_rank(self):
        options = ["1", "2"]
        rank = input("1. Captain\t2. Co-Pilot\nSelect a rank: ")
        while rank not in options:
            print ("Invalid input! Please try again")
            rank = input("1. Captain\t2. Co-Pilot\nSelect a rank: ")
        if rank == "1":
            rank = "Captain"
        elif rank == "2":
            rank = "Copilot"
        return rank
    
    def get_cabincrew_rank(self):
        options = ["1", "2"]
        rank = input("1. Flight Service Manager\t2. Flight Attendant\tSelect a rank: ")
        while rank not in options:
            print ("Invalid input! Please try again")
            rank = input("1. Flight Service Manager\t2. Flight Attendant\tSelect a rank: ")
        if rank == "1":
            rank = "Flight Service Manager"
        elif rank == "2":
            rank = "Flight Attendant" 
        return rank

    def get_employee_address(self):
        return input("Employee address: ")

    def get_employee_num(self):
        num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        while True:
            phone_num = input("Phone number: ")
            new_num = ""
            for char in phone_num:
                if char in num:
                    new_num += char
            if len(new_num) == 7:
                return new_num
            else:
                print ("Invalid input, pleaes try again!")

    def get_employee_email(self):
        while True:
            email = input("Employee email: ")
            first = ""
            mid = ""
            last = ""
            name = True
            for char in email:
                if name:
                    if char != "@":
                        first += char
                    elif char == "@":
                        mid += "@"
                        name = False
                else:
                    last += char
            if "." in last:
                email = first + mid + last
                return email
            else:
                print ("Invalid input, please try again!")