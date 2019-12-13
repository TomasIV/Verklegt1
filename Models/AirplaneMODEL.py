class Airplane:
    def __init__(self, name, model, number_of_seats = ''):
        self.name = name
        self.model = model
        self.seats = number_of_seats
        self.status = ''

    def __str__(self):
        '''Returns the aircraft information format so it looks super nice and pretty'''
        return "{:<20s}{}\n{:<20s}{}\n{:<20s}{}\n{:<20s}{}\n".format("Name:", self.name, "Model:", self.model, "Number of seats:", self.seats, "Status:", self.status)
    
    def __eq__(self, comparison):
        if (self.name == comparison) or (self.model == comparison):
            return True
        else:
            return False

    def get_airplane_attributes(self):
        return [self.name, self.model, self.seats]

    def get_name(self):
        return self.name

    def get_model(self):
        return self.model
    
    def add_seats(self, number_of_seats):
        self.seats = number_of_seats
    
    def add_status(self, some_status):
        self.status = some_status