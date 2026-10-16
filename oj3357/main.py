"""Giraffe"""
def main():
    """Giraffe"""
    X = int(input())
    COUNT = 0
    ALL = []
    for _ in range(X):
        HEIGHT = int(input())
        ALL.append(HEIGHT)
    if len(ALL) == 1:
        print(1)
    else:
        if ALL[0] > ALL[1]:
            COUNT += 1
        if ALL[-1] > ALL[-2]:
            COUNT +=1
        for i in range(1,X-1):
            if ALL[i] > ALL[i-1] and ALL[i] > ALL[i+1]:
                COUNT += 1
        print(COUNT)
main()
