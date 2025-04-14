from abc import ABC, abstractmethod


# Шаг 1: Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


# Шаг 2: Конкретные реализации оружия
class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"


class Bow(Weapon):
    def attack(self):
        return "стреляет из лука"


class Axe(Weapon):
    def attack(self):
        return "рубит топором"


class MagicWand(Weapon):
    def attack(self):
        return "кастует заклинание"


# Шаг 3: Класс бойца
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None  # Изначально без оружия

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.__class__.__name__.lower()}.")

    def attack(self):
        if self.weapon:
            print(f"{self.name} {self.weapon.attack()}.")
        else:
            print(f"{self.name} бьёт кулаками.")


# Класс монстра
class Monster:
    def __init__(self, name, health=10):
        self.name = name
        self.health = health

    def is_defeated(self):
        return self.health <= 0

    def take_hit(self):
        self.health -= 5
        if self.is_defeated():
            print(f"{self.name} побежден!")
        else:
            print(f"{self.name} получает урон! Осталось здоровья: {self.health}")


# Шаг 4: Механизм боя
def battle(fighter: Fighter, monster: Monster):
    print("\nНачинается бой!")
    fighter.attack()
    monster.take_hit()
    if not monster.is_defeated():
        print("Монстр выжил и контратакует!")
        print(f"{monster.name} атакует бойца!")
    else:
        print("Бой окончен!")


# Демонстрация
if __name__ == "__main__":
    # Создаем персонажей
    hero = Fighter("Боец")
    orc = Monster("Орк")

    # Бой с разным оружием
    hero.change_weapon(Sword())
    battle(hero, orc)

    # Новый монстр
    troll = Monster("Тролль", 15)
    hero.change_weapon(Bow())
    battle(hero, troll)

    # Добавляем новое оружие БЕЗ изменения существующего кода
    hero.change_weapon(Axe())
    battle(hero, Monster("Гоблин"))

    hero.change_weapon(MagicWand())
    battle(hero, Monster("Дракон", 20))