import os
import msvcrt

from UserInterface.ManagerInterface import ManagerInterface
from UserInterface.HRInterface import HRInterface
from UserInterface.InformationInterface import InformationInterface


class Interface:

    def __init__(self):
        self.selection_msg_str = "Select one of the following options"
        self.__main_menu_list = ["Exit", "Human Resources", "Manager", "Information"]

        self.manager = ManagerInterface(self)
        self.hr = HRInterface(self)
        self.info = InformationInterface(self)


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
    

    def menu_helper(self, name, menu_list):
        """Creates a working menu with error check from a title and a list of options to perform"""
        self.clear()
        print (name)
        self.selection_msg_str
        self.dash_divider(self.selection_msg_str)
        self.print_menu(menu_list)
        self.dash_divider(self.selection_msg_str)
        options = []
        for index in range(len(menu_list)):
            options.append(str(index))
        input_command_str = input("select a number: ")
        command_str = self.check_command(input_command_str, options)
        return command_str
        

    def main_menu(self):
        """Prentar út main menu"""
        while True:
            self.clear()
            print ("Welcome to NaN Air")
            print (self.selection_msg_str)
            options_commands = ["0", "1", "2", "3"]
            self.dash_divider(self.selection_msg_str)
            self.print_menu(self.__main_menu_list)
            self.dash_divider(self.selection_msg_str)

            input_command_str =  str(input("Enter a number: "))
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