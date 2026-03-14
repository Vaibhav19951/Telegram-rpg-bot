import random
from database.db import load_players, save_players

players = load_players()

def fight(player_id, player_name, enemy):
    player = players.get(str(player_id), {"HP":100, "Attack":10, "Defense":5, "Gold":50})
    player_attack = player['Attack'] + random.randint(0,5)
    enemy_attack = enemy['Attack'] + random.randint(0,5)
    enemy['HP'] -= player_attack
    player['HP'] -= enemy_attack
    result = {
        "player_hp": player['HP'],
        "enemy_hp": enemy['HP'],
        "damage_dealt": player_attack,
        "damage_taken": enemy_attack
    }
    if enemy['HP'] <=0 and player['HP']>0:
        gold = random.randint(10,30)
        player['Gold'] += gold
        result['win']=True
        result['gold']=gold
    elif player['HP']<=0:
        result['lost']=True
    players[str(player_id)] = player
    save_players(players)
    return result
