# # Feature: Create a Character
# As a character I want to have a name so that I can be distinguished from other characters

# can get and set Name

class Characters:
    def __init__(self):
        self.name = "Eric Emery the Destroyer"
        self.alignment = "Neutral"
        self.armor_class = 10
        self.hit_points = 5
        self.attack_power = 5

# take in a string
    def set_name(self, n):
        self.name = n


    def get_alignment(self):
        return self.alignment

    def set_alignment(self, n):
        self.alignment = n

    def take_damage(self, damage):
        if damage > 0:
            self.hit_points -= damage

    def is_alive(self):
        return self.hit_points > 0


    def get_armor_class(self):
        return self.armor_class

    def set_armor_class(self, n):
        self.armor_class = n

    def get_character_attack(self):
        return self.attack_power

    def set_character_attack(self, n):
        self.attack_power = n

    def attack(self, opponent):
        roll = '15'  # Placeholder value for the roll, replace with actual implementation
        if roll == '20':
            return True  
        return roll >= opponent.get_armor_class()