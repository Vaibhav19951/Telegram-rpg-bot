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

    # 🎒 INVENTORY FIX (HARD FIX)
    inventory = player.get("inventory")

    # agar inventory missing ya galat hai
    if not isinstance(inventory, list):
        inventory = []

    # item add
    item = f"{monster['name']} Loot"
    inventory.append(item)

    # IMPORTANT: wapas assign kar
    player["inventory"] = inventory

    rewards["item"] = item

    print("🔥 ITEM ADDED:", item)
    print("📦 FINAL INVENTORY:", player["inventory"])

    return rewards
