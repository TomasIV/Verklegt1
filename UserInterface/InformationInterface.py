from Logic.LogicLayerAPI import LogicLayer

class InformationInterface:
    def __init__(self, interface):
        self.__interface = interface
        self.all_employees = LogicLayer().list_all_employees()
        self.__menu_list = ["Back",
        "List all employees", "Employees on a voyage NSFW",
        "Most popular destinations NSFW", "All destinations",
        "Active voyages NSFW", "Old voyages NSFW", "Future voyages NSFW"]
        self.__clear = self.__interface.clear
        self.__menu_helper = self.__interface.menu_helper

    def menu(self):
        while True:
            command_str = self.__menu_helper("Information", self.__menu_list)
            if command_str == "0":
                return
            elif command_str =="1":
                for employee in self.all_employees:
                    print (employee)
                input ("Press enter to continue...")
            elif command_str == "4":
                destinations = LogicLayer().list_all_destinations()
                for destination in destinations:
                    print (destination)
                input ("press enter to continue...")
