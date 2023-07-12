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

def test_take_damage():
    c = Characters()
    c.take_damage(3)
    assert c.hit_points == 2

def test_is_alive():
    f = Characters()
    assert f.is_alive() == True

    f.take_damage(5)
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

    