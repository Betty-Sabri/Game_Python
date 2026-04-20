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

class Archer(Creature):
    def __init__(self, name):
        super().__init__(name, 30)
        self.ability = {
            "attack": 7,
            "defence": 9,
            "speed": 8,
        }
        
        self.original_attack = self.ability["attack"]
        self.original_defence = self.ability["defence"]
        self.round_count = 0

    def power_shot(self, target):

        roll1 = random.randint(1,20)
        roll2 = random.randint(1,20)
        roll = max(roll1, roll2)

        if self.ability["speed"] > target.ability["speed"]:
            speed_add = self.ability["speed"] - target.ability["speed"]
            roll += speed_add
        else:
            self.ability["attack"] += 3
            self.ability["defence"] -= 3


        if roll < 10:
            print(f"{self.name} uses Power Shot on {target.name}. Attack missed...")
        else:
            damage = random.randint(1, 8) + self.ability["attack"]
            print(f"{self.name} uses Power Shot on {target.name} for {damage} damage!")
            target.hp -= damage
            return target.check_life()
        return False
    

    def attack(self, target):
        self.ability["attack"] = self.original_attack
        self.ability["defence"] = self.original_defence
        return super().attack(target)
    
    def auto_select(self, target_list):
        
        sorted_targets = sorted(target_list, key=lambda t: t.hp)
        target = sorted_targets[0]

        print(f"This is the selected archer: {target.name}.")
        return target
    
    def turn(self, round_num, target_list):
        if self.hp > 0:
            self.round_count += 1
            if self.round_count > 4:
                self.round_count = 1

            target = self.auto_select(target_list)
            if self.round_count == 1:
                print(f"{self.name} attacks {target.name}.")
                self.attack(target)
            elif self.round_count in [2, 3, 4]:
                print(f"{self.name} uses Power Shot on {target.name}.")
                self.power_shot(target)

class Fighter(Creature):
    def __init__(self, name):
        super().__init__(name, 50)
        self.ability = {
            "attack": 5,
            "defence": 8,
            "speed": 5,
        }
    
    def auto_select(self, target_list):

        target = max(target_list, key=lambda t: t.hp)
        print(f"This is the selected fighter: {target.name}.")
        return target
    
    def turn(self, round_num, target_list):

        if self.hp > 0:
            target = self.auto_select(target_list)

            # First attack
            print(f"{self.name} attacks {target.name}.")
            if self.attack(target):
                target_list.remove(target)
                target = self.auto_select(target_list)

            # Second attack
            self.ability["attack"] -= 3
            print(f"{self.name} attacks {target.name} with reduced power.")
            if target and target.hp > 0 and self.attack(target):
                target_list.remove(target)
                target = self.auto_select(target_list)

            # Third attack
            print(f"{self.name} attacks {target.name} with reduced power.")
            if target and target.hp > 0 and self.attack(target):
                target_list.remove(target)


# Create Archer and Fighter
archer = Archer("Legolas")
fighter = Fighter("Aragorn")

# Target list
archer_targets = [fighter]
fighter_targets = [archer]


for round_num in range(1, 21):
    print(f"Round {round_num}:")
    
    # Archer's turn
    archer.turn(round_num, archer_targets)
    if fighter.hp <= 0:
        print(f"{fighter.name} has been defeated! {archer.name} wins!")
        break

    # Fighter's turn
    fighter.turn(round_num, fighter_targets)
    if archer.hp <= 0:
        print(f"{archer.name} has been defeated! {fighter.name} wins!")
        break


