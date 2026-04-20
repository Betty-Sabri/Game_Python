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


class Boss(Orc):
    def __init__(self, name):
        Creature.__init__(self, name, 200)
        self.ability = {
            "attack": 5,
            "defence": 8,
            "speed": 5,
        }
        self.original_attack = self.ability["attack"]
        self.original_defence = self.ability["defence"]
        self.round_count = 0
        self.in_rage = False
    

    def auto_select(self, target_list, mode="Random"):
        
        if mode == "Strong":
            target = max(target_list, key=lambda t: t.hp)
            print(f"Targetting the strongest: {target.name} with {target.hp} HP.")
        
        elif mode == "Weak":
            target = min(target_list, key=lambda t: t.hp)
            print(f"Targetting the weakest: {target.name} with {target.hp} HP.")
        
        elif mode == "Random":
            weakest = min(target_list, key=lambda t: t.hp)
            strongest = max(target_list, key=lambda t: t.hp)
            target = random.choice([weakest, strongest])
            print(f"Randomly targeting: {target.name} with {target.hp} HP.")
        
        return target

    def turn(self, round_num, target_list):
        if self.hp > 0:
            self.round_count += 1
            if self.round_count > 4:
                self.round_count = 1

            if round_num == 1:
                target = self.auto_select(target_list, mode="Weak")
                print(f"{self.name} attacks {target.name}.")
                if self.attack(target):
                    if not target_list:
                        return
            
                for _ in range(2):
                    target = self.auto_select(target_list, mode="Random")
                    print(f"{self.name} attacks {target.name}.")
                    if self.attack(target):
                        if not target_list:
                            return
            
            elif round_num in [2,3,4]:
                target = self.auto_select(target_list, mode="Strong")
                print(f"{self.name} performs a heavy attack on {target.name}.")
                self.heavy_attack(target)

