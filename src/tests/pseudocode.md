# Pseudocode

## Procedural

1. Define a function named "test_attack" that takes no arguments.
2. Inside the function:
     - Create an attacker character.
     - Create a defender character.
     - Set the defender's armor class to 10.
     - Define the roll value for the test case.
     - Call the "attack" function with the attacker, defender, and roll as arguments and store the result in a variable named "result".
     - Assert that "result" is equal to True.

3. Define a function named "attack" that takes the attacker, defender, and roll as arguments.
4. Inside the "attack" function:
     - Check if the roll is equal to 20.
          - If true, return True (attack is successful).
     - Check if the roll is greater than or equal to the defender's armor class.
          - If true, return True (attack is successful).
     - Otherwise, return False (attack misses).

5. Define a function named "get_armor_class" that takes a character as an argument.
6. Inside the "get_armor_class" function:
     - Return the armor class value of the character.


## Functional

1. Create a class called "Characters".
2. Inside the class:
     - Define the constructor function that initializes the character's attributes such as name, alignment, armor class, and hit points.
     - Implement the "attack" method that takes another character as an argument.
     - Inside the "attack" method:
          - Define the roll value for the attack.
          - Check if the roll is equal to 20.
               - If true, return True (attack is successful).
          - Check if the roll is greater than or equal to the defender's armor class.
               - If true, return True (attack is successful).
          - Otherwise, return False (attack misses).
     - Implement the "get_armor_class" method that returns the armor class value of the character.
3. Define a function named "test_attack" that takes no arguments.
4. Inside the function:
     - Create an attacker character object.
     - Create a defender character object.
     - Set the defender's armor class to 10.
     - Define the roll value for the test case.
     - Call the "attack" method of the attacker object with the defender as an argument and store the result in a variable named "result".
     - Assert that "result" is equal to True.

