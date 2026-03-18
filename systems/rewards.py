def give_rewards(player, monster):
    rewards = {}

    # 💰 GOLD
    gold = monster.get("gold", 20)
    player["gold"] = player.get("gold", 0) + gold
    rewards["gold"] = gold

    # ✨ XP
    xp = monster.get("xp", 10)
    player["xp"] = player.get("xp", 0) + xp
    rewards["xp"] = xp

    # 🎒 INVENTORY FIX (IMPORTANT)
    if "inventory" not in player or not isinstance(player["inventory"], list):
        player["inventory"] = []

    # 🎁 ITEM DROP
    item = f"{monster['name']} Loot"
    player["inventory"].append(item)
    rewards["item"] = item

    # 🔥 DEBUG PRINT
    print("Inventory now:", player["inventory"])

    return rewards
