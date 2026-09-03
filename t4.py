"""Prime"""
X,Y = map(int,input().split())
COUNT = 0
P = []
for i in range(X,Y+1): #เลข
    PRIME = True
    if i < 2:
        PRIME = False
    else:
        for j in range(2,i):
            if not i % j:
                PRIME = False
                break

    if PRIME is True:
        COUNT += 1
        P.append(i)
if COUNT:
    print(*P)
    print(f"Total primes: {COUNT}")
