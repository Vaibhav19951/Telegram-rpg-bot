
import random

def arise(rank):
    chance = 5
    if rank == "S":
        chance = 30
    return random.randint(1,100) <= chance
