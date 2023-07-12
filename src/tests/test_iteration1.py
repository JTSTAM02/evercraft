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

# def test_get_armor():
#     f = Characters('10')
#     assert f.armor == '10'

# def test_set_armor():
#     g = Characters('10')
#     assert g.armor == '10'

# def test_get_hit_points():
#     i = Characters('5')
#     assert i.hitpoints == '5'


# def test_set_hit_points():
#     j = Characters('5')
#     assert j.hitpoints == '5'