class ManagerInterface:
    def __init__(self, interface):
        self.__interface = interface
        
        self.__menu_list = ["Back", 
        "Register Airplane", "Register Voyage", "Register Destination", 
        "Edit Airplane", "Edit Voyage","Edit Destination", 
        "View Airplanes", "View Voyages","View Destinations"]
        self.__clear = self.__interface.clear
        self.__menu_helper = self.__interface.menu_helper


    def menu(self): # Kóði virkar en eftir að tengja hann við API
        command_str = self.__menu_helper("Manager", self.__menu_list)
        if command_str == "0":
            self.__interface.main_menu()
        elif command_str == "1":
            print ("Please enter the details of the new airplae")
            self.name = self.get_airplane_name()
            self.manufacturer = self.get_airplane_manufacturer()
            if self.manufacturer == "BAE":
                self.model = self.get_airplane_bae_model()
            elif self.manufacturer == "Fokker":
                self.model = self.get_airplane_fokker_model()
            elif self.manufacturer != "Fokker" or self.manufacturer != "BAE":
                self.model = self.get_airplane_other_model()
            self.capacity = self.get_airplane_capacity()
            self.new_airplane = Airplane(self.name, self.model, self.manufacturer, self.capacity)
            self.__logicapi.register_airplane(self.new_airplane) # sends the airplane to LLAPI
        elif command_str == "2":
            print ("Wow!") # Class coming!
        elif command_str == "3":
            print("Please enter the details of the new Destination")
            self.ids = self.get_destination_id()
            self.destination = self.get_destination_name()
            self.emergency_contact = self.get_destination_emergency_contact()
            self.emergency_phone = self.get_destination_emegency_phone()
            self.new_destination = Destination(self.ids, self.destination, self.emergency_contact, self.emergency_phone)
            self.__logicapi.register_destination(self.new_destination) # sends the destination to LLAPI
        elif command_str == "5":
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

    def get_airplane_name(self):
        return input("PlaneID: ")

    def get_airplane_manufacturer(self):
        manufacturer = input("Manufacturer: \n1. BAE\n2. Fokker\n3. Other manufacturer \nSelect Manufacturer: ")
        manufacturer_options = ["1", "2", "3"]
        while manufacturer not in manufacturer_options:
            print ("Invalid input! Please try again")
            new_manufacturer = input("Manufacturer: \n1. BAE\n2. Fokker\n3. Input other manufacturer \nSelect Manufacturer: ")
            manufacturer = new_manufacturer
        if manufacturer == "1":
            manufacturer = "BAE"
        elif manufacturer == "2":
            manufacturer = "Fokker"
        elif manufacturer == "3":
            manufacturer = input("Input other Manufacturer: ")
        return manufacturer

    def get_airplane_bae_model(self):
        model = input("Model \n1. Model 148\n2. Other Model \nSelect Model: ")
        model_options = ["1", "2"]
        while model not in model_options:
            print("Invalid input! Please try again")
            model = input("Model \n1. Model 148\n2. Other Model \nSelect Model: ")
        if model == "1":
            model = "148"
        elif model == "2":
            model = input("Input other Model: ")
        return model

    def get_airplane_fokker_model(self):
        model = input("Model \n1. Model F28\n2. Model F100\n3. Other Model \nSelect Model: ")
        model_options = ["1", "2", "3"]
        while model not in model_options:
            print("Invalid input! Please try again")
            model = input("Model \n1. Model F28\n2. Model F100\n3. Other Model \nSelect Model: ")
        if model == "1":
            model = "F28"
        elif model == "2":
            model = "F100"
        elif model == "3":
            model = model = input("Input other Model: ")
        return model

    def get_airplane_other_model(self):
        return input("Input model number: ")

    def get_airplane_capacity(self):
        num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        while True:
            capacity = input("Capacity: ")
            new_num = ""
            for char in capacity:
                if char in num:
                    new_num += char
            if 0 < len(new_num) < 4:
                return new_num
            else: 
                print("Invalid input, please try again!")

    def get_destination_id(self):
        return input("Input destination ID: ")

    def get_destination_name(self):
        return input("Input destination name: ")

    def get_destination_emergency_contact(self):
        return input("Input emergency contact: ")

    def get_destination_emegency_phone(self):
        num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        while True:
            em_phone = input("Input emergency phone number: ")
            new_em_phone = ""
            for char in em_phone:
                if char in num:
                    new_em_phone += char
            if 0 < len(new_em_phone) < 15: # MAx 15 vegna lengd númera í útlöndum
                return new_em_phone
            else:
                print("Invalid input, please try again!")