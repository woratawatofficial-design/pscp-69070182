"""Electric"""
def main():
    """this function calculates the price of electricity bill"""
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
            elif 11 <= i <= 50:
                PRICE += 7
            elif 51 <= i <= 100:
                PRICE += 10
            elif 101 <= i <= 200:
                PRICE += 12
            elif i >= 201:
                PRICE += 15
        TOTAL = PRICE+(VAT*PRICE)+FT
        print(f"{TOTAL:.1f}")
main()
