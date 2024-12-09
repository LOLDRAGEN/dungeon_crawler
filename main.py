from player import Player
from room import Room, HealRoom, DmgRoom, RandRoom
import random

room1 = Room("room 1","room1 - spawn")
room2 = DmgRoom("room 2","room2 - dead",999)
room3 = Room("room 3","room3 - spawn")
room4 = DmgRoom("room 4","room4 - dmg",3)
room5 = DmgRoom("room 5","room5 - dmg",4)
room6 = Room("room 6","room6 - safe")
room7 = RandRoom("room 7","room7 - random",4,4)
room8 = Room("room 8","room8 - safe")
room9 = DmgRoom("room 9","room9 - dead",999)
room10 = Room("room 10","room10 - multiple")

current = room1
win = False
more = False

room1.connect.append(room2)
room1.connect.append(room3)
room1.connect.append(room4)
room3.connect.append(room2)
room3.connect.append(room5)
room3.connect.append(room6)
room4.connect.append(room6)
room4.connect.append(room7)
room5.connect.append(room8)
room5.connect.append(room9)
room6.connect.append(room7)
room6.connect.append(room9)
room7.connect.append(room10)
room8.connect.append(room1)

print("--- dungeon crawler ---")
stats = Player("Tester")

while True:
    
    if type(current) == DmgRoom:
        stats.hp -= current.dmg
    elif type(current) == RandRoom:
        print("sus mystery fountain appears")
        choice = input("drink or not (y/n) ")
        if choice.lower() == "y":
            if random.randint(1,10) < 7:
                stats.hp += current.heal
                print(f"{current.heal} healed (more alive wow)")
            else:
                stats.hp -= current.dmg
                print(f"{current.dmg} damage taken (uh oh)")

    print(f"Room: {current.name}")
    print(f"HP: {stats.hp}")

    if stats.hp <= 0:
        print("dead lmao (skill issue funny moment)")
        break 

    if win == True:
        print("win (no reward btw)")
        break

    if current.name != "room 10":
        for i in current.connect:
            print(f"{current.connect.index(i)+1}. {i.name}")

        choice = input("Choice: ")
        if choice.isdigit():
            choice = int(choice) - 1
            if 0 <= choice < len(current.connect):
                current = current.connect[choice]
            else:
                print("invalid (wtf bruh)")
        else:
            print("invalid (y no number)")
    elif more == False:
        print("1. jump for it (trust)")
        print("2. pull rope (hmmm)")
        print("3. crawl (ooh secrets)")
        print("4. search room (ah yes very interesting)")
        choice = input("Choice: ")
        if choice.isdigit():
            choice = int(choice)
            print(choice)
            if choice == 1 or choice == 3:
                print(choice)
                stats.hp -= 999
                print(stats.hp)
            elif choice == 2:
                stats.hp -= 7
                win = True
            elif choice == 4:
                more = True
            else:
                print("invalid (wtf bruh)")
        else:
            print("invalid (y no number)")
    else:
        print("1. push big red hidden button (looks cool tho damn)")
        print("2. pull lever (not so hidden but ok)")
        choice = input("Choice: ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                stats.hp -= 999
            elif choice == 2:
                win = True
            else:
                print("invalid (wtf bruh)")
        else:
            print("invalid (y no number)")
