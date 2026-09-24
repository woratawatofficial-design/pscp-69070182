"""Ticket Cinema"""
def main():
    """This function calculates the price of 
    the ticket depends 
    on your age and the capacity of the seats"""
    TOTAL = int(input())
    PRICE = 0
    while TOTAL > 0:
        AGE,BUY = map(int,input().split())
        if AGE < 15:
            print(-1)
        else:
            if BUY > TOTAL:
                print(-2)
            else:
                TOTAL -= BUY
                if 15 <= AGE <= 22:
                    PRICE = 120
                elif AGE >= 60:
                    PRICE = 75
                else:
                    PRICE = 150
                print(f"{PRICE*BUY} {TOTAL}")
main()
