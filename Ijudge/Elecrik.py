"""Electric"""
def main():
    """this function calculates the price of electricity bill"""
    import math
    current = int(input())
    FT = 0.5*current
    VAT = 0.07
    PRICE = 0
    if current <= 0:
        print(0.0)
    else:
        for i in range(1,current+1):
            if i <= 10:
                PRICE += 5
            elif i <= 50:
                PRICE += 7
            elif i <= 100:
                PRICE += 10
            elif i <= 200:
                PRICE += 12
            else:
                PRICE += 15
        TOTAL = PRICE+(VAT*PRICE)+FT
        print(f"{TOTAL:.1f}")
main()
