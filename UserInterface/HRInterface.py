from Models.EmployeeMODEL import Employee
from Logic.LogicLayerAPI import LogicLayer
from Models.VoyageMODEL import Voyage

class HRInterface:

    def __init__(self, interface):
        self.__interface = interface
        self.__logicapi = LogicLayer()
        self.all_employees = self.__logicapi.list_all_employees()

        self.__menu_list = ["Back",
        'Edit employees', 'Find Pilot for specific airplane', 'Find employee',
        'List Employees', 'Register employees on voyage', 'Register new employee', "Is employee on duty", "List employees work schedule"]

        self.__list_menu = ["Back",
        "Employees", "Pilots", "Captains",
        "Co-Pilots", "Cabin Crew",
        "Flight Service Managers", "Flight Attendants"]
        self.__menu_helper = self.__interface.menu_helper
        self.__clear = self.__interface.clear

    def menu(self):
        while True:
            command_str = self.__menu_helper("Human Resources", self.__menu_list)
            if command_str == "0":
                return
            elif command_str == "1":
                self.change_employee()
            elif command_str =="2":
                self.find_pilots_by_license()
            elif command_str == "3":
                employee = self.find_employee()
                try:
                    print ("\n" + str(employee[0]))
                except:
                    print ("Employee not found, press enter to return...")
                input("press enter to return...")
            elif command_str == "4":
                self.list_menu()
            elif command_str == "5":
                some_voyage = self.__interface.find_voyage()
                print("Please enter what position you want to add to the voyage")
                role = self.get_position_for_voyage()
                some_bool = False
                ssn = self.__logicapi.get_employee_ssn(some_bool)
                self.__logicapi.add_employee_to_voyage(some_voyage, role, ssn)
                input("press enter to return...")
            elif command_str == "6":
                self.register_new_employee()
            elif command_str == "7":
                print ("1. Working\t2. Not Working")
                a_command = self.__interface.get_input()
                options = ["1", "2"]
                while a_command not in options:
                    print ("Invalid input, please try again!")
                    a_command = self.__interface.get_input()
                if a_command == "1":
                    print ("Enter a date")
                    a_date = self.__interface.get_voyage_date_without_time()
                    voyages_day = self.__logicapi.get_all_voyages_by_date(a_date, a_date)
                    for voyage in voyages_day:
                        try:
                            for element in voyage.get_employees_on_voyage():
                                if len(element) > 9:
                                    print (str(element) + " going to " + voyage.get_destination())
                        except:
                            pass
                    input("Press enter to continue...")
                elif a_command == "2":
                    ignore_list = []
                    all_employees = self.__logicapi.list_all_employees()
                    print ("Enter a date")
                    a_date = self.__interface.get_voyage_date_without_time()
                    voyages_day = self.__logicapi.get_all_voyages_by_date(a_date, a_date)
                    for voyage in voyages_day:
                        try:
                            for element in voyage.get_employees_on_voyage():
                                if len(element) > 9:
                                    ignore_list.append(element)
                        except:
                            pass
                    for element in all_employees:
                        if element not in ignore_list:
                            print (element)
                    input("Press enter to continue...")
        
            elif command_str == "8":
                options = ["1", "2"]
                print ("1. Day" + "\t" + "2. from date, to date")
                chosen = self.__interface.get_input()
                some_bool = False
                ssn = self.__logicapi.get_employee_ssn(some_bool)
                while chosen not in options:
                    print ("Invalid input please try again")
                    chosen = self.__interface.get_input()
                if chosen == "1":
                    from_date = self.__interface.get_voyage_date_without_time()
                    voyages_day = self.__logicapi.get_all_voyages_by_date(from_date, from_date)
                    for voyage in voyages_day:
                        if ssn in voyage.get_employees_on_voyage():
                            print (voyage)
                    input("Press enter to return...")
                elif chosen == "2":
                    input ("First enter in a date to start with and next the end date\npress enter to continute...")
                    print ("input the 'from' date")
                    from_date = self.__interface.get_voyage_date_without_time()
                    print ("input the 'to' date")
                    to_date = self.__interface.get_voyage_date_without_time()
                    voyages = self.__logicapi.get_all_voyages_by_date(from_date, to_date)
                    for voyage in voyages:
                        if ssn in voyage.get_employees_on_voyage():
                            print ("\n" + str(voyage))
                    input ("\nPress enter to return...")


    def list_menu(self):
        
        while True:
            command_str = self.__interface.menu_helper("Employee Lists", self.__list_menu)
            if command_str == "0":
                return
            elif command_str == "1":
                for employee in self.all_employees:
                    print (employee)
                input("press enter to return...")
            elif command_str == "2":
                for element in sorted(self.all_employees, key=lambda x: x.get_license()):
                    if element.get_role() == "Pilot":
                        print (element)
                input ("press enter to return...")
            elif command_str == "3":
                for employee in self.all_employees:
                    if "Captain" in employee.__str__():
                        print (employee)
                input("press enter to return...")
            elif command_str == "4":
                for employee in self.all_employees:
                    if "Copilot" in employee.__str__():
                        print (employee)
                input("press enter to return...")
            elif command_str == "5":
                for employee in sorted(self.all_employees, key=lambda x: x.get_rank()):
                    if employee.get_role() == "Cabincrew":
                        print (employee)
                input ("press enter to return...")
            elif command_str == "6":
                for employee in self.all_employees:
                    if "Flight Service Manager" in employee.__str__():
                        print (employee)
                input("press enter to return...")
            elif command_str == "7":
                for employee in self.all_employees:
                    if "Flight Attendant" in employee.__str__():
                        print (employee)
                input("press enter to return...")

                   
    def get_employee_name(self):
        return input("Name: ")

    def get_employee_role(self):
        print ("1. Pilot\t2. CabinCrew\tSelect a role: ")
        role = self.__interface.get_input()
        options = ["1", "2"]
        while role not in options:
            print ("Invalid input! Please try again")
            print ("1. Pilot\t2. CabinCrew\tSelect a role: ")
            new_role = self.__interface.get_input()
            role = new_role
        if role =="1":
            role = "Pilot"
        elif role == "2":
            role = "Cabincrew"
        return role
    
    def get_pilot_license(self):
        print ("1. NAFokkerF100\t2. NAFokkerF28\t3. NABAE146\tSelect a license")
        options = ["1", "2", "3"]
        pilot_license = self.__interface.get_input()
        while pilot_license not in options:
            print ("Invalid input, please try again!")
            print ("1. NAFokkerF100\t2. NAFokkerF28\t3. NABAE146\tSelect a license")
            new_pilot_license = self.__interface.get_input()
            pilot_license = new_pilot_license
        if pilot_license == "1":
            the_license = "NAFokkerF100"
        elif pilot_license == "2":
            the_license = "NAFokkerF28"
        elif pilot_license == "3":
            the_license = "NABAE146"
        return the_license

        
    def get_pilot_rank(self):
        options = ["1", "2"]
        print ("1. Captain\t2. Co-Pilot\tSelect a rank")
        rank = self.__interface.get_input()
        while rank not in options:
            print ("Invalid input! Please try again")
            print ("1. Captain\t2. Co-Pilot\nSelect a rank: ")
            rank = self.__interface.get_input()
        if rank == "1":
            rank = "Captain"
        elif rank == "2":
            rank = "Copilot"
        return rank
    
    def get_cabincrew_rank(self):
        options = ["1", "2"]
        print ("1. Flight Service Manager\t2. Flight Attendant\tSelect a rank: ")
        rank = self.__interface.get_input()
        while rank not in options:
            print ("Invalid input! Please try again")
            print ("1. Flight Service Manager\t2. Flight Attendant\tSelect a rank: ")
            new_rank = self.__interface.get_input()
            rank = new_rank
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
                print ("Invalid input, please try again!")

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
        print ("1. Register Captain\t2. Register Co-pilot\t3. Register FSM\t4. Register FA\nSelect a position: ")
        position = self.__interface.get_input()
        options = ["1", "2", "3", "4"]
        while position not in options:
            print ("Invalid input! Please try again")
            print ("1. Register Captain\t2. Register Co-pilot\t3. Register FSM\t4. Register FA\nSelect a position: ")
            position = self.__interface.get_input()
        if position =="1":
            position = "Captain"
        elif position == "2":
            position = "Copilot"
        elif position == "3":
            position = "Flight Service Manager"
        elif position == "4":
            position = "Flight Attendant"
        return position
    
    def find_pilots_by_license(self):
        all_employees = self.all_employees
        menu_options = ["1", "2", "3"]
        print ("1. NAFokkerF28\t2. NAFokkerF100\t3. NABAE146\tSelect a license")
        command_str = self.__interface.get_input()
        while command_str not in menu_options:
            print("Invaldi input, please try again")
            print ("1. NAFokkerF28\t2. NAFokkerF100\t3. NABAE146\tSelect a license")
            command_str = self.__interface.get_input()
        pilot_list = []
        menu_list = ["NAFokkerF28", "NAFokkerF100", "NABAE146"]
        selected_license = menu_list[int(command_str)-1]
        for employee in all_employees:
            if selected_license in employee.__str__():
                pilot_list.append(employee)
        for pilot in pilot_list:
            print (pilot)
        input("Press enter to continue...")

    def find_employee(self):
        self.__clear()
        ssn = input("Enter employee SSN: ")
        employee = self.__logicapi.find_employees(ssn)
        return employee

    def change_employee(self):
        self.__clear()
        ssn = input("Enter employee SSN: ")
        employee_ssn = self.__logicapi.find_employees(ssn)
        try:
            print ("Employee details\n\n" + str(employee_ssn[0]))
            input ("press enter to continute...")
        except:
            input ("Employee not found, press enter to return")
            return
        if "Pilot" in employee_ssn:
            change_list = ["Back", "License", "Address", "Phone", "Email"]
            command_str = self.__menu_helper("Change Employee", change_list)
            if command_str == "0":
                return
            if command_str == "1":
                change = "license"
                new_info = self.get_pilot_license()
            elif command_str == "2":
                change = "address"
                new_info = self.get_employee_address()
            elif command_str == "3":
                change = "phonenumber"
                new_info = self.get_employee_num()
            elif command_str == "4":
                change = "email"
                new_info = self.get_employee_email()
            if change:
                self.__logicapi.change_employee(employee_ssn[0].get_ssn(), change, new_info)
        elif "Cabincrew" in employee_ssn:
            change_list2 = ["Back", "address", "phone", "email"]
            command_str = self.__menu_helper("Change Employee", change_list2)
            if command_str == "0":
                return
            if command_str == "1":
                change = "address"
                new_info = self.get_employee_address()
            elif command_str == "2":
                change = "phonenumber"
                new_info = self.get_employee_num()
            elif command_str == "3":
                change = "email"
                new_info = self.get_employee_email()
            if change:
                self.__logicapi.change_employee(employee_ssn[0].get_ssn(), change, new_info)
                
    def register_new_employee(self):
        print ("Please enter the details of the new employee")
        some_bool = True
        self.ssn = self.__logicapi.get_employee_ssn(some_bool)
        self.name = self.get_employee_name()
        self.role = self.get_employee_role()
        if self.role == "Pilot":
            self.pilot_license = self.get_pilot_license()
            self.rank = self.get_pilot_rank()       
        elif self.role == "Cabincrew":
            self.pilot_license = "N/A"
            self.rank = self.get_cabincrew_rank()
        self.address = self.get_employee_address()
        self.mobile_phone = self.get_employee_num()
        self.email = self.get_employee_email()
        input("Wow! you created an employee, press enter to continue")
        self.new_employee = Employee(self.ssn, self.name, self.role, self.rank, self.pilot_license, self.address, self.mobile_phone, self.email)
        self.__logicapi.register_employee(self.new_employee) # sends the employee to LLAP
