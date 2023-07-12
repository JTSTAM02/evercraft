# # Feature: Create a Character
# As a character I want to have a name so that I can be distinguished from other characters

# can get and set Name

class Characters:
    def __init__(self):
        self.name = "Eric Emery the Destroyer"
        self.alignment = "Neutral"
        self.armor = '10'
        self.hitpoints = '5'

# take in a string
    def set_name(self, n):
        self.name = n


    def get_alignment(self):
        return self.alignment

    def set_alignment(self, n):
        self.alignment = n

    # def get_armor(self):
    #     return self.armor

    # def set_armor(self, n):
    #     self.armor = n

    # def get_hit_points(self, n):
    #     self.hitpoints = n

    # def set_hit_points(self, n):
    #     self.hitpoints = n
