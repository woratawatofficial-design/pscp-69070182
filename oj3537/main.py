"""Imposter"""
import json
def main():
    """Well Well Well"""
    imposter_count = 0
    DATA = {}
    DEAD = []
    X = input()
    while X != 'Start':
        DATA.update(json.loads(X))
        X = input()
    X = input()
    while X != 'End':
        DEAD.append(X)
        X = input()
    ALIVE = list(set(DATA) - set(DEAD))
    ALIVE.sort()
    DEAD.sort()
    for name in ALIVE:
        if DATA[name] == 'Impostor':
            imposter_count += 1
    print(f"{imposter_count} Impostor Remains")

    print('***Alive***')
    for name1 in ALIVE:
        print(f"{name1} : {DATA[name1]}")

    print('***Dead***')
    for name2 in DEAD:
        print(f"{name2} : {DATA[name2]}")
main()
