from Models.EmployeeMODEL import Employee
from Logic.LogicLayerAPI import LogicLayer
from Models.VoyageMODEL import Voyage

class HRInterface:

    def __init__(self, interface):
        self.__interface = interface
        self.__logicapi = LogicLayer()
        self.all_employees = self.__logicapi.list_all_employees()

        self.__menu_list = ["Back",
        "Register new employee - COMPLETE", "All employees - COMPLETE", "Edit employees - COMPLETE",
        "Captains - COMPLETE", "Co-Pilots - COMPLETE",
        "Flight service managers - COMPLETE", "Flight attendants - COMPLETE",
        "Register employees on voyage"]

        self.__menu_helper = self.__interface.menu_helper
        self.__clear = self.__interface.clear

    def menu(self):
        while True:
            command_str = self.__menu_helper("Human Resources", self.__menu_list)
            if command_str == "0":
                return
            elif command_str == "1":
                self.register_new_employee()
            elif command_str == "2":
                for employee in self.all_employees:
                    print (employee)
                input("press enter to return to main menu...")
            elif command_str == "3":
                self.change_employee()
            elif command_str == "4":
                for employee in self.all_employees:
                    if "Captain" in employee.__str__():
                        print (employee)
                input("press enter to return to main menu...")
            elif command_str == "5":
                for employee in self.all_employees:
                    if "Copilot" in employee.__str__():
                        print (employee)
                input("press enter to return to main menu...")
            elif command_str == "6":
                for employee in self.all_employees:
                    if "Flight Service Manager" in employee.__str__():
                        print (employee)
                input("press enter to return to main menu...")
            elif command_str == "7":
                for employee in self.all_employees:
                    if "Flight Attendant" in employee.__str__():
                        print (employee)
                input("press enter to return to main menu...")
            elif command_str == "8":
                #search_word = input("Please enter either flight numbers of the voyage you want to add on: ")
                #self.voyage = self.__logicapi.get_voyage_to_add_employee_on(search_word)
                print("Please enter what position you want to add to the voyage")
                self.position = self.get_position_for_voyage()
                self.target_employees = self.__logicapi.find_employees(self.position)
                for person in self.target_employees:
                    print(person)

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

    def get_position_for_voyage(self):
        position = input("1. Register Captain\t2. Register Co-pilot\t3. Register FSM\t4. Register FA\nSelect a position: ")
        options = ["1", "2", "3", "4"]
        while position not in options:
            print ("Invalid input! Please try again")
            new_position = input("1. Register Captain\t2. Register Co-pilot\t3. Register FSM\t4. Register FA\nSelect a position: ")
            position = new_position
        if position =="1":
            position = "Captain"
        elif position == "2":
            position = "Copilot"
        elif position == "3":
            position = "Flight Service Manager"
        elif position == "4":
            position = "Flight Attendant"
        return position

    def add_employee_to_voyage(self, ssn):
        #self.__logicapi.
        #self.employees.append(ssn)
        pass
    
    def change_employee(self):
        self.__clear()
        ssn = input("Enter employee SSN: ")
        employee_ssn = self.__logicapi.find_employees(ssn)
        try:
            print ("Employee details\n\n" + str(employee_ssn[0]))
            input("Press enter to continue...")
        except:
            input ("Employee not found, press enter to return to main menu")
            return
        if "Pilot" in employee_ssn:
            change_list = ["Main menu", "License", "Address", "Phone", "Email"]
            command_str = self.__menu_helper("Change Employee", change_list)
            if command_str == "0":
                return
            if command_str == "1":
                change = change_list[1]
            elif command_str == "2":
                change = change_list[2]
            elif command_str == "3":
                change = change_list[3]
            elif command_str == "4":
                change = change_list[4]
            if change and command_str:
                new_info = input("New " + change + ": ")
                self.__logicapi.change_employee(employee_ssn, change, new_info)
        elif "Cabincrew" in employee_ssn:
            change_list2 = ["Main menu", "address", "phone", "email"]
            command_str = self.__menu_helper("Change Employee", change_list2)
            if command_str == "0":
                return
            if command_str == "1":
                change = change_list[1]
            elif command_str == "2":
                change = change_list[2]
            elif command_str == "3":
                change = change_list[3]
            if change and command_str:
                new_info = input("New " + change + ": ")
                self.__logicapi.change_employee(employee_ssn, change, new_info)
    def register_new_employee(self):
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
        self.new_employee = Employee(self.ssn, self.name, self.role, self.rank, self.pilot_license, self.address, self.mobile_phone, self.email)
        self.__logicapi.register_employee(self.new_employee) # sends the employee to LLAP

