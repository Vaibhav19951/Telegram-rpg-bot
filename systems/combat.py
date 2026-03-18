import random


def calculate_damage(player):
    base = player.get("strength", 10)
    return random.randint(base, base + 10)


def monster_damage():
    return random.randint(5, 15)


def fight(player, monster):
    player_hp = player.get("hp", 100)
    monster_hp = monster.get("hp", 50)

    log = []

    while player_hp > 0 and monster_hp > 0:
        dmg = calculate_damage(player)
        monster_hp -= dmg
        log.append(f"⚔️ You hit {monster['name']} for {dmg}")

        if monster_hp <= 0:
            return True, log

        dmg = monster_damage()
        player_hp -= dmg
        log.append(f"💀 {monster['name']} hit you for {dmg}")

    return False, log
