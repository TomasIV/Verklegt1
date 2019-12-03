import csv

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

    def save_employee(self):
        '''Takes an instance of an employee and saves it in an employee file.
        If such file doesn't exist, it's created.'''
        employees = open("employees.csv", "a")
        list_of_attributes = [self.__ssn, self.__name, self.__role, self.__rank, self.address, self.mobile, self.email]
        employees.write(','.join(list_of_attributes) + '\n')
        employees.close()

    def change_employee(self):
        pass


def find_employee(ssn):
    employees = open("employees.csv")

john = Employee('100382-2389', 'John Stevenson Jr', 'Pilot', 'Captain', 'Boeing', '5686802', 'Flugmannavegur 3', 'refur34@gmail.com')
input("Press enter to save John to file: ")
john.save_employee()