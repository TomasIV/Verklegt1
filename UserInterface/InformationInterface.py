from Logic.LogicLayerAPI import LogicLayer

class InformationInterface:
    def __init__(self, interface):
        self.__interface = interface
        self.all_employees = LogicLayer().list_all_employees()
        self.__menu_list = ["Back",
        "List all employees COMPLETE", "Employees on a voyage",
        "Most popular destinations", "All destinations COMPLETE",
        "Active voyages", "Old voyages", "Future voyages"]
        self.__clear = self.__interface.clear
        self.__menu_helper = self.__interface.menu_helper

    def menu(self):
        command_str = self.__menu_helper("Information", self.__menu_list)
        if command_str == "0":
            self.__interface.main_menu()
        elif command_str =="1":
            for employee in self.all_employees:
                print (employee)
            input ("Press enter to continue...")
        elif command_str == "4":
            destinations = LogicLayer().list_all_destinations()
            for destination in destinations:
                print (destination)
            input ("press enter to continue...")
