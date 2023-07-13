# Feature: Characters Have Classes
# As a player I want a character to 
# have a class that customizes its capabilities 
# so that I can play more interesting characters

# Ideas
# changes in hit points
# changes in attack and damage
# increased critical range or damage
# bonuses/penalties versus other classes
# special abilities
# alignment limitations
# Samples

# As a player I want to play a Fighter so that I can kick ass and take names
# attacks roll is increased by 1 for every level instead of every other level
# has 10 hit points per level instead of 5

# As a player I want to play a Rogue so that I can defeat my enemies with finesse
# does triple damage on critical hits
# ignores an opponents Dexterity modifier (if positive) to Armor Class when attacking
# adds Dexterity modifier to attacks instead of Strength
# cannot have Good alignment

# As a player I want to play a Monk so that I can enjoy being an Asian martial-arts archetype in a Medieval European setting
# has 6 hit point per level instead of 5
# does 3 points of damage instead of 1 when successfully attacking
# adds Wisdom modifier (if positive) to Armor Class in addition to Dexterity
# attack roll is increased by 1 every 2nd and 3rd level

# As a player I want to play a Paladin so that I can smite evil, write wrongs, and be a self-righteous jerk
# has 8 hit points per level instead of 5
# +2 to attack and damage when attacking Evil characters
# does triple damage when critting on an Evil character (i.e. add the +2 bonus for a regular attack, and then triple that)
# attacks roll is increased by 1 for every level instead of every other level
# can only have Good alignment

import pytest
from character import Characters, Fighter, Rogue, Monk, Paladin

# Test Characters class

def test_get_name():                        
    a = Characters()
    assert a.name == "Eric Emery the Destroyer"

def test_set_name():
    b = Characters()
    b.set_name('Billy Bob')
    assert b.name == 'Billy Bob'

def test_get_alignment():
    e = Characters()
    assert e.alignment == "Neutral"

def test_set_alignment():
    d = Characters()
    d.set_alignment('Evil')
    assert d.alignment == 'Evil'

def test_is_alive():
    f = Characters()
    assert f.is_alive() == True

    f.take_damage(5, 0)
    assert f.is_alive() == False


def test_get_armor_class():
    c = Characters()
    assert c.get_armor_class() == 10

def test_set_armor_class():
    g = Characters()
    g.set_armor_class(10)
    assert g.get_armor_class() == 10


def test_get_character_attack():
    h = Characters ()
    assert h.get_character_attack() == 5

def test_set_character_attack():
    i = Characters ()
    i.set_character_attack(5)
    assert i.get_character_attack() == 5


def test_attack():
    j = Characters()
    k = Characters()
    k.set_armor_class(10)
    result = j.attack(k, 15)
    assert result in [True, False]
    

def test_take_damage():
    m = Characters()

    m.take_damage(3, 0)
    assert m.hit_points == 2

    m.take_damage(20, 0)
    assert m.hit_points == 0
    assert m.is_alive() == False


def test_ability_scores():
    character = Characters()

    assert character.get_ability_score('Strength') == 10
    assert character.get_ability_modifier('Strength') == 0

    character.set_ability_score('Strength', 15)
    assert character.get_ability_score('Strength') == 15
    assert character.get_ability_modifier('Strength') == 2

    character.set_ability_score('Intelligence', 25)
    assert character.get_ability_score('Intelligence') == 25
    assert character.get_ability_modifier('Intelligence') == 7

    assert character.get_ability_score('Agility') is None
    assert character.get_ability_modifier('Agility') is None


def test_apply_ability_modifiers():
    character = Characters()

    assert character.attack_power == 5
    assert character.armor_class == 10
    assert character.hit_points == 5

    character.set_ability_score('Strength', 14)
    character.set_ability_score('Dexterity', 12)
    character.set_ability_score('Constitution', 8)
    character.apply_ability_modifiers()

    assert character.attack_power == 7  
    assert character.armor_class == 11  
    assert character.hit_points == 4    


def test_experience_points():
    character = Characters()
    assert character.experience_points == 10


def test_character_level():
    character = Characters()
    assert character.level_experience == 3000
    assert character.mock_roll == 4
    assert character.level == 3



# Test Fighter class

def test_fighter_attack_bonus():
    fighter = Fighter()
    assert fighter.strength_modifier == +1
    assert fighter.hit_points_per_level == 10


# Test Rogue class

def test_rogue_critical_damage_multiplier():
    rogue = Rogue()
    assert rogue.critical_damage_multiplier == 3

def test_rogue_ignore_dexterity_ac():
    rogue = Rogue()
    assert rogue.ignore_dexterity_ac == True

def test_rogue_attack_stat():
    rogue = Rogue()
    assert rogue.attack_stat == "Dexterity"

def test_rogue_allowed_alignments():
    rogue = Rogue()
    assert rogue.allowed_alignments == ["Neutral", "Evil"]


# Test Monk class

def test_monk_hit_points_per_level():
    monk = Monk()
    assert monk.hit_points_per_level == 6

def test_monk_attack_damage():
    monk = Monk()
    assert monk.attack_damage == 3

def test_monk_wisdom_ac_bonus():
    monk = Monk()
    assert monk.wisdom_ac_bonus == True

def test_monk_attack_bonus_per_level():
    monk = Monk()
    assert monk.attack_bonus_per_level == [1, 1, 2]


# Test Paladin class

def test_paladin_hit_points_per_level():
    paladin = Paladin()
    assert paladin.hit_points_per_level == 8

def test_paladin_evil_attack_bonus():
    paladin = Paladin()
    assert paladin.evil_attack_bonus == 2

def test_paladin_evil_critical_damage_multiplier():
    paladin = Paladin()
    assert paladin.evil_critical_damage_multiplier == 3

def test_paladin_attack_bonus():
    paladin = Paladin()
    assert paladin.attack_bonus == 1

def test_paladin_allowed_alignments():
    paladin = Paladin()
    assert paladin.allowed_alignments == ["Good"]
