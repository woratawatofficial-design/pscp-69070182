"""Electric"""
def main():
    """this function calculates the price of electricity bill"""
    current = float(input())
    FT = 0.5*current
    PRICE = 0
    if 1 <= current <= 10:
        PRICE += current*5
    elif 11 <= current <= 50:
        PRICE += (current-10)*7 + 50
    elif 51 <= current <= 100:
        PRICE += (current - 50)*10 + 50 + 280
    elif 101 <= current <= 200:
        PRICE += (current - 100)*12 + 50 + 280 + 500
    elif current >= 201:
        PRICE += (current - 200)*15 + 50 + 280 + 500 + 1200
    TOTAL = PRICE*1.07 + FT
    print(f"{TOTAL:.1f}")
main()
