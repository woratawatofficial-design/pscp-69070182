"""โคตรเกลียด"""
def main():
    """This function converts your goofy string into even number"""
    X = input()
    L = []
    X = X[1:-1]
    print(X)
    Y = X.split(',')
    print(Y)
    for i in Y:
        L.append(int(i))
    print(L)
main()