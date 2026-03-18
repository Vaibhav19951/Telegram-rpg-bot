import random
from database.db import users

HUNTERS = [
    ("Yoo Jinho", "E"),
    ("Han Song-Yi", "D"),
    ("Woo Jinchul", "C"),
    ("Jung Yerim", "B"),
    ("Baek Yoonho", "A"),
    ("Cha Hae-In", "S"),
    ("Thomas Andre", "SS"),
]

def summon_rank():
    roll = random.uniform(0, 100)

    if roll < 40:
        return "E"
    elif roll < 65:
        return "D"
    elif roll < 80:
        return "C"
    elif roll < 90:
        return "B"
    elif roll < 97:
        return "A"
    elif roll < 99.8:
        return "S"
    return "SS"

async def summon(update, context):
    user = update.effective_user
    players = context.bot_data.get("players", {})
    player = players.get(user.id)

    if not player:
        await update.message.reply_text("First use /start")
        return

    player["summons"] += 1
    total = player["summons"]

    forced_rank = None
    if total % 200 == 0:
        forced_rank = "SS"
    elif total % 100 == 0:
        forced_rank = "S"
    elif total % 50 == 0:
        forced_rank = "A"

    rank = forced_rank if forced_rank else summon_rank()

    possible = [name for name, r in HUNTERS if r == rank]
    hunter = random.choice(possible)

    if hunter not in player["hunters"]:
        player["hunters"].append(hunter)
        result_text = f"🎰 Summoning...\n\n✨ {rank} Rank Hunter Found!\n\n{hunter} joined your hunters."
    else:
        player["gold"] += 50
        result_text = (
            f"🎰 Summoning...\n\n"
            f"✨ {rank} Rank Hunter Found!\n\n"
            f"{hunter} was a duplicate.\n"
            f"You got 50 gold instead."
        )

    result_text += f"\n\nTotal Summons: {total}"

    await update.message.reply_text(result_text)
