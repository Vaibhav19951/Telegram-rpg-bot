import random

def shadow_event(player):
    events = ["You found hidden treasure!", "A trap hurts you!", "A mysterious ally heals you."]
    event = random.choice(events)
    return event
