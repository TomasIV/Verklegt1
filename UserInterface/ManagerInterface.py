from Models.VoyageMODEL import Voyage
from Models.AirplaneMODEL import Airplane
from Logic.LogicLayerAPI import LogicLayer
from Models.DestinationMODEL import Destination
import string
import dateutil
import datetime

class ManagerInterface:
    def __init__(self, interface):
        self.__interface = interface
        #self.__voyage = Voyage()
        self.__logicapi = LogicLayer()
        self.__menu_list = ["Back", 
        "Register Airplane", "Register Voyage", "Register Destination", 
        "Edit Voyage NSFW", "Edit Destination", 
        "View Airplanes", "View Voyages","View Destinations", "Voyages in a certain week/day"]
        self.__clear = self.__interface.clear
        self.__menu_helper = self.__interface.menu_helper


    def menu(self):
        while True:
            command_str = self.__menu_helper("Manager", self.__menu_list)
            if command_str == "0":
                return
            elif command_str == "1":
                print ("Please enter new airplane")
                self.name = self.get_airplane_name()
                self.model = self.get_airplane_model()
                self.new_airplane = Airplane(self.name, self.model)
                self.__logicapi.register_airplane(self.new_airplane)
                input ("Airplane created, press enter to continue...")
                # self.name = self.get_airplane_name()
                # self.manufacturer = self.get_airplane_manufacturer()
                # if self.manufacturer == "BAE":
                #     self.model = self.get_airplane_bae_model()
                # elif self.manufacturer == "Fokker":
                #     self.model = self.get_airplane_fokker_model()
                # elif self.manufacturer != "Fokker" or self.manufacturer != "BAE":
                #     self.model = self.get_airplane_other_model()
                # self.capacity = self.get_airplane_capacity()
                # self.new_airplane = Airplane(self.name, self.model, self.manufacturer, self.capacity)
                # self.__logicapi.register_airplane(self.new_airplane) # sends the airplane to LLAPI
            elif command_str == "2":
                print ("Please enter a new voyage")
                print ("Please enter date and time of departure")
                self.departure_date_time = self.__interface.get_voyage_date()
                self.voyage_destination = self.get_voyage_destination()
                print ("Please enter number of sold seats for departure flight")
                self.departure_sold_seats = self.get_voyage_sold_seats()
                print ("Please enter number of sold seats for arrival flight")
                self.arrival_sold_seats = self.get_voyage_sold_seats()
                self.voyage_airplane_id = self.get_voyage_airplane()
                while self.voyage_airplane_id not in self.__logicapi.list_all_airplanes():
                    print ("Invalid input, please try again")
                    self.voyage_airplane_id = self.get_voyage_airplane()
                self.new_voyage = Voyage(self.voyage_airplane_id, self.voyage_destination, self.departure_sold_seats, self.arrival_sold_seats, self.departure_date_time)
                self.__logicapi.register_voyage(self.new_voyage)
                input("Voyage created, press enter to continue...")
            elif command_str == "3":
                print("Please enter the details of the new Destination")
                self.ids = self.get_destination_id()
                self.destination = self.get_destination_name()
                self.destination_number = self.get_destination_number()
                self.emergency_contact = self.get_destination_emergency_contact()
                self.emergency_phone = self.get_destination_emergency_phone()
                self.flight_time = self.get_flight_time()
                self.kilometers= self.get_km()
                self.new_destination = Destination(self.ids, self.destination, self.destination_number, self.emergency_contact, self.emergency_phone, self.flight_time, self.kilometers)
                self.__logicapi.register_destination(self.new_destination) # sends the destination to LLAPI
                input("Destination created, press enter to continue...")
            elif command_str == "4":
                print ("Please enter date and time of departure")
                some_date = self.__interface.get_voyage_date()
                print("Please enter a flight number")
                some_number = input("Flight number: ")
                a_voyage = self.__logicapi.find_voyage(some_number, some_date)
                print (a_voyage)
                input("Press enter to return...")
                #self.__logicapi.change_voyage(a_voyage, )
            elif command_str == "5":
                self.change_destination()
            elif command_str == "6":
                options = ["1", "2"]
                print("1. Status for today\t2. Status for some specific day")
                chosen = self.__interface.get_input()
                while chosen not in options:
                    print ("Invalid input please try again")
                    chosen = self.__interface.get_input()
                all_airplanes = self.__logicapi.list_all_airplanes()
                if chosen == "1":
                    for airplane in all_airplanes:
                        status = self.__logicapi.get_airplane_status(airplane, datetime.datetime.now().isoformat())
                        airplane.add_status(status)
                        print (airplane)
                elif chosen == "2":
                    some_date = self.__interface.get_voyage_date()
                    for airplane in all_airplanes:
                        status = self.__logicapi.get_airplane_status(airplane, some_date)
                        airplane.add_status(status)
                        print (airplane)
                input ("Presss enter to return......")
            elif command_str == "7":
                self.view_voyage()
            elif command_str == "8":
                all_destinations = self.__logicapi.list_all_destinations()
                for destinations in all_destinations:
                    print (destinations)
                input ("Press enter to return...")
            elif command_str == "9":
                options = ["1", "2"]
                print ("1. Day" + "\t" + "2. Week",)
                chosen = self.__interface.get_input()
                while chosen not in options:
                    print ("Invalid input please try again")
                    chosen = self.__interface.get_input()
                if chosen == "1":
                    from_date = self.__interface.get_voyage_date_without_time()
                    voyages_day = self.__logicapi.get_all_voyages_by_date(from_date, from_date)
                    for voyage in voyages_day:
                        print (voyage)
                    input("Press enter to return...")
                elif chosen == "2":
                    input ("First enter in a date to start with and next the end date\npress enter to continute...")
                    print("Starting date")
                    from_date = self.__interface.get_voyage_date_without_time()
                    print("End date")
                    to_date = self.__interface.get_voyage_date_without_time()
                    voyages = self.__logicapi.get_all_voyages_by_date(from_date, to_date)
                    for voyage in voyages:
                        print (voyage)
                    input ("\nPress enter to return...")


                
                
    def get_voyages_on_specific_day(self):
        voyages = self.__logicapi.view_all_voyages()
        date = self.__interface.get_voyage_date_without_time()
        voyage_day_list = []
        for voyage in voyages:
            voyage_date = voyage.get_voyage_depart_time()
            if date[:9] == voyage_date[:9]:
                voyage_day_list.append(voyage)
        return voyage_day_list
    def get_km(self):
        return input("Kilometers from Iceland to Destination: ")
    
    def get_flight_time(self):
        return input("Time from Iceland to Destination: ")

    def get_airplane_name(self):
        while True:
            plane_insignia = input("Plane Insignia: ")
            new_plane_insignia = ""
            if len(plane_insignia.replace("-", "")) == 5:
                for char in plane_insignia:
                    if char in string.ascii_letters:
                        new_plane_insignia += char
            if len(new_plane_insignia) == 5:
                a_str = new_plane_insignia[:2] + "-" + new_plane_insignia[2:]
                return a_str
            else:
                print ("Invalid input, please try again!")

    def get_airplane_model(self):
        print("Model \n1. NAFokkerF100\n2. NAFokkerF28 \n3. NABAE146 \nSelect Model: ")
        model = self.__interface.get_input()
        model_options = ["1", "2", "3"]
        while model not in model_options:
            print("Invalid input! Please try again")
            print("Model \n1. NAFokkerF100\n2. NAFokkerF28 \n3. NABAE146 \nSelect Model: ")
            model = self.__interface.get_input()
        if model == "1":
            model = "NAFokkerF100"
        elif model == "2":
            model = "NAFokkerF28"
        elif model == "3":
            model = "NABAE146"
        return model

    def change_airplane(self):
        pass
    # def get_airplane_name(self):
    #     return input("PlaneID: ")

    # def get_airplane_manufacturer(self):
    #     manufacturer = input("Manufacturer: \n1. BAE\n2. Fokker\n3. Other manufacturer \nSelect Manufacturer: ")
    #     manufacturer_options = ["1", "2", "3"]
    #     while manufacturer not in manufacturer_options:
    #         print ("Invalid input! Please try again")
    #         new_manufacturer = input("Manufacturer: \n1. BAE\n2. Fokker\n3. Input other manufacturer \nSelect Manufacturer: ")
    #         manufacturer = new_manufacturer
    #     if manufacturer == "1":
    #         manufacturer = "BAE"
    #     elif manufacturer == "2":
    #         manufacturer = "Fokker"
    #     elif manufacturer == "3":
    #         manufacturer = input("Input other Manufacturer: ")
    #     return manufacturer

    # def get_airplane_bae_model(self):
    #     model = input("Model \n1. Model 148\n2. Other Model \nSelect Model: ")
    #     model_options = ["1", "2"]
    #     while model not in model_options:
    #         print("Invalid input! Please try again")
    #         model = input("Model \n1. Model 148\n2. Other Model \nSelect Model: ")
    #     if model == "1":
    #         model = "148"
    #     elif model == "2":
    #         model = input("Input other Model: ")
    #     return model

    # def get_airplane_fokker_model(self):
    #     model = input("Model \n1. Model F28\n2. Model F100\n3. Other Model \nSelect Model: ")
    #     model_options = ["1", "2", "3"]
    #     while model not in model_options:
    #         print("Invalid input! Please try again")
    #         model = input("Model \n1. Model F28\n2. Model F100\n3. Other Model \nSelect Model: ")
    #     if model == "1":
    #         model = "F28"
    #     elif model == "2":
    #         model = "F100"
    #     elif model == "3":
    #         model = model = input("Input other Model: ")
    #     return model

    # def get_airplane_other_model(self):
    #     return input("Input model number: ")

    # def get_airplane_capacity(self):
    #     num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    #     while True:
    #         capacity = input("Capacity: ")
    #         new_num = ""
    #         for char in capacity:
    #             if char in num:
    #                 new_num += char
    #         if 0 < len(new_num) < 4:
    #             return new_num
    #         else: 
    #             print("Invalid input, please try again!")

    # def get_voyage_sold_seats(self):
    #     num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    #     while True:
    #         sold_seats = input("Sold Seats: ")
    #         new_num = ""
    #         for char in sold_seats:
    #             if char in num:
    #                 new_num += char
    #         if 0 < len(new_num) < 4:
    #             return new_num
    #         else: 
    #             print("Invalid input, please try again!")

    # def get_voyage_airplane(self):
    #     pass

    # def get_voyage_date(self):
    #     pass


    def get_destination_id(self):
        return input("Input destination ID: ")

    def get_destination_name(self):
        return input("Input destination name: ")

    def get_destination_emergency_contact(self):
        return input("Input emergency contact: ")

    def get_destination_emergency_phone(self):
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

    def get_voyage_sold_seats(self):
        num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        while True:
            sold_seats = input("Sold Seats: ")
            new_num = ""
            for char in sold_seats:
                if char in num:
                    new_num += char
                if 0 < len(new_num) < 4:
                    return new_num
                else: 
                    print("Invalid input, please try again!")

    def get_voyage_airplane(self):
        voyage_airplane_id = input("Enter Airplane ID for voyage: ")
        return voyage_airplane_id
        #Búa til brú niður í LL þar sem athugað er hvort flugvélin sé nógu stór?

    def get_voyage_destination(self):
        all_destinations = self.__logicapi.list_all_destinations()
        for destinations in all_destinations:
            print (destinations._Destination__destination, "-", destinations._Destination__id,)
        voyage_destination = input("Enter voyage destinations three letter id: ").upper()
        return voyage_destination

    def get_destination_number(self):
        dest_num_list = []
        all_destinations = self.__logicapi.list_all_destinations()
        for destination in all_destinations:
            dest_num_list.append(destination.get_destiantion_number())
        if int(dest_num_list[-1])+1 < 10:
            return str("0" + (str(int(dest_num_list[-1])+1)))
        else:
            return str(int(dest_num_list[-1])+1)

    def change_destination(self):
        self.__clear()
        destination = input("Enter destination: ")
        destination_name = self.__logicapi.find_destination(destination)
        try:
            print("Destination details\n\n" + str(destination_name))
            input("Press enter to continue...")
        except:
            input("Destination not found, Presss enter to return...")
            return
        change_list = ["Back", "Emergency contact name", "Emergency contact phone number"]
        command_str = self.__interface.menu_helper("Change Destination", change_list)
        if command_str == "0":
            return
        if command_str == "1":
            change = "emergencycontact"
            new_info = self.get_destination_emergency_contact()
        elif command_str == "2":
            change = "phonenumber"
            new_info = self.get_destination_emergency_phone()
        if change:
            self.__logicapi.change_destination(destination_name.get_name(), change, new_info)


    def view_voyage(self):
        voyages = self.__logicapi.view_all_voyages()
        for voyage in voyages:
            print (voyage)
        input("Press enter to return...")
   