class Employee(object):
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