"""Flower"""
def main():
    """This function finds an area to plant a flower"""
    L,N = map(int,input().split())
    STEP = 1
    COUNT = L * (L+ 1) // 2
    while N > COUNT:
        N -= COUNT
        STEP += 1
        COUNT += L**2
    print(STEP)
main()
