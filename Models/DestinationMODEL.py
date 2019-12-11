class Destination:
    def __init__(self, id, destination, destination_number, emergency_contact, emergency_phone, flight_time, kilometers):
        self.id = id #we could not have id so I changed it to ids
        self.destination = destination
        self.number = destination_number
        self.emergency_contact = emergency_contact
        self.emergency_phone = emergency_phone
        self.flight_time = flight_time
        self.kilometers = kilometers
    
    def __str__(self):
        '''Returns the destinastion information format so it looks super nice and pretty'''
        #line = "ID and Destination: Emergency Name and Mobile:\n{:<20s}{}\n{:<20s}{}\n".format(self.id, self.emergency_contact, self.destination,  self.emergency_phone)
        attribute = ["Destination", "Destination ID", "Destination Number", "Emergency Contact", "Emergency phone number", "Flight time", "Kilometers"] #Longest string is 23 so spacing is 23
        return ("{:<23s}: {}\n{:<23s}: {}\n{:<23s}: {}\n{:<23s}: {}\n{:<23s}: {}\n{:<23s}: {}\n{:<23s}: {}\n".format(attribute[0], self.destination, attribute[1], self.id, attribute[2], self.number, attribute[3], self.emergency_contact, attribute[4], self.emergency_phone, attribute[5], self.flight_time, attribute[6], self.kilometers))

    # def add_destination(self):
    #     print ("Please enter the details of the new destination")
    #     destination_id = input("Id: ")
    #     name_of_destination  = input("Name of destination: ")
    #     em_contact = input("Name of emergency contact: ")
    #     # em_phone = input("Emergency phone number: ")
    