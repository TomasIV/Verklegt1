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
        the_line = "{:<20s}Licence: {}\n{:<20s}Role: {}\n{:<20s}Rank: {}\n{}\n{}".format(self.__ssn, self.licence, self.__name, self.__role, self.address, self.__rank, self.mobile, self.email)
        return the_line
    
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
        