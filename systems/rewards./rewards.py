def give_rewards(player, monster):
    rewards = {}

    # 💰 gold
    gold = monster.get("gold", 20)
    player["gold"] += gold
    rewards["gold"] = gold

    # ✨ xp
    xp = monster.get("xp", 10)
    player["xp"] += xp
    rewards["xp"] = xp

    # 🎒 loot system
    loot = monster.get("loot", [])

    if loot:
        if "inventory" not in player:
            player["inventory"] = []

        item = loot[0]
        player["inventory"].append(item)
        rewards["item"] = item

    return rewards
