import random



class Ability:
    def __init__(self, name, x):
        self.name = name
        self.max_damage = x

    def attack(self):
        attack_damage = random.randint(0, self.max_damage)
        return attack_damage


if __name__ == '__main__':

    hero_ability = Ability('Hulk', 55)
    print(hero_ability.name)
    # print(hero_ability.max_damage)
    print(hero_ability.attack())
