class Room:

    # Lagrer navn, info og koblet romm
    def __init__(self, name:str, desc:str):
        self.name = name
        self.desc = desc
        self.connect = []

class HealRoom(Room):

    # Lagrer mengde helbrede
    def __init__(self, name:str, desc:str, heal:int):
        super().__init__(name, desc)
        self.heal = heal

class DmgRoom(Room):

    # Lagrer mengde skade
    def __init__(self, name:str, desc:str, dmg:int):
        super().__init__(name, desc)
        self.dmg = dmg

class RandRoom(Room):

    # Lagrer mengde skade og helbrede
    def __init__(self, name:str, desc:str, heal:int, dmg:int):
        super().__init__(name, desc)
        self.heal = heal
        self.dmg = dmg
