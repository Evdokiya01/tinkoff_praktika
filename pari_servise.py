pari_map = {}


def add_pari(user_id, pari):
    if user_id not in pari_map.keys():
        pari_map[user_id] = [pari]
    else:
        pari_map[user_id].append(pari)


def get_pari(user_id):
    if user_id not in pari_map.keys():
        return []
    return pari_map[user_id]