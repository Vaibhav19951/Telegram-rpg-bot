import random

MONSTERS = [
    # E Rank
    {"name": "Goblin", "rank": "E", "hp": 50, "xp": 20, "gold": 15},
    {"name": "Wild Wolf", "rank": "E", "hp": 60, "xp": 25, "gold": 20},
    {"name": "Skeleton", "rank": "E", "hp": 55, "xp": 22, "gold": 18},

    # D Rank
    {"name": "Orc", "rank": "D", "hp": 80, "xp": 35, "gold": 30},
    {"name": "Lizardman", "rank": "D", "hp": 90, "xp": 40, "gold": 35},
    {"name": "Dark Mage", "rank": "D", "hp": 85, "xp": 45, "gold": 40},

    # C Rank
    {"name": "Ogre", "rank": "C", "hp": 120, "xp": 70, "gold": 60},
    {"name": "Shadow Beast", "rank": "C", "hp": 130, "xp": 75, "gold": 65},
    {"name": "Stone Golem", "rank": "C", "hp": 140, "xp": 80, "gold": 70},

    # B Rank
    {"name": "Demon Knight", "rank": "B", "hp": 180, "xp": 120, "gold": 100},
    {"name": "Frost Giant", "rank": "B", "hp": 200, "xp": 140, "gold": 120},
    {"name": "Hell Hound", "rank": "B", "hp": 190, "xp": 130, "gold": 110},

    # A Rank
    {"name": "Ancient Dragon", "rank": "A", "hp": 350, "xp": 300, "gold": 250},
    {"name": "Demon General", "rank": "A", "hp": 320, "xp": 280, "gold": 230},
    {"name": "Red Wyvern", "rank": "A", "hp": 300, "xp": 260, "gold": 220},
]

# Yahan apne image links daal
# Jis monster ka link nahi hoga uski image skip ho jayegi
MONSTER_IMAGES = {
    "Goblin": "https://tse3.mm.bing.net/th/id/OIP.Fi-ADUBhjshVp8r5ErYzgAAAAA?rs=1&pid=ImgDetMain&o=7&rm=3",
    "Wild Wolf": "https://i.pinimg.com/originals/a7/19/ea/a719ea2f8326c3453e8af5a280c24571.jpg",
    "Skeleton": "https://th.bing.com/th/id/OIP.eA52W1ensEqMqjjBjT8IsgHaEK?o=7rm=3&rs=1&pid=ImgDetMain&o=7&rm=3",
    "Orc": "https://i.redd.it/n5csiyeqfgz31.jpg",
    "Lizardman": "https://tse4.mm.bing.net/th/id/OIP.f7MkoQniATZmX949OjigEgHaHa?rs=1&pid=ImgDetMain&o=7&rm=3",
    "Dark Mage": "https://tse3.mm.bing.net/th/id/OIP.vjM5EaW-tQjQGlE7cMnayQAAAA?rs=1&pid=ImgDetMain&o=7&rm=3",
    "Ogre": "https://static0.cbrimages.com/wordpress/wp-content/uploads/2024/02/img_0980.jpeg?q=70&fit=crop&w=825&dpr=1",
    "Shadow Beast": "https://tse4.mm.bing.net/th/id/OIP.v-6JpsSbeK9pmrUya6Bp0wAAAA?rs=1&pid=ImgDetMain&o=7&rm=3",
    "Stone Golem": "https://fictionhorizon.com/wp-content/uploads/2024/01/StoneGolem-768x432.jpg",
    "Demon Knight": "https://i.pinimg.com/736x/d3/ae/d6/d3aed687dd009080376bc71d3040a7ea.jpg",
    "Frost Giant": "https://tse2.mm.bing.net/th/id/OIP.YudqKb3Aj4wofPGLWq3CcAAAAA?rs=1&pid=ImgDetMain&o=7&rm=3",
    "Hell Hound": "https://tse4.mm.bing.net/th/id/OIP.NoNkF77LZeq0xtGHo7R7uAHaEK?w=1920&h=1080&rs=1&pid=ImgDetMain&o=7&rm=3",
    "Ancient Dragon": "https://i.pinimg.com/originals/e4/17/f0/e417f02fecd6fa7aded6eb03e892a362.jpg",
    "Demon General": "https://tse2.mm.bing.net/th/id/OIP.hw7lLUoYE4b3wBu6PQhzzAAAAA?rs=1&pid=ImgDetMain&o=7&rm=3",
    "Red Wyvern": "https://i.pinimg.com/originals/14/e7/b6/14e7b6141ed7f6a22aa09d290c0d43b3.jpg",
}

def get_required_xp(level: int) -> int:
    if level >= 30:
        return 30000
    return level * level * 100

def get_monster_by_level(player_level: int):
    if player_level <= 5:
        pool = [m for m in MONSTERS if m["rank"] == "E"]
    elif player_level <= 10:
        pool = [m for m in MONSTERS if m["rank"] in ["E", "D"]]
    elif player_level <= 15:
        pool = [m for m in MONSTERS if m["rank"] in ["D", "C"]]
    elif player_level <= 20:
        pool = [m for m in MONSTERS if m["rank"] in ["C", "B"]]
    else:
        pool = [m for m in MONSTERS if m["rank"] in ["B", "A"]]

    return random.choice(pool)

async def hunt(update, context):
    user = update.effective_user
    players = context.bot_data.get("players", {})
    player = players.get(user.id)

    if not player:
        await update.message.reply_text("First use /start")
        return

    monster = get_monster_by_level(player["level"])

    image_url = MONSTER_IMAGES.get(monster["name"])
    if image_url and image_url.startswith("http"):
        try:
            await update.message.reply_photo(photo=image_url)
        except Exception:
            pass

    # Basic damage
    damage = player["strength"] * 5

    # Aura bonus
    aura = player.get("aura", "").lower()
    if aura == "fire":
        damage = int(damage * 1.20)
    elif aura == "light":
        damage = int(damage * 1.10)

    # Crit chance
    crit = False
    crit_chance = player.get("sense", 0) * 0.01

    if aura == "lightning":
        crit_chance += 0.15

    if random.random() < crit_chance:
        damage = int(damage * 1.5)
        crit = True

    monster_hp_left = monster["hp"] - damage

    gained_xp = monster["xp"]
    gained_gold = monster["gold"]

    player["xp"] += gained_xp
    player["gold"] += gained_gold

    level_up_text = ""

    required = get_required_xp(player["level"])
    while player["xp"] >= required:
        player["xp"] -= required
        player["level"] += 1
        player["stat_points"] += 5
        player["hp"] += 20
        player["mana"] += 10
        required = get_required_xp(player["level"])
        level_up_text += (
            f"\n\n🎉 LEVEL UP!"
            f"\nYou are now level {player['level']}"
            f"\n+5 stat points gained"
        )

    crit_text = "\n💥 CRITICAL HIT!" if crit else ""

    await update.message.reply_text(
        f"⚔ HUNT STARTED\n\n"
        f"Enemy: {monster['name']}\n"
        f"Rank: {monster['rank']}\n"
        f"Enemy HP: {monster['hp']}\n\n"
        f"You dealt {damage} damage{crit_text}\n"
        f"Enemy HP left: {max(0, monster_hp_left)}\n\n"
        f"Rewards:\n"
        f"+{gained_xp} XP\n"
        f"+{gained_gold} Gold"
        f"{level_up_text}"
    )
