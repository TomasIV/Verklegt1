class Employee(object):
    def __init__(self, SSN, name, role, rank, landline, mobile_phone, address, email):
        self.__name = name
        self.__ssn = SSN
        self.landline = landline
        self.mobile = mobile_phone
        self.address = address
        self.email = email
        self.__role = role # NOTE: We're keeping this a private attribute for now, can be changed later
        self.__rank = rank

    def save_employee(self):
        employees = open("employees.csv", "a+")
        list_of_attributes = [self.__ssn, self.__name, self.__role, self.__rank, self.landline, self.mobile, self.address, self.email]
        employees.write(','.join(list_of_attributes) + '\n')
        employees.close()

    def change_employee(self):
        pass

john = Employee('100382-2389', 'John Stevenson Jr', 'Pilot', 'Captain', '5812345', '5686802', 'Flugmannavegur 3', 'refur34@gmail.com')
input("Press enter to save John:")
john.save_employee()