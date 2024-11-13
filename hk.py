import random


class Hero:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} погиб.")
        else:
            print(f"{self.name} получил {damage} урона. Осталось здоровья: {self.health}")


class Witcher(Hero):
    def revive_hero(self, hero):
        if hero.health <= 0:
            print(f"{self.name} жертвует собой, чтобы воскресить {hero.name}!")
            hero.health = 50  # Восстанавливаем 50% здоровья
            print(f"{hero.name} возрожден с {hero.health} здоровья!")


class Magic:
    def __init__(self, increment):
        self.increment = increment

    def enhance_attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:  # Проверяем, жив ли герой
                hero.attack += self.increment
                print(f"{hero.name} увеличил урон на {self.increment}. Теперь его атака: {hero.attack}")


class Hacker:
    def __init__(self, damage):
        self.damage = damage

    def steal_health(self, boss, hero):
        if boss.health > 0:
            boss.health -= self.damage
            hero.health += self.damage
            print(f"Hacker забирает {self.damage} здоровья у босса и передает {hero.name}.")
            print(f"{hero.name} теперь имеет {hero.health} здоровья. Здоровье босса: {boss.health}")


class Boss:
    def __init__(self, health):
        self.health = health

    def attack_hero(self, hero):
        if hero.health > 0 and self.health > 0:  # Проверяем, жив ли герой
            damage = random.randint(10, 30)  # Урон от босса
            hero.take_damage(damage)


# Пример использования

# Создание героев
witcher = Witcher("Ведьмак", health=100, attack=20)
hero1 = Hero("Герой 1", health=80, attack=15)
hero2 = Hero("Герой 2", health=75, attack=18)

# Создание босса
boss = Boss(300)

# Создание магии и хакера
magic = Magic(increment=5)
hacker = Hacker(damage=20)

# Бой
for round in range(1, 6):  # 5 раундов
    print(f"\nРаунд {round}")

    # Атака босса по героям
    boss.attack_hero(hero1)
    boss.attack_hero(hero2)
    boss.attack_hero(witcher)

    # Увеличение атаки героев
    magic.enhance_attack([hero1, hero2, witcher])

    # Хакер "крадет" здоровье у босса
    hacker.steal_health(boss, hero1)  # Передаем здоровье первому герою

    # Если первый герой погиб, ведьмак пытается его воскресить
    if hero1.health <= 0:
        witcher.revive_hero(hero1)

    # Проверка на окончание боя
    if boss.health <= 0:
        print("Босс побежден! Герои одержали победу!")
        break

    # Проверка на то, все ли герои погибли
    if hero1.health <= 0 and hero2.health <= 0 and witcher.health <= 0:
        print("Все герои погибли! Босс победил!")
        break

