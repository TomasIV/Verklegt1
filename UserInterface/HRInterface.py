from Models.Employee import Employee
from Logic.LogicLayerAPI import LogicLayer
from string import punctuation

class HRInterface:
    def __init__(self, interface):
        self.__interface = interface
        self.__logicapi = LogicLayer()
        self.__menu_list = ["Back",
        "Register new employee", "All employees", "Edit employees",
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
            role = input("1. Pilot\t2. CabinCrew\nSelect a role: ")
            options = ["1", "2"]
            while role not in options:
                print ("Invalid input! Please try again")
                new_role = input("1. Pilot\t2. CabinCrew\nSelect a role: ")
                role = new_role
            if role =="1":
                role = "Pilot"
            elif role == "2":
                role = "Cabin crew"
            if role == "Pilot":
                pilot_license = input("Enter a license: ")
                rank = input("1. Captain\t2. Co-Pilot\nSelect a rank: ")
                while rank not in options:
                    print ("Invalid input! Please try again")
                    rank = input("1. Captain\t2. Co-Pilot\nSelect a rank: ")
                if rank == "1":
                    rank = "Captain"
                elif rank == "2":
                    rank = "Copilot"       
            elif role == "Cabincrew":
                rank = input("1. Flight Service Manager\t2. Flight Attendant\nSelect a rank: ")
                while rank not in rank:
                    print ("Invalid input! Please try again")
                    rank = input("1. Flight Service Manager\t2. Flight Attendant\nSelect a rank: ")
                if rank == "1":
                    rank = "Flight Service Manager"
                elif rank == "2":
                    rank = "Flight Attendant"  
            address = input("Employee address: ")
            mobile_phone = input("Employee phone number: ")
            email = input("Employee email: ")
            print ("Wow! you created an employee!")
            self.new_employee = Employee(ssn, name, role, pilot_license, rank, address, mobile_phone, email)
            self.__logicapi.register_employee(self.new_employee) # sends the employee to LLAPI
           
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
        self.__role = input("1. Pilot\t2. CabinCrew\nSelect a role: ")


    def get_pilot_license(self):
        #Print License selection list
        self.license = input("Select a License")

    def get_pilot_rank(self):
        self.employee_rank = input("1. Captain\t2. Co-Pilot\nSelect a rank: ")
    
    def get_cabin_rank(self):
        self.employee_rank = input("1. Flight Service Manager\t2. Flight Attendant\nSelect a rank: ")
    
    def error_check_ssn(self, ssn):
        pass
            
"""

	captain
	co pilot
	flight service manager
	flight attendant
"""