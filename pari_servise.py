from pari import Pari, PariState

pari_map = {}


def add_pari(user_login, pari_name):
    pari = Pari(pari_name=pari_name,
                description="descriptions",
                challenger_login=user_login,
                state=PariState.NEW)
    if user_login not in pari_map.keys():
        pari_map[user_login] = [pari]
    else:
        pari_map[user_login].append(pari)


def get_pari(user_login):
    if user_login not in pari_map.keys():
        return []
    return pari_map[user_login]