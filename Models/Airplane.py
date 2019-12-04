class Airplane:
    def __init__(self, name, model, manufacturer, capacity):
        self.__name = name
        self.model = model
        self.manufacturer = manufacturer
        self.capacity = capacity
    

    def add_airplane(self):
        print("Please enter the deatails of the new airplane")
        name = input("PlaneID: ")
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
        if manufacturer == "BAE":
            model = input("Model \n1. Model 148\n2. Other Model \nSelect Model: ")
            model_options = ["1", "2"]
            while model not in model_options:
                print("Invalid input! Please try again")
                model = input("Model \n1. Model 148\n2. Other Model \nSelect Model: ")
            if model == "1":
                model = "148"
            elif model == "2":
                model = input("Input other Model: ")
        elif manufacturer == "Fokker":
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
        elif manufacturer != "Fokker" or manufacturer != "BAE":
            model = input("Input model number: ")
        capacity = input("Capacity: ")
        return Airplane(name, model, manufacturer, capacity)
        

pink_airplane = Airplane('some name', 'some model', 'some bitch', 'a lot')
updated_airplane = pink_airplane.add_airplane()
print(pink_airplane.capacity)
print(updated_airplane.model)