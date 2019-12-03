class ManagerInterface:
    def __init__(self, interface):
        self.__interface = interface
        
        self.__menu_list = ["Back", 
        "Register Airplane", "Register Voyage", "Register Destination", 
        "Edit Airplane", "Edit Voyage","Edit Destination", 
        "View Airplanes", "View Voyages","View Destinations"]
        self.__clear = self.__interface.clear
        self.__menu_helper = self.__interface.menu_helper

    def menu(self):
        command_str = self.__menu_helper("Manager", self.__menu_list)
        if command_str == "0":
            self.__interface.main_menu()
        elif command_str == "1":
            print ("Wow!") # Class coming!
        elif command_str == "2":
            print ("Wow!") # Class coming!
        elif command_str == "3":
            print ("Wow!") # Class coming!
        elif command_str == "5":
            print ("Wow!") # Class coming!
        elif command_str == "6":
            print ("Wow!") # Class coming!
        elif command_str == "7":
            print ("Wow!") # Class coming!
        elif command_str == "8":
            print ("Wow!") # Class coming!
        elif command_str == "9":
            print ("Wow!") # Class coming!

