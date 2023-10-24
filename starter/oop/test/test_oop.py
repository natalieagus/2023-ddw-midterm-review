import pytest

# Import the classes from your exercise code
from player import Body, Character, Item


def test_body_initialization():
    body = Body("TestBody", health=90)
    assert body.name == "TestBody"
    assert body.health == 90


def test_body_health_setter():
    body = Body("TestBody")
    body.health = 80
    assert body.health == 80


def test_body_health_setter_negative_value():
    body = Body("TestBody")
    body.health = -10
    assert body.health == 0


def test_body_is_alive():
    body = Body("TestBody", health=50)
    assert body.is_alive == True


def test_character_attack():
    player1 = Character("Player1")
    player2 = Character("Player2")
    player1.attack(player2)
    assert player2.health == 90  # Assuming default damage is 10


def test_character_add_item():
    player1 = Character("Player1")
    sword = Item("Sword", "A sharp weapon", 50)
    player1.add_item(sword)
    assert sword in player1.items


def test_character_remove_item():
    player1 = Character("Player1")
    sword = Item("Sword", "A sharp weapon", 50)
    player1.add_item(sword)
    player1.remove_item(sword)
    assert sword not in player1.items


def test_turn_based_gameplay():
    player1 = Character("Player1", health=100, damage=10)
    player2 = Character("Player2", health=100, damage=15)
    while player1.health > 0 and player2.is_alive:
        player1.attack(player2)
        player2.attack(player1)
    assert player1.is_alive == False and player2.is_alive == True
