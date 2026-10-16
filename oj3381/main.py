"""Dot Product"""
def main():
    """This func"""
    AMNT = int(input())

    for _ in range(AMNT):
        PTS = []

        POINT = int(input())

        for _ in range(POINT):
            X, Y = map(int, input().split())
            PTS.append((X, Y))

        PTS.sort(key=lambda p: (p[0] + p[1], -p[1]))

        for X, Y in PTS:
            print(X, Y)

main()
