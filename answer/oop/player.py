# Step 1: Player Class
class Body:
    def __init__(self, name, health=100):
        self.name = name
        self._health = health
        self.items = []  # Composition: Characters can possess items

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value >= 0:
            self._health = value
        else:
            self._health = 0

    @property
    def is_alive(self):
        return self.health > 0


class Character(Body):
    def __init__(self, name, health=100, damage=10):
        super().__init__(name, health)
        self.damage = damage

    def attack(self, target):
        if isinstance(target, Body):
            target.health -= self.damage

    # Composition: Characters can possess items
    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)


class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value


player1 = Body("P1")
player2 = Character("P2", health=100, damage=15)

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

    print(f"{player1.name} - Health: {player1.health}, is alive: {player1.is_alive}")
    print(f"{player2.name} - Health: {player2.health}, is alive: {player2.is_alive}")

# Composition: Adding items to characters
sword = Item("Sword", "A sharp weapon", 50)
shield = Item("Shield", "Protective gear", 30)

player2.add_item(sword)
player2.add_item(shield)

print(f"{player2.name} has the following items:")
for item in player2.items:
    print(f"{item.name}: {item.description}, Value: {item.value}")

print("GAME OVER")
