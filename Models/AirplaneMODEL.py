class Airplane:
    '''Simple airplane class.
    It has four attributes (name, model, seats and status)
    but it only takes three arguments (besides "self"),
    one of which is defaulted to an empty string (number_of_seats).
    The seats and model attributes can be added via two add functions within the class.'''
    def __init__(self, name, model, number_of_seats = ''):
        self.name = name
        self.model = model
        self.seats = number_of_seats
        self.status = ''

    def __str__(self):
        '''Returns the aircraft information format so it looks super nice and pretty'''
        return "{:<20s}{}\n{:<20s}{}\n{:<20s}{}\n{:<20s}{}\n".format("Name:", self.name, "Model:", self.model, "Number of seats:", self.seats, "Status:", self.status)
    
    def __eq__(self, comparison):
        if self.name == comparison \
        or self.model == comparison:
            return True
        else:
            return False

    def get_airplane_attributes(self):
        '''Returnes the airplane attributes in a list'''
        return [self.name, self.model, self.seats]

    def get_name(self):
        '''Returns the name of the airplane'''
        return self.name

    def get_model(self):
        '''Returns the model of the airplane'''
        return self.model
    
    def add_seats(self, number_of_seats):
        '''Takes a string argument and assigns it to the seat variable'''
        self.seats = number_of_seats
    
    def add_status(self, some_status):
        '''Takes a string argument and assigns it to the status variable'''
        self.status = some_status