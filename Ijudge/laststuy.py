"""LastStand"""
def main():
    """This function gives an output of the last digit number in every num"""
    X = input()
    X = X[1:-1]
    Y = X.split(',')
    for i in Y:
        print(i[-1])
main()
