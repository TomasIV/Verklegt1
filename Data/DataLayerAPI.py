import csv
from Models.Employee import Employee

class DataLayer:
    def __init__(self):
        pass

    def save_employee(self, some_employee):
        '''Takes an instance of an employee and saves it in an employee file.
        If such file doesn't exist, it's created.'''
        with open("Crew.csv", "a") as employees:
            csv_writer = csv.writer(employees)
            list_of_attributes = [some_employee.__ssn, some_employee.__name, some_employee.__role, some_employee.__rank, some_employee.licence, some_employee.address, some_employee.mobile, some_employee.email]
            csv_writer.writerow(list_of_attributes)

    def list_employee(self):
        list_employee = []
        with open('employees.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                employee = Employee(row['ssn'], row['name'], row['role'], row['rank'], row['licence'], row['address'], row['phonenumber'], row['email'])
                list_employee.append(employee)
            #return list_employee
            print(list_employee)



# john = Employee('100382-2389', 'steb stebson', 'Pilot', 'Captain', 'Boeing', '5686802', 'Flugmannavegur 3', 'refur34@gmail.com')
# input("Press enter to save John to file: ")
# john.save_employee()
# Employee.list_employee()