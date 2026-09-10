"""Jack"""
CARDS ={
    'A' : "ace",
    'J' : "jack",
    'Q' : "queen",
    'K' : "king",
    'D' : "diamonds",
    'H' : "hearts",
    'S' : "spades",
    'C' : "clubs"}
N = input().upper()
Y = len(N)
if Y == 2:
    if N[0] in CARDS and N[1] in CARDS:
        print(f"{CARDS[N[0]]} of {CARDS[N[1]]}")
    elif N[0] in CARDS:
        print(f"{CARDS[N[0]]} of {N[1]}")
    elif N[1] in CARDS:
        print(f"{N[0]} of {CARDS[N[1]]}")
elif Y == 1:
    if N[0] in CARDS:
        print(CARDS[N])
    else:
        print(N)
elif Y == 3:
    if N[0] in CARDS and N[1]:
        print(f"{CARDS[N[0]]} of {N[1]}{N[2]}")
    if N[2] in CARDS:
        print(f"{N[0]}{N[1]} of {CARDS[N[2]]}")
