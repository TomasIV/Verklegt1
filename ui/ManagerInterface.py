class ManagerInterface:
    def __init__(self, interface):
        self.__interface = interface
        
        self.__menu_list = ["Back", 
        "Register Airplane", "Register Voyage", "Register Destination", 
        "Edit Airplane", "Edit Voyage","Edit Destination", 
        "View Airplanes", "View Voyages","View Destinations"]
        self.__clear = self.__interface.clear
        self.__dash_divider = self.__interface.dash_divider
        self.__selection_msg_str = self.__interface.selection_msg_str
        self.__check_command = self.__interface.check_command

    def menu(self):
        self.__clear()

        print ("Manager")
        self.__selection_msg_str
        self.__dash_divider(self.__selection_msg_str)
        self.__interface.print_menu(self.__menu_list)
        self.__dash_divider(self.__selection_msg_str)
        options_commands = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        input_command_str = str(input("Select a number: "))
        command_str = self.__check_command(input_command_str, options_commands)
        print (command_str)
        if command_str == "0":
            self.__interface.main_menu()

