# Battle Game (Python OOP)

A turn-based fantasy battle simulator built using Python Object-Oriented Programming. The project demonstrates inheritance, polymorphism, AI decision-making, and a full battle system with multiple character classes and abilities.

---

## Features

- Object-oriented design with multiple character classes
- Turn-based combat system with rounds
- Randomized attack and damage mechanics
- Special abilities per class (rage, shield, magic, power shots)
- AI-based target selection strategies
- Boss enemy that joins mid-battle
- Win/loss detection system

---

## Class Overview

### Base Class: Creature
- Core attributes: `name`, `hp`, `ability`
- Basic attack system with hit/miss logic
- Automatic life check (`check_life`)
- Random target selection

---

### Enemy Classes
- **Goblin**: Fast, low HP attacker
- **Orc**: Tank with rage and heavy attacks
- **OrcGeneral**: Hybrid of Orc and Warrior abilities
- **GoblinKing**: Combines Goblin + Archer mechanics
- **Boss**: Advanced AI targeting (strong/weak/random decisions)

---

### Ally Classes
- **Warrior**: Defensive fighter using shield mechanics
- **Archer**: High-speed attacker with power shot ability
- **Fighter**: Multi-hit aggressive attacker
- **Wizard**: Magic-based unit with:
  - Mana system
  - Fire bolt
  - Healing and mass heal
  - Fire storm AoE attack

---

## Battle System

### Class: Battle
Manages the full simulation:

- Sorts units by speed
- Executes enemy and ally turns each round
- Handles attacks and HP updates
- Introduces boss when conditions are met
- Checks victory conditions after each round

---

## Gameplay Loop

1. Initialize enemies, allies, and boss
2. Start battle
3. Each round:
   - Enemies attack
   - Allies attack
   - Boss may join mid-game
4. Repeat until one side is defeated

---

## Key Mechanics

- Randomized combat rolls (1–20 system)
- HP-based survival system
- Ability cooldowns and round-based skills
- Dynamic AI targeting strategies
- Resource management (Wizard mana system)

---

## How to Run

```bash
python battle_game.py
