"""Ramen"""
def main():
    """Ramen Bowl"""
    N = int(input())
    HAVE = []
    COUNT = []
    for _ in range(N):
        size = int(input())
        HAVE.append(size)
    for i in set(HAVE):
        COUNT.append(HAVE.count(i))
    print(max(COUNT))
main()
