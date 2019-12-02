import os
from ui.ManagerInterface import ManagerInterface

class Interface:

    def __init__(self):
        #self.hr = HumanResourcesInterface(self)
        #self.info = GeneralInformation(self)

        self.selection_msg_str = "Select one of the following options"
        self.__main_menu_list = ["Exit", "Human Resources", "Manager", "General Information"]
        self.manager = ManagerInterface(self)
    def print_menu(self, main_menu_list):
        if len (main_menu_list) < 11:
            for index, text in enumerate(main_menu_list):
                print ("{:<3}{}".format(str(index) + ".", text))
        else:
            for index, text in enumerate(main_menu_list):
                print ("{:<4}{}".format(str(index) + ".", text))

    def dash_divider(self, a_str):
        """Prints dashes after length of word"""
        print ("-"*len(str(a_str)))

    def clear(self):
        os.system("cls")

    def check_command(self, command, options):
        while command not in options:
            print ("Invalid input, please try again")
            command = str(input("Select a number: "))
        return command

    def main_menu(self):
        """Prentar út main menu"""
        self.clear()
        print ("Welcome to NaN Air")
        print (self.selection_msg_str)
        options_commands = ["0", "1", "2", "3"]
        self.dash_divider(self.selection_msg_str)
        self.print_menu(self.__main_menu_list)
        self.dash_divider(self.selection_msg_str)

        input_command_str = str(input("Enter a number: "))
        command_str = self.check_command(input_command_str, options_commands)
        if command_str == "0":
            self.clear()
            print ("Thanks for using our program")
        elif command_str == "1":
            pass
            #self.hr.menu()
        elif command_str == "2":
            self.manager.menu()
        elif command_str == "3":
            pass
            #self.info.menu()

"""
def manager():
    os.system('cls')
    title = "MANAGER MENU"
    options =["1", "2", "3", "4"]

    print (title)
    print ("-"*LENGTH)
    print ("1. Airplanes")
    print ("2. Destinations")
    print ("3. Voyages")
    print ("4. Back to main menu")
    print ("-"*LENGTH)

    command = str(input("Select category: "))

    command = check_command(command, options)
    if command == "1":
        airplanes()
    elif command == "2":
        destinations()
    elif command == "3":
        voyages()
    elif command == "4":
        start_menu()


def airplanes():
    os.system('cls')
    title = "AIRPLANES"
    options =["1", "2", "3", "4"]

    print (title)
    print ("-"*LENGTH)
    print ("1. Register airplane")
    print ("2. Existing airplanes")
    print ("3. Edit Existing airplane")
    print ("4. Back")
    print ("-"*LENGTH)

    command = str(input("Select category: "))

    command = check_command(command, options)
    if command == "1":
        os.system('cls')
        print ("WOW, you registered an airplane")
        go_back = input("PRESS ENTER TO GO BACK")
        if go_back:
            airplanes()
        else:
            airplanes()
    elif command == "2":
        os.system('cls')
        print ("WOW, you got a list of airplanes")
        go_back = input("PRESS ENTER TO GO BACK")
        if go_back:
            airplanes()
        else:
            airplanes()
    elif command == "3":
        os.system('cls')
        print ("WOW, you managed to edit an airplane")
        go_back = input("PRESS ENTER TO GO BACK")
        if go_back:
            airplanes()
        else:
            airplanes()
    elif command == "4":
        manager()


def destinations():
    os.system('cls')
    title = "DESTINATIONS"
    options =["1", "2", "3", "4"]


    print (title)
    print ("-"*LENGTH)
    print ("1. Register destination")
    print ("2. Existing destinations")
    print ("3. Edit Existing destination")
    print ("4. Back")
    print ("-"*LENGTH)

    command = str(input("Select category: "))

    command = check_command(command, options)
    if command == "1":
        os.system('cls')
        print ("WOW, you registered a destination")
        go_back = input("PRESS ENTER TO GO BACK")
        if go_back:
            destinations()
        else:
            destinations()
    elif command == "2":
        os.system('cls')
        print ("WOW, you got a list of destinations")
        go_back = input("PRESS ENTER TO GO BACK")
        if go_back:
            destinations()
        else:
            destinations()
    elif command == "3":
        os.system('cls')
        print ("WOW, you managed to edit a destination")
        go_back = input("PRESS ENTER TO GO BACK")
        if go_back:
            destinations()
        else:
            destinations()
    elif command == "4":
        manager()

def voyages():
    os.system('cls')
    title = "VOYAGES"
    options =["1", "2", "3", "4"]

    print (title)
    print ("-"*LENGTH)
    print ("1. Register voyage")
    print ("2. Existing voyages")
    print ("3. Edit Existing voyage")
    print ("4. Back")
    print ("-"*LENGTH)

    command = str(input("Select category: "))

    command = check_command(command, options)
    if command == "1":
        os.system('cls')
        print ("WOW, you registered a voyage")
        go_back = input("PRESS ENTER TO GO BACK")
        if go_back:
            voyages()
        else:
            voyages()
    elif command == "2":
        os.system('cls')
        print ("WOW, you got a list of voyages")
        go_back = input("PRESS ENTER TO GO BACK")
        if go_back:
            voyages()
        else:
            voyages()
    elif command == "3":
        os.system('cls')
        print ("WOW, you managed to edit a voyage")
        go_back = input("PRESS ENTER TO GO BACK")
        if go_back:
            voyages()
        else:
            voyages()
    elif command == "4":
        manager()
"""