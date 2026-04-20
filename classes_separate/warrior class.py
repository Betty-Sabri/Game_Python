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
            print(f"{self.name} attacks {target.name}. Attack missed...")
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


class Warrior(Creature):
    def __init__(self, name):
        super().__init__(name, 50)
        self.ability = {
            "attack": 5,
            "defence": 10,
            "speed": 4,
        }
        
        self.original_attack = self.ability["attack"]
        self.original_defence = self.ability["defence"]
        self.shield_up_active = False  # Track if shield is up
        self.round_count = 0

    def shield_up(self):
        if not self.shield_up_active:
            print(f"{self.name} takes a defensive stance!")
            self.ability["attack"] -= 4
            self.ability["defence"] += 4
            self.shield_up_active = True
        else:
            print(f"{self.name} already has their shield up.")

    def shield_down(self):
        if self.shield_up_active:  # Only revert if shield is currently active
            print(f"{self.name} stance returns to normal.")
            self.ability["attack"] = self.original_attack
            self.ability["defence"] = self.original_defence
            self.shield_up_active = False
        else:
            print(f"{self.name} does not have their shield up.")

    def attack(self, target):
        roll = random.randint(1, 20)

        if roll < 10:
            print(f"{self.name} attacks {target.name}. Attack missed...")
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

            if self.round_count == 1:
                print(f"Round {round_num}: {self.name} attacks {target.name} and takes a defensive stance!")
                self.attack(target)
                self.shield_up()

            elif self.round_count in [2, 3]:
                print(f"Round {round_num}: {self.name} attacks {target.name}!")
                self.attack(target)

            elif self.round_count == 4:
                print(f"Round {round_num}: {self.name} lowers shield and attacks {target.name}!")
                self.shield_down()
                self.attack(target)



gollum = Creature("Gollum")
boromir = Warrior("Boromir")


for round_num in range(1, 21):
    boromir.turn(round_num, [gollum])  
    gollum.turn(round_num, [boromir])  


    if gollum.hp <= 0:
        print(f"{gollum.name} has been defeated!")
        break
    elif boromir.hp <= 0:
        print(f"{boromir.name} has been defeated!")
        break
