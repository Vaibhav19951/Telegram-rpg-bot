import random

def calculate_damage(attacker, defender, move_type="basic"):
    base_damage = attacker["strength"] * 5

    if move_type == "skill":
        base_damage += attacker["intelligence"] * 3

    crit = False
    if random.random() < 0.1:
        base_damage *= 1.5
        crit = True

    defence = defender["vitality"] * 2
    final_damage = int(max(1, base_damage - defence))

    return final_damage, crit
