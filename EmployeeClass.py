class Employee(object):
    def __init__(self, name, SSN, landline, mobile_phone, address, email, role):
        # Fill out this yes
        self.__name = name
        self.__ssn = SSN
        self.landline = landline
        self.mobile = mobile_phone
        self.address = address
        self.email = email
        self.__role = role # NOTE: We're keeping this a private attribute for now, can be changed later
    
    def change_address(self):
        new_address = input("New name:")
        self.address = new_address


def make_employee():
    get_name = input("NAme:")
    get_ssn = input("SSN:")
    jhon_the_bitch = Employee(get_name, get_ssn)

def change_employee():
    jhon_the_bitch.change_address()