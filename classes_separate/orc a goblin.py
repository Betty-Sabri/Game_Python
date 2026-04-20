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


class Goblin(Creature):
    def __init__(self, name):
        super().__init__(name, 15)
        self.ability = {
            "attack": 3,
            "defence": 6,
            "speed": 6,
        }


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


class OrcGeneral(Orc, Warrior):
    def __init__(self, name):
        Creature.__init__(self, name, 80)
        self.ability = {
            "attack": 5,
            "defence": 8,
            "speed": 3,
        }
        self.original_attack = self.ability["attack"]
        self.original_defence = self.ability["defence"]
        self.round_count = 0
        self.in_rage = False
        self.shield_up_active = False
    
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
            
            elif self.round_count == 2:
                    print(f"Round {round_num}: {self.name} attacks {target.name}!")
                    self.attack(target)
            
            elif self.round_count == 3:
                    print(f"Round {round_num}: {self.name} lowers shield and attacks {target.name}!")
                    self.shield_down()
                    self.attack(target)
            
            elif self.round_count == 4:
                    print(f"Round {round_num}:")
                    print(f"{self.name} attacks {target.name}.")
                    self.heavy_attack(target)
    
    def auto_select(self, target_list):
        return target_list[0]

class GoblinKing(Goblin, Archer):
      
    def __init__(self, name):
        Goblin.__init__(self, name)
        Archer.__init__(self, name)
        self.hp = 50
        self.ability = {
            "attack": 3,
            "defence": 6,
            "speed": 6,
        }
        self.round_count = 0
        self.original_attack = self.ability["attack"]
        self.original_defence = self.ability["defence"]
    
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



orc_general = OrcGeneral("Orc General")
goblin_king = GoblinKing("Goblin King")
    
for round_num in range(1, 21):

    orc_general.turn(round_num, [goblin_king])
    if goblin_king.hp <= 0:
        print(f"{goblin_king.name} has been defeated! {orc_general.name} wins!")
        break

    goblin_king.turn(round_num, [orc_general])
    if orc_general.hp <= 0:
        print(f"{orc_general.name} has been defeated! {goblin_king.name} wins!")
        break