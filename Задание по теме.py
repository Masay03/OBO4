from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")
        return 10  # Условный урон мечом

class Bow(Weapon):
    def attack(self):
        print("Боец наносит удар из лука.")
        return 7  # Условный урон из лука

class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        if isinstance(weapon, Sword):
            print("Боец выбирает меч.")
        elif isinstance(weapon, Bow):
            print("Боец выбирает лук.")

    def attack(self, monster):
        damage = self.weapon.attack()
        monster.take_damage(damage)

class Monster:
    def __init__(self, health: int):
        self.health = health

    def take_damage(self, damage: int):
        self.health -= damage
        if self.health <= 0:
            print("Монстр побежден!")
        else:
            print(f"У монстра осталось {self.health} здоровья.")

sword = Sword()
bow = Bow()
fighter = Fighter(sword)
monster = Monster(10)

fighter.attack(monster)

fighter.change_weapon(bow)
fighter.attack(monster)

