from database.db import load_players, save_players
players = load_players()

def add_item(player_id, item):
    player = players.get(str(player_id), {"inventory":[], "gold":100})
    player['inventory'].append(item)
    players[str(player_id)] = player
    save_players(players)

def remove_item(player_id, item):
    player = players.get(str(player_id), {"inventory":[]})
    if item in player['inventory']:
        player['inventory'].remove(item)
        players[str(player_id)] = player
        save_players(players)
        return True
    return False
