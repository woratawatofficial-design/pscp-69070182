"""ThaiPlus"""
NAME = str(input())
AGE = int(input())
INCOME = int(input())
STATUS = str(input())
FAMILY = int(input())
THAIPLUS = True
RANK = ''
money = 0
if AGE < 18:
    THAIPLUS = False
if STATUS == 'Y':
    RANK = 'GOLD'
elif INCOME <= 15000:
    RANK = 'GOLD'
elif 15000 < INCOME <= 30000:
    RANK = 'SILVER'
if RANK == 'GOLD':
    money += 3000
    if FAMILY >= 3:
        money += 500
elif RANK == 'SILVER':
    money += 1500
    if FAMILY >= 3:
        money += 500
else: THAIPLUS = False
if THAIPLUS:
    print(f"{NAME} {RANK} {money}")
elif THAIPLUS is False:
    print(f"{NAME} NOT ELIGIBLE")
