"""Calculator V2"""
def main():
    """Calculator For You!"""
    TOTAL = 9
    X = int(input())
    if 1 < X < 10:
        print(X + X)
    elif X <= 1:
        print(X)
    else:
        START = 10
        DIGIT = 2
        while START <= X:
            END = (START*10)-1
            if END > X:
                END = X
            TOTAL += (END-START+1)*DIGIT
            DIGIT += 1
            START *= 10
        print(TOTAL+X)
main()
