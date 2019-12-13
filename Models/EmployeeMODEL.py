class Employee:
    '''Employee class.
    It has eight attributes (besides "self").'''
    def __init__(self, ssn, name, role, rank, a_license, address, mobile_phone, email):
        self.__ssn = ssn
        self.__name = name
        self.__role = role
        self.__rank = rank
        self.license = a_license
        self.mobile = mobile_phone
        self.address = address
        self.email = email

    def __str__(self):
        '''Returns the employee information on a very pretty format'''
        the_line = "SSN     : {:<10s}\nName    : {:<30s} License : {}\nAddress : {:<30s} Role    : {:<20s}\nPhone   : {:<30s} Rank    : {}\nEmail   : {}\n".format(self.__ssn, self.__name, self.license, self.address, self.__role, self.mobile, self.__rank, self.email)      
        return the_line

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

    def get_employee_attributes(self):
        '''Returnes the employee attributes in a list'''
        return [self.__ssn, self.__name, self.__role, self.__rank, self.license, self.address, self.mobile, self.email]

    def get_ssn(self):
        '''Returnes the social security number as a string'''
        return self.__ssn

    def get_role(self):
        '''Returnes the role of an employee'''
        return self.__role

    def get_license(self):
        '''Returnes the license of an employee'''
        return self.license

    def get_rank(self):
        '''Returnes the rank of an employee'''
        return self.__rank