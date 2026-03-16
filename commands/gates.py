async def gates(update, context):
    gates_data = context.bot_data.get("gates", [
        {"rank": "B", "location": "Seoul", "time_left": "20 min"},
        {"rank": "A", "location": "Tokyo", "time_left": "12 min"},
    ])

    lines = ["🚪 ACTIVE GATES\n"]
    for gate in gates_data:
        lines.append(
            f"{gate['rank']} Rank Gate - {gate['location']} - Time left: {gate['time_left']}"
        )

    await update.message.reply_text("\n".join(lines))
