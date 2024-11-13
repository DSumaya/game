import random



class Hero:
    def __int__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name


    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value


    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.health} damage: {self.damage}'

class Magic(Hero):
    def __init__(self, name, health, damage, amount_attack ):
        super().__init__(self, name, health, damage)
        self.__amount_attack = amount_attack



    def increase_attack(self, heroes):
        for hero in heroes:
           if hero.health > 0:
               hero.attack += self.amount_attack
               print(f'{hero.name} увеличил урон на {self. amount_attack}. Его атака: {hero.attack}')

class Witcher(Hero):
    def __init__(self,name, health, damage, revive):
        super().__init__(self,name, health, damage )
        self.revive = revive

    def revive_hero(self, heroes):
        for hero in heroes:
            if hero.health <= 0:
                print(f'{self.name} жертвует собой для воскрешения {hero.name}')
                hero.health = 50
                print(f'{hero.name} возрожден с {hero.health} здоровья')

class Hacker(Hero):
    def __init__(self, name, health, damage, take_health ):
        super().__init__(self, name, health, damage)
        self.take_health = take_health

def steal_health(self, boss, hero):
    if boss.health > 0:
        boss.health -= self.take_health
        hero.health += self.take_health
        print(f'Hacker забирает {self.take_health} здоровье у Босса и передает {hero.name}'
              f'{hero.name} имеет {hero.health} здорровья. Здоровье Босса {boss.health}')

class Boss:
    def __init__(self, name, health, damage) :
        self.name = name
        self.health = health
        self.damage = damage


    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0 and self.health > 0:
                damage = random.randint(10,20)
                hero.take_damage(damage)

round_number = 0

def show_statistics(boss, heroes):
    print(f'ROUND - {round_number} ------------')
    print(boss)
    for hero in heroes:
        print(hero)

def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0:
            hero.attack(boss)
    show_statistics(boss, heroes)

def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
        return True
    return False

def start_game():
    boss = Boss(name ='Босс' , health = 1000, damage = 50 )
    magic = Magic(name = 'Маг', health= 150, damage= 20, amount_attack= 25)
    wither = Witcher(name= 'Ведьмак', health= 150, damage= 0)
    hacker = Hacker(name= 'Хакер', helth= 150, damage= 25)
    heroes_list = [magic, wither,]

    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()













