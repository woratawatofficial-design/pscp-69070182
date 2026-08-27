"""คำนวณราคาสมาชิก"""
import math
MEMBER = input()
QTT = int(input())
TOTAL = 0
for _ in range(QTT):
    BUY = float(input())
    TOTAL += BUY
if MEMBER == "Y":
    TOTAL -= TOTAL*0.05
elif MEMBER == "N" and TOTAL >= 500:
    TOTAL -= TOTAL*0.03
X = math.ceil(TOTAL*100)/100
print(f"{X:.2f}")
