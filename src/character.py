# # Feature: Create a Character
# As a character I want to have a name so that I can be distinguished from other characters

# can get and set Name
import random
class Characters:
    def __init__(self):
        self.name = "Eric Emery the Destroyer"
        self.alignment = "Neutral"
        self.armor_class = 10
        self.hit_points = 5
        self.attack_power = 5
        self.abilities = {
            'Strength': 10,
            'Dexterity': 10,
            'Constitution': 10,
            'Wisdom': 10,
            'Intelligence': 10,
            'Charisma': 10
        }

    
# take in a string
    def set_name(self, n):
        self.name = n

    def mock_roll(self):
        return self.mock_roll

    def get_alignment(self):
        return self.alignment

    def set_alignment(self, n):
        self.alignment = n

    def take_damage(self, damage):
        if damage > 0:
            self.hit_points -= damage
        if self.hit_points <= 0:
            self.hit_points = 0

    def take_damage(self, damage, roll):
        if damage > 0:
            if roll == 20:
                self.hit_points -= damage * 2  # Double the damage for a critical hit
            else:
                self.hit_points -= damage
        if self.hit_points <= 0:
            self.hit_points = 0

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

    def attack(self, opponent, roll):
        if roll == 20:
            return True  
        return roll >= opponent.get_armor_class()

    def get_ability_score(self, ability):
        if ability in self.abilities:
            return self.abilities[ability]
        else:
            return None

    def set_ability_score(self, ability, score):
        if ability in self.abilities:
            self.abilities[ability] = score

    def get_ability_modifier(self, ability):
        score = self.get_ability_score(ability)
        if score is not None:
            return (score - 10) // 2
        return None