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
            print(f"{self.name} fainted.")
            self.hp = 0
            return True
        else:
            print(f"{self.name} health points: {self.hp}")
            return False

    def attack(self, target):
        roll = random.randint(1, 20)
        if roll < 10:
            print(f"{self.name} attacks {target.name}. Attack missed.")
        else:
            attack = random.randint(1, 4)
            print(f"{self.name} attacks {target.name}. Attack hits for {attack} damage!")
            target.hp -= attack
            return target.check_life()
        return False

    def auto_select(self, target_list):
        target = random.choice(target_list)
        if target is None:
            print("No creature was selected.")
            return None
        else:
            return target

    def turn(self, round_num, target_list):
        if self.hp > 0:
            target = self.auto_select(target_list)
            self.attack(target)

class Goblin(Creature):
    def __init__(self, name):
        super().__init__(name, 15)
        self.ability = {
            "attack": 3,
            "defence": 6,
            "speed": 6,
        }

class Orc(Creature):
    def __init__(self, name):
        super().__init__(name, 50)
        self.ability = {
            "attack": 5,
            "defence": 8,
            "speed": 3,
        }
        self.original_attack = self.ability["attack"]
        self.original_defence = self.ability["defence"]
        self.in_rage = False  # To track if Orc is in rage state
        self.round_count = 0  # To track the rounds for strategy

    def heavy_attack(self, target):
        if not self.in_rage:
            self.ability["attack"] += 5
            self.ability["defence"] -= 3
            self.in_rage = True 

        roll = random.randint(1, 20)
        if roll < 10:
            print(f"{self.name} performs a heavy attack on {target.name}. Attack missed.")
        else:
            attack = random.randint(1, 4) + self.ability["attack"] 
            print(f"{self.name} performs a heavy attack on {target.name}. Attack hits for {attack} damage!")
            target.hp -= attack
            return target.check_life()
        return False

    def attack(self, target):
        if self.in_rage:
            print(f"{self.name} cooled down!")
            self.ability["attack"] = self.original_attack
            self.ability["defence"] = self.original_defence
            self.in_rage = False 

        roll = random.randint(1, 20)
        if roll < 10:
            print(f"{self.name} attacks {target.name}. Attack missed.")
        else:
            attack = random.randint(1, 4) + self.ability["attack"]  
            print(f"{self.name} attacks {target.name}. Attack hits for {attack} damage!")
            target.hp -= attack
            return target.check_life()
        return False

    def turn(self, round_num, target_list):
        if self.hp > 0:
            self.round_count += 1
            if self.round_count > 4:
                self.round_count = 1 

            target = self.auto_select(target_list)
            if self.round_count in [1, 2, 3]:
                print(f"Round {round_num}:")
                print(f"{self.name} attacks {target.name}.")
                self.attack(target)
            # Round 4 - heavy attack
            elif self.round_count == 4:
                print(f"Round {round_num}:")
                print(f"{self.name} attacks {target.name}.")
                self.heavy_attack(target)


orc = Orc("Orc")
goblin = Goblin("Goblin")


for round_num in range(1, 21):
    orc.turn(round_num, [goblin])  
    goblin.turn(round_num, [orc])  


    if orc.hp <= 0:
        print(f"{orc.name} has been defeated!")
        break
    elif goblin.hp <= 0:
        print(f"{goblin.name} has been defeated!")
        break
