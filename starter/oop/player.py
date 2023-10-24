# Step 1: Body Class
# Define a class called "Body" to represent a character or entity.

class Body:
    # Step 2
    # Initialize the Body object with a name and optional health value.
    # Step 3
    # Define a property "health" to get and set the health value.
    # Ensure that the health value is never less than 0.
    # Step 4
    # Define a property "is_alive" to check if the character is alive.
    pass

# Step 5
# Define a Character class that inherits from the Body class.


class Character:
    # Initialize the Character with a name, health, and damage.
    # Define a method to perform an attack on a target (which can be a Body object).
    # Define a method to add an item to the character's possessions.
    # Define a method to remove an item from the character's possessions.
    pass

# Step 6
# Define a class called "Item" to represent items that can be possessed by characters.


class Item:
    # Initialize the Item with a name, description, and value.
    pass


# Step 7: Instantiate Players and Characters
player1 = Body("P1")
player2 = Character("P2", health=100, damage=15)

# Step 8: Turn-Based Gameplay
while player1.health > 0 and player2.is_alive:
    # Check if the target is an instance of Character before attacking
    if isinstance(player2, Character):
        player2.attack(player1)
    else:
        player2.health -= 10  # fix attack rate

    if isinstance(player1, Character):
        player1.attack(player2)
    else:
        player1.health -= 10  # fix attack rate

    # Step 9: Display Information
    print(f"{player1.name} - Health: {player1.health}, is alive: {player1.is_alive}")
    print(f"{player2.name} - Health: {player2.health}, is alive: {player2.is_alive}")

# Step 10
# Composition: Adding items to characters
sword = None
shield = None

player2.add_item(sword)
player2.add_item(shield)

print(f"{player2.name} has the following items:")
for item in player2.items:
    print(f"{item.name}: {item.description}, Value: {item.value}")

print("GAME OVER")
