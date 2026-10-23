"""Coke"""
def main():
    """THis function calculates the total price of cokes"""
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    PRICE = 0
    if not B or not D:
        PRICE = A*D
    else:
        PRO = (D-1) // B
        NPRO = D - PRO
        PRICE = PRO*C + NPRO*A
    print(PRICE)
main()
