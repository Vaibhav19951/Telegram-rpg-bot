guilds = {}

def create_guild(name, owner):
    if name in guilds:
        return False
    guilds[name] = {"owner": owner, "members":[owner]}
    return True

def join_guild(name, member):
    if name not in guilds:
        return False
    if member not in guilds[name]['members']:
        guilds[name]['members'].append(member)
    return True
