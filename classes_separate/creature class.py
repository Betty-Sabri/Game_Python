import random

class Creature:
    def __init__(self, name, hp=10):
        self.name = name
        self.hp = hp
        self.ability = {
        "attack": 1,
        "defence": 5,
        "speed": 5,
        }

    def check_life(self):
        if self.hp <= 0:
            print (f"{self.name} fainted.")
            self.hp = 0
            return True
        else:
            print (f"{self.name} health points: {self.hp}")
            return False
        
    
    def attack(self, target):

        roll = random.randint(1,20)

        if roll < 10:
            print (f"{self.name} attacks {target.name}. Attack missed...")
        else:
            attack = random.randint(1,4)
            print(f"{self.name} attacks {target.name} for {attack} damage!")
            target.hp -= attack
            return target.check_life()
        return False

    def auto_select(self, target_list):
        target = random.choice(target_list)
        if target is None:
            print("No creature was selected.")
            return None
        else:
            print(f"This is the selected creature: {target.name}.")
            return target
    
    def turn(self, target_list):
        if self.hp > 0:
            target = self.auto_select(target_list)
            if self.attack(target):
                exit()

my_creatures = [
    Creature('Fairy'),
    Creature('Griffin'),
    Creature('Frodo'),

]

enemy_creatures = [
    Creature('Golem'),
    Creature('Pimpin'),
    Creature('Minotaur'),
]

for round_num in range(1, 21):
    print(f"Round {round_num}")
    for creature in my_creatures:
        creature.turn(enemy_creatures)
    for creature in enemy_creatures:
        creature.turn(my_creatures)

