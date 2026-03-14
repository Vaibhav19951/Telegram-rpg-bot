
inventories = {}

def add_item(player,item):
    inventories.setdefault(player,[]).append(item)
