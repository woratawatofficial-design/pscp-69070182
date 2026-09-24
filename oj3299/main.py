"""Flower"""
def main():
    """THis function finds a field where the flower belongs to"""
    L,N = map(int,input().split())
    AREA = L*(L+1)//2
    count = 1
    while N > AREA:
        count += 1
        N -= AREA
        AREA += L**2
    print(count)
main()
