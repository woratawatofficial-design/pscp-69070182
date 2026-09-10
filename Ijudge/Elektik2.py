"""Electric"""
def main():
    """this function calculates the price of electric use"""
    current = int(input())
    FT = 0.5*current
    VAT = 0.07*current
    PRICE = 0
    if not current:
        print(PRICE)
    else:
        for i in range(1,current+1):
            if i in range(1,11):
                PRICE += 5
            elif i in range(11,51):
                PRICE += 7
            elif i in range(51,101):
                PRICE += 10
            elif i in range(101,201):
                PRICE += 12
            elif i >= 201:
                PRICE += 15
        print(PRICE)
main()