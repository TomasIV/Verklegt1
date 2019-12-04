class Employee:
    def __init__(self, SSN, name, role, rank, licence, address, mobile_phone, email):
        self.__name = name
        self.__ssn = SSN
        self.mobile = mobile_phone
        self.address = address
        self.email = email
        self.__role = role # NOTE: We're keeping this a private attribute for now, can be changed later
        self.__rank = rank # Same here
        self.licence = licence

    def __str__(self):
        '''Returns the employee information on a very pretty format'''
        the_line = "{:<20s}Licence: {}\n{:<20s}Role: {}\n{:<20s}Rank: {}\n{}\n{}".format(self.__ssn, self.licence, self.__name, self.__role, self.address, self.__rank, self.mobile, self.email)
        return the_line
    
    def add_employee(self):
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
        Employee(ssn, name, role, rank, pilot_license, address, mobile_phone, email)
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
        self.__name = name
        self.__ssn = SSN
        self.mobile = mobile_phone
        self.address = address
        self.email = email
        self.__role = role # NOTE: We're keeping this a private attribute for now, can be changed later
        self.__rank = rank # Same here
        self.licence = licence
"""