class Wizard(Creature):
    def __init__(self, name):
        super().__init__(name, 20)
        self.ability = {
            "attack": 3,
            "defence": 5,
            "speed": 5,
        }
        self.mana = 0
        self.arcana = 10
    
    def set_mana(self, value):
        if value < 0:
            print("Effect failed.")
        elif value > 100:
            print("Mana cannot exceed 100.")
            self.mana = 100
        else:
            self.mana = value
    
    def attack(self, target):
        print(f"\nUsing attack:")
        self.mana += 20
        print("Mana: +20!")
        print(f"{self.name} attacks {target.name}")

        roll = random.randint(1, 20)
        if roll < 10:
            print("Attack missed...")
        else:
            attack = random.randint(1, 4)
            print(f"Attack hits for {attack} attack!")
            target.hp -= attack
            target.check_life()
    
    def recharge(self):
        print(f"\nUsing recharge:")
        self.mana += 30
        print(f"{self.name} channels magical energy...")
        print("Mana: +30!")
        if self.mana > 100:
            self.mana = 100
            print(f"Mana is full!")
        print(f"{self.name} mana after recharge: {self.mana}")
    
    def fire_bolt(self, target):
        print("\nUsing fire bolt:")
        if self.hp <= 0:
            print(f"{self.name} cannot attack.")
            return
        print(f"{self.name} casts Fire Bolt at {target.name}")
        
        roll = random.randint(1, 20) + (self.arcana // 2)
        if roll < 10:
            print(f"Attack missed")
        else:
            attack = random.randint(1, self.arcana)
            print(f"{self.name} casts Fire Bolt at {target.name} for {attack} attack!")
            target.hp -= attack
            self.set_mana(self.mana + 10)
            print(f"Mana: +10!")
            return target.check_life()
    
    def heal(self, target):
        print("\nUsing heal:")
        if self.mana < 20:
            print(f"{self.name} does not have enough Mana points to heal.")
            return

        print("Mana: -20!")
        self.set_mana(self.mana - 20)
        amount_healed = random.randint(0, 8) + (self.arcana // 2)
        target.hp += amount_healed
        print(f"{self.name} heals {target.name} for {amount_healed} HP.")
        print(f"{target.name} now has {target.hp} HP.")
    
    def mass_heal(self, allies):
        print("\nUsing mass heal:")
        if self.mana < 30:
            print(f"{self.name} does not have enough Mana points.")
            return
        
        print("Mana: -30!")
        self.set_mana(self.mana - 30)
        amount_healed = random.randint(0, 10) + self.arcana
        print(f"{self.name} casts Mass Heal, restoring {amount_healed} HP to all allies.")

        for ally in allies:
            ally.hp += amount_healed
            print(f"{ally.name} now has {ally.hp} HP.")
    
    def fire_storm(self, enemies):
        print("\nUsing fire storm:")
        if self.mana < 50:
            print(f"{self.name} does not have enough Mana points.")
            return
        
        print("Mana: -50!")
        self.set_mana(self.mana - 50)
        print(f"{self.name} casts Fire storm, damaging all enemies.")

        for enemy in enemies:
            roll = random.randint(1, 20) + enemy.ability["speed"]
            full_damage = random.randint(5, 20) + self.arcana

            if roll >= self.arcana:
                damage = full_damage // 2
                print(f"{enemy.name} takes {damage} damage.")
            else:
                damage = full_damage
                print(f"{enemy.name} takes {damage} damage (full damage).")
            
            enemy.hp -= damage
            enemy.check_life()


    def select_target(self, target_list):
        for i in range(len(target_list)):
            print(f"{i + 1}: {target_list[i].name}, HP: {target_list[i].hp}")


        while True:
                try:
                    choice = int(input("Select the target by entering a number: "))
                    if choice >= 1 and choice <= len(target_list):
                        return target_list[choice - 1]
                    else:
                        print(f"Invalid choice. Choose a number again.")
                        choice = int(input("Select the target by entering a number: "))
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    choice = int(input("Select the target by entering a number: "))



class Battle:
    def __init__(self, all_enemies, all_allies, boss):
        self.all_enemies = all_enemies
        self.all_allies = all_allies
        self.boss = boss
        self.boss_added = False

    def start(self):
        print("The battle begins")
        self.all_enemies.sort(key=lambda creature: creature.ability["speed"], reverse=True)
        self.all_allies.sort(key=lambda creature: creature.ability["speed"], reverse=True)

    def turn(self, round_num):
        print(f"\nRound {round_num}")

        # Enemies' turn
        print("\nEnemies Turn:")
        for enemy in self.all_enemies:
            if enemy.check_life() > 0:
                print(f"{enemy.name} prepares to attack.")
                target = random.choice([ally for ally in self.all_allies if ally.check_life()])
                attack = random.randint(1, 20)
                print(f"{enemy.name} attacks {target.name} for {attack} attack!")
                target.hp -= attack
                print(f"{target.name} now has {target.hp} HP remaining.")
                if target.hp <= 0:
                    print(f"{target.name} has fainted!")
            else:
                print(f"{enemy.name} is defeated and cannot act.")

        # Add the boss if conditions are met
        if not self.boss_added and len([boss for boss in self.all_enemies if boss.check_life()]) == 1:
            print("\nThe Boss joins the fight!")
            self.all_enemies.append(self.boss)
            self.all_enemies.sort(key=lambda creature: creature.ability["speed"], reverse=True)
            self.boss_added = True

        # Allies' turn
        print("\nAllies Turn:")
        for ally in self.all_allies:
            if ally.check_life() > 0:
                print(f"{ally.name} prepares to attack.")
                target = random.choice([enemy for enemy in self.all_enemies if enemy.check_life()])
                attack = random.randint(1, 20)
                print(f"{ally.name} attacks {target.name} for {attack} attack!")
                target.hp -= attack
                print(f"{target.name} now has {max(0, target.hp)} HP remaining.")
                if target.hp <= 0:
                    print(f"{target.name} has fainted!")
            else:
                print(f"{ally.name} is defeated and cannot act.")

        # Victory check
        if not any(enemy.check_life() for enemy in self.all_enemies):
            print("\nAll enemies have been defeated! Allies win!")
            return True
        if not any(ally.check_life() for ally in self.all_allies):
            print("\nAll allies have been defeated! Enemies win!")
            return True
        return False
    

enemies_list = [OrcGeneral("Orc General"), Goblin("Goblin 1"), Goblin("Goblin 2"), Orc("Orc 1"), Orc("Orc 2")]
allies_list = [Fighter("Fighter"), Warrior("Warrior"), Creature("Creature"), Archer("Archer")]
boss = OrcGeneral("Boss Orc")


battle = Battle(all_enemies=enemies_list, all_allies=allies_list, boss=boss)

# Start the battle
battle.start()
for round_num in range(1, 21):
    if battle.turn(round_num):
        break
