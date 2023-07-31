class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member=False, gold_card_points= 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
    
    def display_info(self):
        print('first name: ' + self.first_name)
        print('last name: ' + self.last_name)
        print('email: ' + self.email)
        print('age: ' + str(self.age))
        print('rewards member: ' + str(self.is_rewards_member))
        print('gold card points: ' + str(self.gold_card_points))
        return self

    def enroll(self):
        if self.is_rewards_member:
            print('User already a member')
            return False
        self.is_rewards_member = True
        self.gold_card_points = 200
        return True
    
    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print('ERROR: Gold card points spending cannot exceed current points.')
            print('Current gold card points: ' + str(self.gold_card_points))
            return self
        self.gold_card_points -= amount
        return self

#TESTING SECTION

user_homer = User('Homer', 'Simpson', 'dufflover99@gmail.com', 40)
user_homer.display_info()
user_homer.enroll()
user_homer.display_info()
user_john = User('John', 'Doe', 'jdoe832@gmail.com', 55)
user_jane = User('Jane', 'Doe', 'janedoetho@gmail.com', 22)
user_homer.spend_points(50)
user_john.enroll()
user_john.spend_points(80)
user_john.display_info()
user_jane.display_info()
user_homer.display_info()
user_homer.enroll()
user_jane.spend_points(40)
