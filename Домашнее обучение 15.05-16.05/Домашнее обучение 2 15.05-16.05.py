class Pokemon:
    def __init__(self, name, poke_type, hp, attack):
        self.name = name
        self.poke_type = poke_type
        self.hp = hp
        self.attack = attack

    def show(self):
        print(f"{self.name} ({self.poke_type}) — HP: {self.hp}, Атака: {self.attack}")

class FirePokemon(Pokemon):
    def apply_bonus(self):
        self.attack += 10

class WaterPokemon(Pokemon):
    def apply_bonus(self):
        self.hp += 15

class ElectricPokemon(Pokemon):
    def attack_action(self):
        print(f"⚡ {self.name} выпускает молнию! Сила атаки: {self.attack}")

charmander = FirePokemon("Чармандер", "огонь", 39, 52)
squirtle = WaterPokemon("Сквиртл", "вода", 44, 48)
pikachu = ElectricPokemon("Пикачу", "электричество", 35, 55)

charmander.apply_bonus()
squirtle.apply_bonus()

charmander.show()
squirtle.show()
pikachu.show()

pikachu.attack_action()