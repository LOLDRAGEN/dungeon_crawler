import pytest
from player import Player
from room import Room, HealRoom, DmgRoom, RandRoom

def test_player_initialization():
    player = Player("TestPlayer")
    assert player.name == "TestPlayer"
    assert player.hp == 10

def test_room_initialization():
    room = Room("TestRoom", "A test room description.")
    assert room.name == "TestRoom"
    assert room.desc == "A test room description."
    assert room.connect == []

def test_heal_room_initialization():
    heal_room = HealRoom("HealRoom", "A room that heals.", 5)
    assert heal_room.name == "HealRoom"
    assert heal_room.desc == "A room that heals."
    assert heal_room.heal == 5

def test_dmg_room_initialization():
    dmg_room = DmgRoom("DmgRoom", "A room that deals damage.", 5)
    assert dmg_room.name == "DmgRoom"
    assert dmg_room.desc == "A room that deals damage."
    assert dmg_room.dmg == 5

def test_rand_room_initialization():
    rand_room = RandRoom("RandRoom", "A random room.", 5, 5)
    assert rand_room.name == "RandRoom"
    assert rand_room.desc == "A random room."
    assert rand_room.heal == 5
    assert rand_room.dmg == 5