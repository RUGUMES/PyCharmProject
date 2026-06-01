# Первый этап
class monster:
    def __init__(self, name, hp, dmg):
        self.__name = name
        self.__hp = hp
        self.__dmg = dmg

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def get_dmg(self):
        return self.__dmg

    def set_hp(self, value):
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value

    def is_alive(self):
        return self.__hp > 0

    def show_status(self):
        print(f'{self.__name} HP: {self.get_hp()}.')

    def take_damage(self, damage):
        self.set_hp(self.__hp - damage)
        print(f'{self.__name} получил {damage} урона. HP: {self.get_hp()}.')

    def attack_hunter(self, hunter):
        hunter.set_hp(hunter.get_hp()- self.get_dmg())

# m = monster('Зомби', 100, 10)
# m.show_status()
# m.set_hp(-50)
# m.show_status()
# print(m.is_alive())

# Второй этап
class Zombie(monster):
    def __init__(self, name):
        super().__init__(name, 120, 10)

    def take_damage(self, damage):
        print(f'{self.get_name()} теряет конечность!', end=' ')
        super().take_damage(damage)


class Vampire(monster):
    def __init__(self, name):
        super().__init__(name, 80, 15)

    def take_damage(self, damage):
        absords = 5
        dmg_done = damage - absords
        if dmg_done < 0:
            dmg_done = 0
        print(f'{self.get_name()} поглощает {absords} урона!', end=' ')
        super().take_damage(dmg_done)


class Ghost(monster):
    def __init__(self, name):
        super().__init__(name, 60, 20)

    def take_damage(self, damage):
        import random
        if random.random() < 0.3:
            print(f'{self.get_name()} уклонился от удара!')
        else:
            print(f'{self.get_name()} получил удар!')
        super().take_damage(damage)


class Werewolf(monster):
    def __init__(self, name):
        super().__init__(name, 100, 25)
        self.__transformer = False

    def take_damage(self, damage):

        if not self.__transformer and self.get_hp() < 50:
            self.__transformer = True
        print(f'{self.get_name()} трансформируется в оборотня!')
        super().take_damage(damage)

# v = Vampire('Дракула')
# v.take_damage(30)
# z = Zombie('Зомби')
# z.take_damage(30)

# Третий этап

class Weapon:
    def __init__(self, name):
        self.name = name

    def use(self, monster):
        pass


class SilverSword(Weapon):
    def __init__(self):
        super().__init__('Серебрянный меч')

    def use(self, monster):
        damage = 30
        print(f'Охотник бьёт {monster.get_name()} {self.name}!', end=' ')
        monster.take_damage(damage)


class HolyWater(Weapon):
    def __init__(self):
        super().__init__('Святая вода')

    def use(self, monster):
        damage = 20
        print(f'Охотник бьёт {monster.get_name()} {self.name}!', end=' ')
        monster.take_damage(damage)


class Crossbow(Weapon):
    def __init__(self):
        super().__init__('Арбалет с болтом')

    def use(self, monster):
        damage = 25
        print(f'Охотник бьёт {monster.get_name()} {self.name}!', end=' ')
        monster.take_damage(damage)


# weapons = [SilverSword(), HolyWater(), Crossbow()]
# zombie = Zombie('Зомби')
# for w in weapons:
#     w.use(zombie)


# Четвёртый этап

class Hunter:
    def __init__(self, name):
        self.__name = name
        self.__hp = 100
        self.__weapons = []

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def get_len_weapons(self):
        return len(self.__weapons)

    def set_hp(self, value):
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value

    def is_alive(self):
        return self.__hp > 0

    def add_weapon(self, weapon):
        self.__weapons.append(weapon)

    def show_inventory(self):
        print(f'\nИнвентарь {self.get_name()}')
        for i, w in enumerate(self.__weapons):
            print(f'{i}. {w.name}')

    def attack(self, weapon_index, monster):
        if 0 <= weapon_index < len(self.__weapons):
            self.__weapons[weapon_index].use(monster)





# Пятый этап
def run_game():
    hunter = Hunter('Ван Хельсинк')
    hunter.add_weapon(SilverSword())
    hunter.add_weapon(HolyWater())
    hunter.add_weapon(Crossbow())

    monsters = [
        Zombie('Зомби'),
        Vampire('Дракула'),
        Ghost('Каспер'),
        Werewolf('Оборотень')
    ]

    for monster in monsters:
        print(f'На тебя нападает {monster.get_name()}.')
        print(f'Монстр перед вами имеет {monster.get_hp()} HP и {monster.get_dmg()} Damage.')

        while monster.is_alive() and hunter.is_alive():
            print(f'{hunter.get_name()} имеет {hunter.get_hp()} HP')
            hunter.show_inventory()

            try:
                choice = int(input('Выберите оружие:'))
                if 0 <= choice < hunter.get_len_weapons():

                    hunter.attack(choice, monster)
                else:
                    continue
            except ValueError:
                print('Введите число:')
                continue

            monster.attack_hunter(hunter)

            if not hunter.is_alive():
                print(f'{hunter.get_name()} поражение')
                break

            print('Статус')
            print(f'{hunter.get_name()} HP: {hunter.get_hp()}.')
            print(f'{monster.get_name()} HP: {monster.get_hp()}.')

        if not hunter.is_alive():
            break

    if hunter.is_alive():
        print(f'{hunter.get_name()} зачистил старый замок от врагов')
    else:
        print(f'{hunter.get_name()} был сломлен под натиском врагов')

run_game()