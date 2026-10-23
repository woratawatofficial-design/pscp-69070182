"""Paper Cut"""
def main():
    """Paper cut"""
    W,H = map(int,input().split())
    M,N = map(int,input().split())
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    X.append(W)
    Y.append(H)
    NEWX = []
    NEWY = []
    AREA = []
    prev = 0
    prevy = 0
    for i in X:
        NEWX.append(i - prev)
        prev = i
    for j in Y:
        NEWY.append(j - prevy)
        prevy = j
    for x in range(M+1):
        for y in range(N+1):
            AREA.append(NEWX[x]*NEWY[y])
    AREA.sort(reverse=True)
    print(AREA[0])
    print(AREA[1])
main()
