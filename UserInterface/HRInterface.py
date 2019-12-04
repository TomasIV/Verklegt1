from Models.Employee import Employee
from Logic.LogicLayer

class HRInterface:
    def __init__(self, interface):
        self.__interface = interface

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
            ssn = input("SSN: ")
            name = input("Name: ")
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
                pilot_license = input("Enter a license")
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
            new_employee = Employee(ssn, name, role, rank, pilot_license, address, mobile_phone, email)
            print ("Wow! you created an employee!")
        def get_employee_ssn(self):
            self.__ssn = input("SSN: ")

        def get_employee_name(self):
            self.__name = input("Name: ")

        def get_employee_role(self):
            self.__role = input("1. Pilot\t2. CabinCrew\nSelect a role: ")

        def get_pilot_license(self):
            #Print License selection list
            self.license = input("Select a License")

        def get_pilot_rank(self):
            self.employee_rank = input("1. Captain\t2. Co-Pilot\nSelect a rank: ")
        
        def get_cabin_rank(self):
            self.employee_rank = input("1. Flight Service Manager\t2. Flight Attendant\nSelect a rank: ")

"""
	captain
	co pilot
	flight service manager
	flight attendant
    """