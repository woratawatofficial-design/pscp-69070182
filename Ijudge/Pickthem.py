"""Pick them yee"""
def main():
    """This function Picks number bro"""
    X = input()
    X = X[1:-1]
    Y = X.split(',')
    RES = []
    for I in Y:
        if not int(I) % 2:
            RES.append(I)
    if not RES:
        print("Nope")
    else:
        for J in RES:
            print(int(J))
main()
