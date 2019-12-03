class HRInterface:
    def __init__(self, interface):
        self.__interface = interface

        self.__menu_list = ["Back",
        "Regist new employee", "All employees", "Edit employees",
        "Captains", "Co-Pilots",
        "Flight service managers", "Flight attendants",
        "Register employees on voyage"]

        self.__menu_helper = self.__interface.menu_helper
        self.__clear = self.__interface.clear

    def menu(self):
        command_str = self.__menu_helper("Human Resources", self.__menu_list)
        if command_str == "0":
            self.__interface.main_menu()

"""
	captain
	co pilot
	flight service manager
	flight attendant
    """