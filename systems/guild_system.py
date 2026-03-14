import random
from database.db import load_players, save_players
players = load_players()

def pvp_attack(player1_id, player2_id):
    p1 = players.get(str(player1_id), {"HP":100, "Attack":10})
    p2 = players.get(str(player2_id), {"HP":100, "Attack":10})

    p1_attack = p1['Attack'] + random.randint(0,5)
    p2_attack = p2['Attack'] + random.randint(0,5)

    p1['HP'] -= p2_attack
    p2['HP'] -= p1_attack

    players[str(player1_id)] = p1
    players[str(player2_id)] = p2
    save_players(players)

    return {"player1_hp": p1['HP'], "player2_hp": p2['HP'], "p1_dealt": p1_attack, "p2_dealt": p2_attack}
