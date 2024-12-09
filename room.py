class Room:

    """
    Class for Room

    Parameters:
    name (str): name
    desc (str): description for room
    """

    # Lagrer navn, info og koblet romm
    def __init__(self, name:str, desc:str):
        self.name = name
        self.desc = desc
        self.connect = []

class HealRoom(Room):

    """
    Class for HealRoom

    Parameters:
    Inherited from Room
    heal (int): heal amount
    """

    # Lagrer mengde helbrede
    def __init__(self, name:str, desc:str, heal:int):
        super().__init__(name, desc)
        self.heal = heal

class DmgRoom(Room):

    """
    Class for DmgRoom

    Parameters:
    Inherited from Room
    dmg (int): damage amount
    """


    # Lagrer mengde skade
    def __init__(self, name:str, desc:str, dmg:int):
        super().__init__(name, desc)
        self.dmg = dmg

class RandRoom(Room):

    """
    Class for RandRoom

    Parameters:
    Inherited from Room
    heal (int): heal amount
    dmg (int): damage amount
    """

    # Lagrer mengde skade og helbrede
    def __init__(self, name:str, desc:str, heal:int, dmg:int):
        super().__init__(name, desc)
        self.heal = heal
        self.dmg = dmg
