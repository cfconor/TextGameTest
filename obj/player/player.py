class Player:
    
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

    def description(self):
        return "{} is {} years old".format(self.name, self.age)