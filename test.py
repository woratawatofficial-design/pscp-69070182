"""Airport"""
import math
park = float(input())
leave = float(input())
TOTAL = round(leave - park,2)
MINUTE = round(TOTAL - int(TOTAL),2)
HOUR = int(TOTAL - MINUTE)
PRICE = {
        1:25,
        2:50,
        3:80,
        4:110,
        5:145,
        6:180
        }
if not HOUR and MINUTE <= 0.25:
    print("FREE")
else:
    HOUR = math.ceil(HOUR + MINUTE)
    if  24 >= HOUR >= 7:
        print(250)
    elif 0 < HOUR <=6:
        print(PRICE[HOUR])
    else:
        print("ERROR")
