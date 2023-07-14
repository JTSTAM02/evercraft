# Pseudocode

## Procedural

1. Define a function named "test_attack" that takes no arguments.
2. Inside the function:
   3. Create an attacker character.
   4. Create a defender character.
   5. Set the defender's armor class to 10.
   6. Define the roll value for the test case.
   7. Call the "attack" function with the attacker, defender, and roll as arguments and store the result in a variable named "result".
   8. Assert that "result" is equal to True.
9. Define a function named "attack" that takes the attacker, defender, and roll as arguments.
10. Inside the "attack" function:
11. Check if the roll is equal to 20.
12. If true, return True (attack is successful).
13. Check if the roll is greater than or equal to the defender's armor class.
14. If true, return True (attack is successful).
15. Otherwise, return False (attack misses).

16. Define a function named "get_armor_class" that takes a character as an argument.
17. Inside the "get_armor_class" function:
18. Return the armor class value of the character.

## Functional (tests)
-# Import necessary modules
import pytest
from character import Characters

# Test: Get name
def test_get_name():
    character = Characters()
    assert character.get_name() == "Eric Emery the Destroyer"

# Test: Set name
def test_set_name():
    character = Characters()
    character.set_name('Billy Bob')
    assert character.get_name() == 'Billy Bob'


## Object-Oriented (code)

- Import necessary modules
import pytest
from character import Characters

- Create a test class for Characters
class TestCharacters:
    # Test: Get name
    def test_get_name(self):
        character = Characters()
        assert character.get_name() == "Eric Emery the Destroyer"

    # Test: Set name
    def test_set_name(self):
        character = Characters()
        character.set_name('Billy Bob')
        assert character.get_name() == 'Billy Bob'
