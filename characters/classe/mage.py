from classe import Classe

class Mage(Classe):
    def __init__(self, name, HP, defense, mana):
        Classe.__init__(name, HP, defense)
        self.mana = mana