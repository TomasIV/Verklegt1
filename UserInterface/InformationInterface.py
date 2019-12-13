import datetime
import dateutil
from Logic.LogicLayerAPI import LogicLayer
from Models.EmployeeMODEL import Employee

class InformationInterface:
    def __init__(self, interface):
        self.__interface = interface
        self.__logicapi = LogicLayer()
        self.__menu_list = ["Back",
        "List all employees", "Employees on a voyage",
        "Most popular destinations", "All destinations",
        "Active voyages", "Old voyages", "Future voyages"]
        self.__clear = self.__interface.clear
        self.__menu_helper = self.__interface.menu_helper

    def menu(self):
        while True:
            command_str = self.__menu_helper("Information", self.__menu_list)
            if command_str == "0":
                return
            elif command_str =="1":
                for employee in self.__logicapi.list_all_employees():
                    print (employee)
                input ("Press enter to continue...")
            elif command_str == "2":
                options = ["1", "2"]
                print("1. Today\t2. Other")
                chosen = self.__interface.get_input()
                while chosen not in options:
                    print ("Invalid input please try again")
                    chosen = self.__interface.get_input()
                if chosen == "1":
                    some_date = datetime.datetime.now().isoformat()
                    voyages = self.__logicapi.get_all_voyages_by_date(some_date, some_date)
                    if voyages == ['No voyages found...']:
                        print(voyages[0])
                    else:
                        employees = self.__logicapi.get_employees_from_voyages(voyages)
                        for person in employees:
                            print(person)
                elif chosen == "2":
                    some_date = self.__interface.get_voyage_date_without_time()
                    voyages = self.__logicapi.get_all_voyages_by_date(some_date, some_date)
                    if voyages == ['No voyages found...']:
                        print(voyages[0])
                    else:
                        employees = self.__logicapi.get_employees_from_voyages(voyages)
                        for person in employees:
                            print(person)
                input ("Press enter to continue...")
            elif command_str == "3":
                this_is_a_tuple = self.__logicapi.get_most_popular_destination()
                print("The most popular destination is {} with {} voyages documented".format(this_is_a_tuple[0], this_is_a_tuple[1]))
                input ("press enter to continue...")
            elif command_str == "4":
                destinations = LogicLayer().list_all_destinations()
                for destination in destinations:
                    print (destination)
                input ("press enter to continue...")
            elif command_str == "5":
                list_of_voyages = self.__logicapi.get_voyages_by_status('active')
                for voyage in list_of_voyages:
                    print(voyage)
                input ("press enter to continue...")
            elif command_str == "6":
                list_of_voyages = self.__logicapi.get_voyages_by_status('finished')
                for voyage in list_of_voyages:
                    print(voyage)
                input ("press enter to continue...")
            elif command_str == "7":
                list_of_voyages = self.__logicapi.get_voyages_by_status('upcoming')
                for voyage in list_of_voyages:
                    print(voyage)
                input ("press enter to continue...")
