import random



class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        attack_damage = random.randint(0, self.max_damage)
        return attack_damage

class Weapon(Ability):
    def attack(self):
        return random.randint(self.max_damage // 2, self.max_damage)

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        block_strength = random.randint(0, self.max_block)
        return block_strength

class Hero:
    def __init__(self, name, start_health = 100):
        self.name = name
        self.start_health = start_health
        self.current_health = start_health
        self.abilities = []
        self.armors = []


    def add_ability(self, ability):
        return self.abilities.append(ability)

    def attack(self):
        total = 0
        for ability in self.abilities:
            total += ability.attack()
        return total

    def add_armor(self, armor):
        return self.armors.append(armor)

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        after_damage = damage - self.defend()
        self.current_health -= after_damage
        return self.current_health

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
        # print('!!!!')
        # print(self.name)
        # print(opponent.name)
        match = True
        while match:
            if len(self.abilities) == 0 and len(opponent.abilities) == 0:
                print('Draw!')
            else:
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())

            if self.is_alive() == False:
                match = False
                print(f'{opponent.name} won!')
            elif opponent.is_alive() == False:
                match = False
                print(f'{self.name} won!')

class Team:
    def __init__(self, name):
        self.name = name
        self.hero = list()

    def remove_hero(self, name):
        if self.name in self.hero:
            self.hero.pop(self.name)
        else:
            return 0

    def view_all_heroes(self):
        for name in self.hero:
            return name

    def add_hero(self, hero):
        return self.hero.append(hero)










if __name__ == '__main__':

    # hero_ability = Hero('Hulk', 100, 100)
    # print(hero_ability.name)
    # print(hero_ability.max_damage)
    # print(hero_ability.attack())
    # print(hero_ability.block())
    # print(hero_ability.present_health())

    # ability = Ability("Great Debugging", 50)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # print(hero.abilities)

    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Smarty Pants", 90)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # hero.add_ability(another_ability)
    # print(hero.attack())

    #test code for take_damage method
    # hero = Hero("Grace Hopper", 200)
    # shield = Armor("Shield", 50)
    # hero.add_armor(shield)
    # hero.take_damage(50)
    # print(hero.current_health)

    # hero = Hero("Grace Hopper", 200)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.is_alive())

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
