"""Median"""
def main():
    """This function finds a median from one row input"""
    MED = 0
    X = input()
    X = X.replace(', ',' ')
    X = X.split()
    X = list(map(float,X))
    X.sort()
    I = len(X) // 2
    if not len(X) % 2:
        MED = (X[I-1] + X[I])/2
    else:
        MED = X[I]
    print(f"{MED:.2f}")
main()
