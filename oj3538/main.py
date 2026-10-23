"""B- Fully Pair?"""
def main():
    """She told"""
    X = input()
    checked = []
    nopair = ''
    for char in X:
        if char not in checked:
            X.count(char)
            if X.count(char) % 2 == 1:
                nopair += char
            checked.append(char)
    if nopair:
        print(nopair)
    else:
        print("fully paired")
main()
