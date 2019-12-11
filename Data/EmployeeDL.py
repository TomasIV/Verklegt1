import csv
from Models.EmployeeMODEL import Employee

class EmployeeDL:
    PATH = "CSVFiles/Employees.csv"
    def __init__(self):
        pass

    def save_employee(self, some_employee):
        '''Takes an instance of an employee and saves it in an employee file.
        If such file doesn't exist, it's created.'''
        self.some_employee = some_employee
        with open(self.PATH, "a") as employees:
            csv_writer = csv.writer(employees, lineterminator= "\r")
            #list_of_attributes = [self.some_employee.ssn, self.some_employee.name, self.some_employee.role, self.some_employee.rank, self.some_employee.licence, self.some_employee.address, self.some_employee.mobile, self.some_employee.email]
            csv_writer.writerow(some_employee.get_employee_attributes())

    def list_employee(self):
        '''Takes an employee file and reads all employees from it.
        Returns a list of all employees.'''
        list_employee = []
        with open(self.PATH, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                employee = Employee(row['ssn'], row['name'], row['role'], row['rank'], row['licence'], row['address'], row['phonenumber'], row['email'])
                list_employee.append(employee)
            return list_employee
    
    def overwrite_file(self, list_of_employees):
        with open(self.PATH, "w", encoding="utf-8") as cleared_file:
            overwriter = csv.writer(cleared_file, lineterminator= "\r")
            overwriter.writerow(['ssn', 'name', 'role', 'rank', 'licence', 'address', 'phonenumber', 'email'])
            for person in list_of_employees:
                overwriter.writerow(person.get_employee_attributes())