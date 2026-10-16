"""Shorten"""
def main():
    """This function shorten the input num"""
    ALL = []
    SET = []
    while True:
        X = int(input())
        if X == -1:
            break
        ALL.append(X)
    if not ALL:
        print()
    else:
        START = ALL[0]
        for I in range(len(ALL)-1):
            if ALL[I] + 1 == ALL[I+1]:
                continue
            if START == ALL[I]:
                SET.append(str(START))
            else:
                SET.append(f"{START}-{ALL[I]}")
            START = ALL[I + 1]
        if START == ALL[-1]:
            SET.append(str(START))
        else:
            SET.append(f"{START}-{ALL[-1]}")
        print(", ".join(SET))
main()
