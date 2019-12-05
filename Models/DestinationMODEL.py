class Destination:
    def __init__(self, ids, destination, emergency_contact, emergency_phone):
        self.ids = ids #we could not have id so I changed it to ids
        self.destination = destination 
        self.emergency_contact = emergency_contact
        self.emergency_phone = emergency_phone 
    
    def __str__(self):
        '''Returns the destinastion information format so it looks super nice and pretty'''
        line = "ID and Destination: Emergency Name and Mobile:\n{:<20s}{}\n{:<20s}{}\n".format(self.ids, self.emergency_contact, self.destination,  self.emergency_phone)
        return line

    def add_destination(self):
        print ("Please enter the details of the new destination")
        destination_id = input("Id: ")
        name_of_destination  = input("Name of destination: ")
        em_contact = input("Name of emergency contact: ")
        em_phone = input("Emergency phone number: ")
    


#some_destination = Destination("LYR","Longyearbyean","William Defoe","8897393")
#print(some_destination)