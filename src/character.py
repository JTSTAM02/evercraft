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
        self.experience_points = 10
        self.level_experience = 3000
        self.level = 3
        self.mock_roll = 4
        self.abilities = {
            'Strength': 10,
            'Dexterity': 10,
            'Constitution': 10,
            'Wisdom': 10,
            'Intelligence': 10,
            'Charisma': 10
        }

#-----SET NAME AND FAKE FUNCTION FOR ROLL------------------------

    def set_name(self, n):
        self.name = n

    def mock_roll(self):
        return self.mock_roll

#------ALIGNMENT-------------------------------------------------

    def get_alignment(self):
        return self.alignment

    def set_alignment(self, n):
        self.alignment = n

#------ARMOR CLASS AND HITPOINTS---------------------------------
#------ALSO CHARACTER CAN BE DAMAGED-----------------------------

    def take_damage(self, damage):
        if damage > 0:
            self.hit_points -= damage
        if self.hit_points <= 0:
            self.hit_points = 0

    def take_damage(self, damage, roll):
        if damage > 0:
            if roll == 20:
                self.hit_points -= damage * 2  
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

#------CHARACTER CAN ATTACK-------------------------------------
#------ALSO GAIN EXPERIENCE WHEN ATTACKING----------------------

    def get_character_attack(self):
        return self.attack_power

    def set_character_attack(self, n):
        self.attack_power = n

    def attack(self, opponent, roll): 
        if roll == 20:
            return True
        return roll >= opponent.get_armor_class()

    def successful_attack_experience():
        if self.attack == True:
            return self.experience_points + 10

    def unsuccessful_attack_experience():
        if self.attack == True:
            return self.experience_points

#-----ABILITY SCORES---------------------------------------------

    def get_ability_score(self, abilities):
        if abilities in self.abilities:
            return self.abilities[abilities]
        else:
            return None

    def set_ability_score(self, abilities, score):
        if abilities in self.abilities:
            self.abilities[abilities] = score

#-----ABILITY MODIFIERS------------------------------------------

    def get_ability_modifier(self, abilities):
        score = self.get_ability_score(abilities)
        if score is not None:
            return (score - 10) // 2
        return None

    def apply_ability_modifiers(self):
        strength_modifier = self.get_ability_modifier('Strength')
        dexterity_modifier = self.get_ability_modifier('Dexterity')
        constitution_modifier = self.get_ability_modifier('Constitution')

        self.attack_power += strength_modifier
        if self.attack_power < 1:
            self.attack_power = 1

        self.armor_class += dexterity_modifier

        self.hit_points += constitution_modifier
        if self.hit_points < 1:
            self.hit_points = 1

        if self.level + 1:
            return constitution_modifier + 1

#------CHARACTER LEVEL/LEVELING-------------------------------------

    def character_level(self):
        if(self.level_experience + 1000):
            return self.level_experience + self.experience_points
    
    def level_up(self):
        if (self.experience_points +1000):
            return (self.level + 1) + (self.hit_points + 5)

    def current_level(self):
        if (self.level % 2):
            return self.mock_roll + 1

#------ITERATION 2------------------------------------------------


class Fighter:
    def __init__(self):
        self.strength_modifier = +1
        self.hit_points_per_level = 10

class Rogue:
    def __init__(self):
        self.critical_damage_multiplier = 3
        self.ignore_dexterity_ac = True
        self.attack_stat = "Dexterity"
        self.allowed_alignments = ["Neutral", "Evil"]

class Monk:
    def __init__(self):
        self.hit_points_per_level = 6
        self.attack_damage = 3
        self.wisdom_ac_bonus = True
        self.attack_bonus_per_level = [1, 1, 2]

class Paladin:
    def __init__(self):
        self.hit_points_per_level = 8
        self.evil_attack_bonus = 2
        self.evil_critical_damage_multiplier = 3
        self.attack_bonus = 1
        self.allowed_alignments = ["Good"]