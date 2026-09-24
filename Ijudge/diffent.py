"""Diff"""
def main():
    """This funcion finds the different number from each set"""
    SETA = set()
    SETB = set()
    A = int(input())
    B = int(input())
    for _ in range(A):
        AX = int(input())
        SETA.add(AX)
    for _ in range(B):
        AB = int(input())
        SETB.add(AB)
    print(*sorted(SETA - SETB))
main()
