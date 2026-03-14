from telegram import Update
from telegram.ext import ContextTypes
import random

# Simple player data (future me DB me migrate karenge)
players = {}

def get_player(user_id, user_name):
    if user_id not in players:
        players[user_id] = {
            "name": user_name,
            "HP": 100,
            "Attack": 10,
            "Defense": 5,
            "Gold": 50
        }
    return players[user_id]

# Challenge system
async def challenge(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    player = get_player(user.id, user.first_name)

    # Simple boss
    bosses = [
        {"name": "Goblin Chief", "HP": 50, "Attack": 8},
        {"name": "Dark Mage", "HP": 70, "Attack": 12},
        {"name": "Stone Golem", "HP": 100, "Attack": 6}
    ]
    boss = random.choice(bosses)

    # Fight simulation (very simple)
    player_attack = player["Attack"] + random.randint(0,5)
    boss_attack = boss["Attack"] + random.randint(0,5)

    boss["HP"] -= player_attack
    player["HP"] -= boss_attack

    result_text = f"⚔️ You challenged {boss['name']}!\n"
    result_text += f"💥 You dealt {player_attack} damage!\n"
    result_text += f"🛡 {boss['name']} dealt {boss_attack} damage to you!\n"
    result_text += f"💖 Your HP: {player['HP']}\n"
    result_text += f"💀 {boss['name']} HP: {boss['HP']}\n"

    if boss["HP"] <= 0 and player["HP"] > 0:
        gold_earned = random.randint(10, 30)
        player["Gold"] += gold_earned
        result_text += f"\n🏆 You won and earned {gold_earned} gold!"
    elif player["HP"] <= 0:
        result_text += "\n☠️ You lost the challenge!"
    else:
        result_text += "\n🤺 Fight continues... Use /challenge again to attack!"

    await update.message.reply_text(result_text)
