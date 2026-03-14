from database.db import load_players, save_players
players = load_players()

shop_items = {"Health Potion":20, "Iron Sword":50, "Shield":40, "Magic Scroll":80}

def buy_item(player_id, item_name):
    player = players.get(str(player_id), {"gold":100, "inventory":[]})
    if item_name not in shop_items:
        return False, "Item not found"
    price = shop_items[item_name]
    if player['gold'] < price:
        return False, "Not enough gold"
    player['gold'] -= price
    player['inventory'].append(item_name)
    players[str(player_id)] = player
    save_players(players)
    return True, f"Bought {item_name} for {price} gold."
