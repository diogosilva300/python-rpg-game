from random import randint

class Character:
    def __init__(self, data):
        self._name = data.get("name")
        self._hp = data.get("hp")
        self._mp = data.get("mp")
        self._level = data.get("level")
        self._exp = data.get("exp")
        self._maxExp = data.get("maxExp")
        self._atack = data.get("atack")
        self._defense = data.get("defense")
        self._speed = data.get("speed")

    def getStatus(self):
        return {
            "name" : self._name,
            "hp" : self._hp,
            "mp" : self._mp,
            "level" : self._level,
            "exp" : self._exp,
            "maxExp" : self._maxExp,
            "atack" : self._atack,
            "defense" : self._defense,
            "speed" : self._speed
        }

    @classmethod
    def set_level_base_status(classe) -> int:
        min_level = 1
        level_gap = 2

        if classe.main_character:
            return classe.clamp(
                min_level,
                randint(classe.main_character.getStatus().get("level") - level_gap, classe.main_character.getStatus().get("level") + level_gap),
                classe.main_character.getStatus().get("level") + level_gap
            )
        else:
            return 1

    @classmethod
    def create_base_status(classe):
        level = 1
        name = input("Write your character name: ")
        ###
        # Status Inerentes -> Health Points, Mana, Level, Experience, Max Experience.
        # Status Combate   -> Atack, Defense, Speed. -> Opcionais:  Accuracy, Evasion, Critical Rate.
        ###
        character = {
            "name" : name,
            "hp" : 10 * level,
            "mp" : 5 * level,
            "level" : level,
            "exp" : 0,
            "maxExp" : 25 * level,
            "atack" : 5 + 2 * level,
            "defense" : 3 + 1.5 * level,
            "speed" : 5 + 1.2 * level
        }
        return character