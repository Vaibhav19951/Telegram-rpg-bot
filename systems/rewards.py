def give_rewards(player, monster):
    rewards = {}

    gold = monster.get("gold", 20)
    player["gold"] += gold
    rewards["gold"] = gold

    xp = monster.get("xp", 10)
    player["xp"] += xp
    rewards["xp"] = xp

    if "inventory" not in player:
        player["inventory"] = []

    item = f"{monster['name']} Loot"
    player["inventory"].append(item)
    rewards["item"] = item

    return rewards
