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
        with open("employees.csv", "a") as employees:
            list_of_attributes = [self.__ssn, self.__name, self.__role, self.__rank, self.address, self.mobile, self.email]
            employees.write(','.join(list_of_attributes) + '\n')

    def change_employee(self):
        pass

    def __str__(self):
        '''Returns the employee information on a very pretty format'''
        the_line = "{:<20s}Licence: {}\n{:<20s}Role: {}\n{:<20s}Rank: {}\n{}\n{}".format(self.__ssn, self.licence, self.__name, self.__role, self.address, self.__rank, self.mobile, self.email)
        return the_line


def find_employee(ssn):
    '''Takes a ssn and finds the corresponding line in the employees.csv file.
    Returns the line in an instance of Employee.'''
    with open("employees.csv") as employees:
        employee_reader = csv.DictReader(employees)
        for row in employee_reader:
            if ssn == row['ssn']:
                return Employee(row['ssn'], row['name'], row['role'], row['rank'], row['licence'], row['address'], row['phonenumber'], row['email'])
        return 'Employee does not exist!'

# john = Employee('1003822389', 'John Stevenson Jr', 'Pilot', 'Captain', 'Boeing', '5686802', 'Flugmannavegur 3', 'refur34@gmail.com')
# input("Press enter to save John to file: ")
# john.save_employee()

# print(find_employee('0000003322'))