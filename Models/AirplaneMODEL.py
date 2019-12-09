class Airplane:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def __str__(self):
        return ("{:<5s}: {}\n{}: {}\n".format("Name", self.name, "model", self.model))
    
    def __eq__(self, comparison):
        if (self.name == comparison) or (self.model == comparison):
            return True
        else:
            return False
    def get_airplane_attributes(self):
        return [self.name, self.model]
    