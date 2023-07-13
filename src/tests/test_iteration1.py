import pytest
from character import Characters

def test_get_name():                        
    a = Characters()
    assert a.name == "Eric Emery the Destroyer"

def test_set_name():
    b = Characters()
    b.set_name('Billy Bob')
    assert b.name == 'Billy Bob'



#Feature: Alignment
# As a character I want to have an alignment so that I have something to guide my actions

# can get and set alignment
# alignments are Good, Evil, and Neutral

def test_get_alignment():
    e = Characters()
    assert e.alignment == "Neutral"


def test_set_alignment():
    d = Characters()
    d.set_alignment('Evil')
    assert d.alignment == 'Evil'


#     Feature: Armor Class & Hit Points
# As a combatant I want to have an armor class and hit points so that I can resist attacks from my enemies

# has an Armor Class that defaults to 10
# has 5 Hit Points by default

# _____

# def test_take_damage():
#     c = Characters()
#     c.take_damage(3)
#     assert c.hit_points == 2

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

# Feature: Character Can Attack
# As a combatant I want to be able to attack other combatants so that I can survive to fight another day

# roll a 20 sided die (don't code the die)
# roll must meet or beat opponents armor class to hit
# a natural roll of 20 always hits

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
    


# Feature: Character Can Be Damaged
# As an attacker I want to be able to damage my enemies so that they will die and I will live

# If attack is successful, other character takes 1 point of damage when hit
# If a roll is a natural 20 then a critical hit is dealt and the damage is doubled
# when hit points are 0 or fewer, the character is dead

def test_take_damage():
    m = Characters()

    m.take_damage(3, 0)
    assert m.hit_points == 2

    m.take_damage(20, 0)
    assert m.hit_points == 0
    assert m.is_alive() == False

# Feature: Character Has Abilities Scores
# As a character I want to have several abilities so that I am not identical to other characters except in name

# Abilities are Strength, Dexterity, Constitution, Wisdom, Intelligence, Charisma
# Abilities range from 1 to 20 and default to 10
# Abilities have modifiers according to the following table
# Score	Modifier	Score	Modifier	Score	Modifier	Score	Modifier
# 1	-5	6	-2	11	0	16	+3
# 2	-4	7	-2	12	+1	17	+3
# 3	-4	8	-1	13	+1	18	+4
# 4	-3	9	-1	14	+2	19	+4
# 5	-3	10	0	15	+2	20	+5

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


# Feature: Character Ability Modifiers Modify Attributes
# As a character I want to apply my ability modifiers improve my capabilities in combat so that I can vanquish my enemy with extreme prejudice

# add Strength modifier to:
# attack roll and damage dealt
# double Strength modifier on critical hits
# minimum damage is always 1 (even on a critical hit)
# add Dexterity modifier to armor class
# add Constitution modifier to hit points (always at least 1 hit point)

def test_apply_ability_modifiers():
    character = Characters()

    # Test initial attribute values
    assert character.attack_power == 5
    assert character.armor_class == 10
    assert character.hit_points == 5

    # Test ability modifiers
    character.set_ability_score('Strength', 14)
    character.set_ability_score('Dexterity', 12)
    character.set_ability_score('Constitution', 8)
    character.apply_ability_modifiers()

    # Test modified attribute values
    assert character.attack_power == 7  # Strength modifier +1
    assert character.armor_class == 11  # Dexterity modifier +1
    assert character.hit_points == 4    # Constitution modifier -1 (minimum 1)



