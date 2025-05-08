class Mage:
    def __init__(self, name, spells):
        self.name = name
        self.spells = spells


class Warrior:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense


class Elf:
    def __init__(self, name, aura):
        self.name = name
        self.aura = aura


class DarkLord(Warrior, Elf):
    def __init__(self, name, defense, aura, dark_spells):
        Warrior.__init__(self, name, defense)
        Elf.__init__(self, name, aura)
        self.dark_spells = dark_spells


char_darklord = DarkLord("MrMalo", "Defensa de Hierro", "Aura Oscura", "Bola de fuego")

print(char_darklord.name)
print(char_darklord.defense)
print(char_darklord.aura)
print(char_darklord.dark_spells)
