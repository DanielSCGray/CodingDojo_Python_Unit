

# class Pet:
# implement __init__( name , type , tricks ):
# implement the following methods:
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound

class Pet:
    def __init__(self, name, type, tricks, health=25, energy=50):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    
    def play(self):
        self.health += 5
        return self
    
    def noise(self):
        if self.type == 'cat':
            print('Meow')
        elif self.type == 'dog':
            print('Bark')
        else:
            print('I am a 600 year old wizard trapped in animal form')
        return self
