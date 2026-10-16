"""Duplicate I OJ3386"""
def main():
    """This function finds the imposter"""
    LX = []
    LY = []
    SAME = []
    X = int(input())
    Y = int(input())
    for _ in range(X):
        CX = int(input())
        LX.append(CX)
    for _ in range(Y):
        CY = int(input())
        LY.append(CY)
    for I in LX:
        if I in LY:
            SAME.append(I)
    if not SAME:
        print('Nope')
    else:
        SAME.sort(reverse=True)
        for J in SAME:
            print(J)
main()
