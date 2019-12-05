import csv
# ALLT HÉR ER EKKI 100% RÉTT, ÞETTA ER Í VINNSLU
# ÞÚ STENDUR ÞIG VEL!
# TAKK :)


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

    def get_employee_attributes(self):
        return [self.__ssn, self.__name, self.__role, self.__rank, self.licence, self.address, self.mobile, self.email]
    

    def change_employee(self, SSN_number, what_to_change, new_info):
        #licence, address, mobile_phone, email
        self.all_employees = self.find_employee()
        for row in range(len(self.all_employees)):
            if self.all_employees[row].__ssn == SSN_number:
                if what_to_change == 'license':
                    self.all_employees[row].licence = new_info
                elif what_to_change == 'address':
                    self.all_employees[row].address = new_info
                elif what_to_change == 'phone':
                    self.all_employees[row].mobile = new_info
                elif what_to_change == 'email':
                    self.all_employees[row].email = new_info
            with open("Crew.csv", "w") as cleared_file:
                for person in self.all_employees:
                    overwriter = csv.writer(cleared_file)
                    overwriter.writerow(person.get_employee_attributes())


    def __str__(self):
        '''Returns the employee information on a very pretty format'''
        the_line = "{:<20s}Licence: {}\n{:<20s}Role: {}\n{:<20s}Rank: {}\n{}\n{}".format(self.__ssn, self.licence, self.__name, self.__role, self.address, self.__rank, self.mobile, self.email)
        return the_line

    def find_employee(self, search_key="rank", some_variable=["Captain", "Copilot", "Flight Service Manager", "Flight Attendant"]):
        '''Takes a ssn and finds the corresponding line in the employees.csv file.
        Returns the line in an instance of Employee.'''
        with open("Crew.csv", "r") as employees:
            employee_reader = csv.DictReader(employees)
            list_of_employees = []
            for row in employee_reader:
                if row[search_key] in some_variable:
                    list_of_employees.append(Employee(row['ssn'], row['name'], row['role'], row['rank'], row['licence'], row['address'], row['phonenumber'], row['email']))
            return list_of_employees

john = Employee('1003822389', 'John Stevenson Jr', 'Pilot', 'Captain', 'Boeing', '5686802', 'Flugmannavegur 3', 'refur34@gmail.com')
# input("Press enter to save John to file: ")
# petur = john.change_employee("ssn", "1900769521", "address", "Efstasund 32")

john.change_employee("2910858778", "address", "Efstasund 32")

# petur = john.find_employee("ssn", ["2910858778"])

# for em in petur:
#     print(em)
