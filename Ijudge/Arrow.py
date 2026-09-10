"""Arrow"""
def main():
    """ARGH"""
    DIRECTION = input().upper()
    N = int(input())
    SPACE1,SPACE2 = N,N
    if DIRECTION == 'R':
        for i in range(0,N):
            print(i*2*' ' + '*'*SPACE1)
            SPACE1 -= 1
        SPACE1 += 2
        for j in range(N-2,-1,-1):
            print(j*2*' ' + '*'*SPACE1)
            SPACE1 +=1
    elif DIRECTION == 'L':
        for i in range(N-1,-1,-1):
            print(i*' ' + '*'*SPACE1)
            SPACE1 -= 1
        SPACE1 += 2
        for j in range(1,N):
            print(j*' ' + '*'*SPACE1)
            SPACE1 += 1
    elif DIRECTION == "LR":
        for i in range(N-1,-1,-1):
            print(i*' ' + '*'*SPACE1)
            SPACE1 -= 1
        SPACE1 += 2
        for j in range(1,N):
            print(j*' ' + '*'*SPACE1)
            SPACE1 += 1
        if N > 0:
            print()
        for i in range(0,N):
            print(i*2*' ' + '*'*SPACE2)
            SPACE2 -= 1
        SPACE2 += 2
        for j in range(N-2,-1,-1):
            print(j*2*' ' + '*'*SPACE2)
            SPACE2 +=1
    elif DIRECTION == "RL":
        for i in range(0,N):
            print(i*2*' ' + '*'*SPACE1)
            SPACE1 -= 1
        SPACE1 += 2
        for j in range(N-2,-1,-1):
            print(j*2*' ' + '*'*SPACE1)
            SPACE1 +=1
        if N > 0:
            print()
        for i in range(N-1,-1,-1):
            print(i*' ' + '*'*SPACE2)
            SPACE2 -= 1
        SPACE2 += 2
        for j in range(1,N):
            print(j*' ' + '*'*SPACE2)
            SPACE2 += 1
main()
