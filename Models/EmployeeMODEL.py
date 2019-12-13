class Employee:
    '''here you can get empolyee, list them nicely and get the info'''
    def __init__(self, ssn, name, role, rank, a_license, address, mobile_phone, email):
        self.__ssn = ssn
        self.__name = name
        self.__role = role # NOTE: We're keeping this a private attribute for now, can be changed later
        self.__rank = rank # Same here
        self.license = a_license
        self.mobile = mobile_phone
        self.address = address
        self.email = email
    def busy(self, departure_time, arrival_time, all_voyages):
        for voyage in all_voyages:
            cond_1 = (departure_time[:9] == voyage.get_voyage_depart_time()[:9])
            cond_2 = (arrival_time[:9] == voyage.get_arrival()[:9])
            if self.__ssn in voyage.get_employees_on_voyage():
                if (cond_1 or cond_2):
                    return True
                else:
                    return False
            else:
                return False

    def __str__(self):
        '''Returns the employee information on a very pretty format'''
        the_line = "SSN     : {:<10s}\nName    : {:<30s} License : {}\nAddress : {:<30s} Role    : {:<20s}\nPhone   : {:<30s} Rank    : {}\nEmail   : {}\n".format(self.__ssn, self.__name, self.license, self.address, self.__role, self.mobile, self.__rank, self.email)
                    #ssn       #name         #license   #address #role    #rank #mobile #email         
        return the_line
    def get_ssn(self):
        return self.__ssn
    def get_role(self):
        return self.__role
    def get_license(self):
        return self.license
    def get_rank(self):
        return self.__rank

    def get_employee_attributes(self):
        return [self.__ssn, self.__name, self.__role, self.__rank, self.license, self.address, self.mobile, self.email]

    def __eq__(self, comparison):
        if self.__ssn == comparison \
        or self.__name == comparison \
        or self.__role == comparison \
        or self.__rank == comparison \
        or self.license == comparison \
        or self.address == comparison \
        or self.mobile == comparison \
        or self.email == comparison:
            return True
        else:
            return False
        