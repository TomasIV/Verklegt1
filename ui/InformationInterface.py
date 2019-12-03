class InformationInterface:
    def __init__(self, interface):
        self.__interface = interface

        self.__menu_list = ["Back",
        "List all employees", "Employees on a voyage",
        "Most popular destinations", "All destinations",
        "Active voyages", "Old voyages", "Future voyages"]
        self.__clear = self.__interface.clear
        self.__menu_helper = self.__interface.menu_helper

    def menu(self):
        command_str = self.__menu_helper("Information", self.__menu_list)
        if command_str == "0":
            self.__interface.main_menu()