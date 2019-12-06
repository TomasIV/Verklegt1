class Employee:
    def __init__(self, ssn, name, role, rank, licence, address, mobile_phone, email):
        self.__ssn = ssn
        self.__name = name
        self.__role = role # NOTE: We're keeping this a private attribute for now, can be changed later
        self.__rank = rank # Same here
        self.licence = licence
        self.mobile = mobile_phone
        self.address = address
        self.email = email

    def __str__(self):
        '''Returns the employee information on a very pretty format'''
        the_line = "SSN     : {:<10s}\nName    : {:<30s} License : {}\nAddress : {:<30s} Role    : {:<20s}\nPhone   : {:<30s} Rank    : {}\nEmail   : {}\n".format(self.__ssn, self.__name, self.licence, self.address, self.__role, self.mobile, self.__rank, self.email)
                    #ssn       #name         #licence   #address #role    #rank #mobile #email         
        return the_line

    '''How the lsit is suppose to print'''
        #SSN
        #Name       Licence 
        #Address    Role 
        #Moblie     Rank
        #Email 

    def get_employee_attributes(self):
        return [self.__ssn, self.__name, self.__role, self.__rank, self.licence, self.address, self.mobile, self.email]

    def __eq__(self, comparison):
        if self.__ssn == comparison \
        or self.__name == comparison \
        or self.__role == comparison \
        or self.__rank == comparison \
        or self.licence == comparison \
        or self.address == comparison \
        or self.mobile == comparison \
        or self.email == comparison:
            return True
        else:
            return False
        