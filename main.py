from player import Player
from room import Room, HealRoom, DmgRoom, RandRoom
import random

# Define rooms
room1 = Room( "room 1", "The air is damp and heavy. Faint whispers echo from the walls, but no one is here. A single torch flickers, casting long, wavering shadows. Two ancient wooden doors, barely hanging on their rusted hinges, lead deeper into the unknown. \n1: A crumbling wooden door, darkened with age and splintered around the edges. It creaks loudly as you approach, hinting at the weight of what lies beyond. \n2: A stone archway, worn and jagged, as though it’s been through centuries of turmoil. A cold breeze whispers through the cracks. \n3: A rusted gate, barely holding itself upright. Its iron bars are twisted and cold to the touch, but a mysterious energy hums from within.")
room2 = DmgRoom("room 2", "Blood stains the floor, darkened with age. Chains dangle from the ceiling, swaying slightly as if touched by an unseen hand. The door to the west is sealed with deep claw marks, and the air feels heavy with death. ", 999)
room3 = Room("room 3", "Rows of dusty sarcophagi line the walls. The smell of decayed incense lingers. You feel like you're being watched, but no eyes meet yours. Three exits surround you: a stone archway to the south, a narrow wooden door to the east, and a shadowy hallway to the north. \nSouth: A stone archway, smooth and worn with time. The passage feels eerily cold, as if it leads into the bowels of the earth. \n1: A narrow wooden door, warped and creaking as though it hasn’t been used in centuries. The hinges groan with age. \n2: A shadowy hallway, pitch-black and narrow. As you look down it, you feel a chill race up your spine, and your feet hesitate before entering.")
room4 = DmgRoom("room 4", "The floor is covered in jagged shards of stone. Grooves in the walls suggest something massive and clawed has been here before. A heavy stone door to the north and a dark tunnel to the east seem to lead to equally grim fates. \n1: A heavy stone door, aged and cracked. It looks like it hasn’t been opened in centuries, and yet it gives off a faint hum, urging you to enter. \n2: A dark tunnel, its entrance hidden beneath a veil of shadows. The air smells damp, and the walls are slick with moisture.", 3)
room5 = DmgRoom("room 5", "A gaping chasm stretches across the room, glowing faintly with an eerie red light. The sound of distant screams rises and falls like a mournful tide. A rickety bone bridge to the south leads to safety, while a twisting tunnel to the north beckons ominously. \n1: A twisting tunnel, dark and filled with the sounds of distant clattering. The air is thick with the scent of decay. \n2: A rickety bone bridge stretches across the chasm, creaking ominously with each step. The red glow beneath it pulses in rhythm with your heartbeat.", 4)
room6 = Room("room 6", "An inexplicable calm fills the room. The walls are adorned with ancient runes that emit a soothing blue glow. Despite the serenity, the silence feels unnatural. A narrow archway leads south, a polished wooden door lies to the west, and a weathered iron gate leads northward. \n1: A narrow archway, dark and foreboding. It seems to invite you forward, though the way ahead is hidden in shadows. \n2: A polished wooden door, shining faintly in the dim light. It feels warm to the touch, like it’s waiting to be opened. \n3: A weathered iron gate, sturdy yet old. It rattles faintly in the wind, as though it’s been in place for too long.")
room7 = RandRoom("room 7", "At the center of the room is a fountain filled with dark, swirling liquid. Its glow alternates between warm gold and sickly green, and faint laughter seems to emanate from it. Two pathways lead away: a crumbling tunnel to the south and a darkened stairway to the north, where an ominous glow emanates faintly. \n2: A darkened stairway, the steps worn and slick. The air grows colder the further you climb.", 4, 4)
room8 = Room("room 8", "Pillars carved with scenes of battles long forgotten rise toward the ceiling. The air is dry, and a faint hum suggests a hidden power resides here. A glowing portal hums to the west, and an ominous stairwell descends to the north. \n1: An ominous stairwell, descending into a darkness that seems to stretch forever. The stone steps feel ancient beneath your feet. \n2: A glowing portal, framed by delicate arches. It seems to hum with energy, but the light it gives off is unnaturally cold."  )
room9 = DmgRoom("room 9", "The walls are pitch-black, absorbing all light. The floor feels sticky underfoot, and the sound of dripping water is unnervingly close. A jagged doorway leads west, a shimmering door leads south, and a twisted path stretches to the east. \n1: A jagged doorway, uneven and sharp-edged. It seems to recoil from the light, as though it doesn’t want you to enter. \n2: A shimmering door, beautiful but ominous. The light it emits flickers erratically, like a flame struggling to stay lit. \n3: A twisted path, lined with thorns and shadows. The air grows colder the further you move along it.", 999)
room10 = Room("room 10", "The room is vast and circular, with an ornate altar at its center. Shadows dance along the walls, forming shapes that seem almost alive. A towering golden gate with intricate carvings looms ahead, glowing with an otherworldly light. Behind you, a stairway spirals downward, while hidden paths branch outward into the void. \nFinal Paths: The paths leading to different choices (crawl, jump, pull rope, search) are hidden, each leading to a different outcome.")



# Connect rooms
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

# Game state
current = room1
win = False
more = False

print("--- dungeon crawler ---")
stats = Player("player")



while True:
    if win:
        print("You've made it out alive! Congratulations!")
        break
    if isinstance(current, DmgRoom):
        stats.hp -= current.dmg
    elif isinstance(current, RandRoom):
        print("A mysterious fountain is in the middle of the room. It looks like it can heal you or hurt you. The water is glowing.")
        choice = input("Drink or not (y/n)? ")
        if choice.lower() == "y":
            if random.randint(1, 10) < 7:
                stats.hp += current.heal
                print(f"{current.heal} healed (+4 health)")
            else:
                stats.hp -= current.dmg
                print(f"{current.dmg} damage taken (-4 health)")

    # Display room details
    print(f"\nRoom: {current.name}")
    print(f"Description: {current.desc}")
    print(f"HP: {stats.hp}")

    if stats.hp <= 0:
        print("You meet your unfortunate demise. Your body lays on the floor, lifeless.")
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
                print("Invalid choice. Try again.")
        else:
            print("Invalid input. Please enter a number.")
    elif not more:
        print("1. Jump for it (YOLO)")
        print("2. Swing from rope (seems safe)")
        print("3. Crawl (ooh secrets)")
        print("4. Search room (more options perhaps?)")
        choice = input("Choice: ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1 or choice == 3:
                stats.hp -= 999
            elif choice == 2:
                stats.hp -= 7
                win = True
            elif choice == 4:
                more = True
            else:
                print("Invalid choice. Try again.")
        else:
            print("Invalid input. Please enter a number.")
    else:
        print("1. Push big red hidden button (it's hidden under a loose stone in the wall)")
        print("2. Pull lever (not so hidden but ok)")
        choice = input("Choice: ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                stats.hp -= 999
            elif choice == 2:
                win = True
            else:
                print("Invalid choice. Try again.")
        else:
            print("Invalid input. Please enter a number.")
