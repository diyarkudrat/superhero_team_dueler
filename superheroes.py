from random import choice, randint



class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        attack_damage = randint(0, self.max_damage)
        return attack_damage

class Weapon(Ability):
    def attack(self):
        return randint(self.max_damage // 2, self.max_damage)

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        block_strength = randint(0, self.max_block)
        return block_strength

class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.ratio = 0
        self.deaths = 0
        self.kills = 0
        self.abilities = []
        self.armors = []
        self.deaths = 0
        self.kills = 0


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
        if int(self.current_health <= 0):
            return False
        else:
            return True

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

    def add_weapon(self, weapon):
        return self.abilities.append(weapon)

    def add_armor(self, armor):
        # armor = Armor()
        self.armors.append(armor)

    def display_stats(self):
        if self.deaths > 0:
            ratio = self.kills/self.deaths
        else:
            ratio = self.kills

        print(f'Kill/Death Ratio: {ratio}')
        # return '!!!!'

    def fight(self, opponent):

        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())

        # print('Fight Over')

        if not opponent.is_alive():

            self.add_kill(1)
            opponent.add_deaths(1)

            print(f'{self.name} won!')

        elif not self.is_alive():

            opponent.add_kill(1)
            self.add_deaths(1)

            print(f'{opponent.name} won!')

        else:
            print('Draw!')

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()
        self.ratio = 0

    def remove_hero(self, name):
        index = 0
        l = len(self.heroes)

        for hero in self.heroes:
            if hero.name == name:
                del self.heroes[index]

            else:
                index += 1
        if len(self.heroes) == l:
            return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        return self.heroes.append(hero)


    def revive_heroes(self, health = 100):
        for hero in self.heroes:
            health = hero.current_health
        # team1.attack(team2)


    def members_alive(self):
        heroes_alive = []

        for hero in self.heroes:
            if hero.is_alive() == True:
                heroes_alive.append(hero)

        return heroes_alive

    def number_of_team_members_alive(self):

        number_heroes_alive = 0

        for hero in self.heroes:

            if hero.is_alive() == True:
                number_heroes_alive += 1

        return number_heroes_alive

    def attack(self, other_team):

        while self.number_of_team_members_alive() > 0 and other_team.number_of_team_members_alive() > 0:

            hero1 = choice(self.members_alive())
            hero2 = choice(other_team.members_alive())

            hero1.fight(hero2)



    def stats(self):

        ratio = 0
        total_deaths = 0
        total_kills = 0

        for hero in self.heroes:
            total_kills += hero.kills
            total_deaths += hero.deaths

        if total_deaths == 0:
            ratio = total_kills

        else:
            ratio = total_kills/total_deaths

        return ratio



class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        ability = input('Enter name of ability: ')
        damage = int(input('Enter max damage: '))
        return Ability(ability, damage)

    def create_weapon(self):
        weapon = input('Enter name of weapon: ')
        damage = int(input('Enter max damage: '))
        return Weapon(weapon, damage)

    def create_armor(self):
        armor = input('Enter name of armor: ')
        block = int(input('Enter max block: '))
        return Armor(armor, block)

    def create_hero(self):
        hero_health = 100
        hero_name = input('What is your hero name: ')
        new_hero = Hero(hero_name, hero_health)

        ability = input('Do you want to add an ability? Y/N')
        if ability == 'y':
            new_hero.abilities.append(self.create_ability())
        elif ability == 'n':
            print('No ability added')

        weapon = input('Do you want to add a weapon? Y/N')
        if weapon == 'y':
            new_hero.abilities.append(self.create_weapon())
        elif weapon == 'n':
            print('No weapon added')

        armor = input('Do you want to add any armor? Y/N')
        if armor == 'y':
            new_hero.armors.append(self.create_armor())
        elif armor == 'n':
            print('no armor added')

        return new_hero

    def build_team_one(self):
         team_name = input('What is the name of Team: ')
         self.team_one = Team(team_name)

         run = True
         while run:
             try:
                 num_heroes = int(input(f'How many heroes in {team_name}: '))
                 run = False
             except ValueError:
                 print('Try again')

         count = 0
         while count != num_heroes:
            self.team_one.heroes.append(self.create_hero())
            count += 1

         return self.team_one

    def build_team_two(self):
        team_two_name = input('What is the name of Team 2: ')
        self.team_two = Team(team_two_name)

        run = True
        while run:
            try:
                num_heroes = int(input(f'How many heroes in {team_two_name}: '))
                run = False
            except ValueError:
                print('Try again')


        count = 0
        while count != num_heroes:
            self.team_two.heroes.append(self.create_hero())
            count += 1

        return self.team_one

    def team_battle(self):
        # print(self.team_one)
        # print(self.team_two)
        self.team_one.attack(self.team_two)

    def team_dead(self, team):
        dead_count = 0

        for hero in team:
            if hero.current_health == 0:
                dead_count += 1
            else:
                dead_count = 0

            if dead_count == len(team):
                return True
            else:
                return False

    def show_stats(self):

        print(f'Team One Kill/Death Ratio: {self.team_one.stats()}')
        print(f'Team Two Kill/Death Ratio: {self.team_two.stats()}')



if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        # print('????')
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        elif play_again.lower() == 'y':
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()


        # else:
        #     #Revive heroes to play again
        #     arena.team_one.revive_heroes()
        #     arena.team_two.revive_heroes()






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

    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 300)
    # ability2 = Ability("Super Eyes", 130)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)

    # hero1 = Arena()
    # hero1.create_hero()
