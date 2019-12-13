class Airplane:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.status = ''

    def __str__(self):
        '''Returns the aircraft information format so it looks super nice and pretty'''
        return "{:<6s}: {}\n{:<6s}: {}\n{}: {}\n".format("Name", self.name, "Model", self.model, "Status", self.status)
    
    def __eq__(self, comparison):
        if (self.name == comparison) or (self.model == comparison):
            return True
        else:
            return False

    def get_airplane_attributes(self):
        return [self.name, self.model]

    def get_name(self):
        return self.name

    def get_model(self):
        return self.model
    
    def add_status(self, some_status):
        self.status = some_status