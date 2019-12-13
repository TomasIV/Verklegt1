class Destination:
    '''Simple destination class.
    It has seven attributes (besides "self").'''
    def __init__(self, destination_id, destination, destination_number, emergency_contact, emergency_phone, flight_time, kilometers):
        self.__id = destination_id
        self.__destination = destination
        self.__number = destination_number
        self.emergency_contact = emergency_contact
        self.emergency_phone = emergency_phone
        self.__flight_time = flight_time
        self.__kilometers = kilometers
        
    def __str__(self):
        '''Returns the destinastion information format so it looks nice and clean'''
        attribute = ["Destination", "Destination ID", "Destination Number", "Emergency Contact", "Emergency phone number", "Flight time", "Kilometers"] #Longest string is 23 so spacing is 23
        return ("{:<23s}: {}\n{:<23s}: {}\n{:<23s}: {}\n{:<23s}: {}\n{:<23s}: {}\n{:<23s}: {}\n{:<23s}: {}\n".format(attribute[0], self.__destination, attribute[1], self.__id, attribute[2], self.__number, attribute[3], self.emergency_contact, attribute[4], self.emergency_phone, attribute[5], self.__flight_time, attribute[6], self.__kilometers))
    
    def __eq__(self, comparison):
        if self.__id == comparison \
        or self.__destination == comparison \
        or self.__number == comparison \
        or self.emergency_contact == comparison \
        or self.emergency_phone == comparison \
        or self.__flight_time == comparison \
        or self.__kilometers == comparison:
            return True
        else:
            return False

    def get_destination_attributes(self):
        '''Returnes the destination attributes in a list'''
        return [self.__id, self.__destination, self.__number, self.emergency_contact, self.emergency_phone, self.__flight_time, self.__kilometers]

    def get_destiantion_number(self):
        '''Returns the destination number'''
        return self.__number
    
    def get_fligh_time(self):
        '''Returns the flight time to the destiantion'''
        return self.__flight_time
    
    def get_name(self):
        '''Returns the name of the destination'''
        return self.__destination