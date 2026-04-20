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



wizard = Wizard("Merlin")
wizard.mana = 20

creature1 = Creature("Aragorn", 41)
creature2 = Creature("Legolas", 30)
creature3 = Creature("Gandalf", 13)

target_list = [creature1, creature2, creature3]


# 1. Wizard attacks a target
selected_target = wizard.select_target([creature1, creature2, creature3])
wizard.attack(selected_target)

# 2. Wizard recharges mana
wizard.recharge()
print(f"{wizard.name}'s mana after recharge: {wizard.mana}")

# 3. Wizard performs a fire bolt
wizard.fire_bolt(selected_target)

# 4. Wizard heals a target
wizard.heal(creature1)

# 5. Wizard performs a mass heal on all allies
wizard.mass_heal([wizard, creature1, creature2])

# 6. Wizard casts Fire Storm on all enemies
wizard.fire_storm(target_list)

