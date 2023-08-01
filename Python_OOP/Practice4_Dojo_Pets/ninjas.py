from dojo_pets import Pet

# class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
    
    
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet_name, pet_type, pet_tricks):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet(pet_name, pet_type, pet_tricks)

    def walk(self):
        self.pet.play()
        return self
    
    def feed(self):
        self.pet.eat()
        self.pet_food -= 10
        return self
    
    def bathe(self):
        self.pet.noise()
        return self
    

user = Ninja('John', 'Doe', 10, 50, 'Mr. Jinx', 'cat', 'uses toilet')

user.feed()
user.walk()
user.bathe()
