import os
from UserInterface.ManagerInterface import ManagerInterface
from UserInterface.HRInterface import HRInterface
from UserInterface.InformationInterface import InformationInterface
from sys import platform
try:
    import msvcrt
except:
    pass #virkar ekki a fokking mac, what a bitch os

class Interface:

    def __init__(self):
        self.selection_msg_str = "Select one of the following options"
        self.__main_menu_list = ["Exit", "Human Resources", "Manager", "Information"]

        self.manager = ManagerInterface(self)
        self.hr = HRInterface(self)
        self.info = InformationInterface(self)


    def print_menu(self, main_menu_list):
        """Printer for menu"""
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
        """Clears the screen"""
        if platform == "win32" or "win64":
            os.system("cls")
        else:
            os.system("clear")


    def check_command(self, command, options):
        """Checks to see if the command is valid (in the options list)"""
        while command not in options:
            print ("Invalid input, please try again")
            #command = str(input("Select a number: "))
            print ("Select a number")
            if platform == "win32" or "win64":
                command_input = msvcrt.getch()
                command_input_str = str (command_input)
                command = command_input_str[2]
            else:
                command = input("Enter a number you mac bitch: ")
        return str(command)
    

    def menu_helper(self, name, menu_list):
        """Creates a working menu with error check from a title and a list of options to perform"""
        self.clear()
        longest_string = ""
        for string in menu_list:
            if len(string) > len(longest_string):
                longest_string = string
        print (name)
        longest_string += "123"
        self.dash_divider(longest_string)
        self.print_menu(menu_list)
        self.dash_divider(longest_string)
        options = []
        for index in range(len(menu_list)):
            options.append(str(index))
        input_command_str = self.get_input()
        command_str = self.check_command(input_command_str, options)
        return command_str

    def get_input(self):
        """Takes input from using without pressing enter"""
        try:
            user_input = msvcrt.getch() # Takes input in form of b'char' without pressing enter
            user_input_str = str(user_input) #Converts to string
            return user_input_str[2] #Return the char pressed
        except:
            return input("Enter something wrong u mac ReTaRd")


    def main_menu(self):
        """Prentar út main menu"""
        while True:
            self.clear()
            print ("{:>24s}".format("welcome to")) # 38 over
            na = "    _   __      _   __   ___    _     "
            n =  "   / | / /___ _/ | / /  /   |  (_)____"
            a =  "  /  |/ / __ `/  |/ /  / /| | / / ___/" # Lengsti strengur í main menu printinu
            i =  " / /|  / /_/ / /|  /  / ___ |/ / /    "
            r =  "/_/ |_/\__,_/_/ |_/  /_/  |_/_/_/     \n"                              
            nan_air = [na, n, a, i, r]
            for element in nan_air:#Prentar út text artið fyrir ofan
                print (element)
            print (self.selection_msg_str)
            options_commands = ["0", "1", "2", "3"] # options sem hægt er að velja frá menu-inu
            self.dash_divider(a) # til að fá út dashes jafn mikið og lengsti strengur sem upp kemur í printinu
            self.print_menu(self.__main_menu_list) # Main menu verður til út frá lista
            self.dash_divider(a) # lína 82

            input_command_str = self.get_input()
            #input_command_str =  str(input("Enter a number: "))
            command_str = self.check_command(input_command_str, options_commands)
            if command_str == "0":
                self.clear()
                print ("Thanks for using our program")
                break
            elif command_str == "1":
                self.hr.menu()
            elif command_str == "2":
                self.manager.menu()
            elif command_str == "3":
                self.info.menu()