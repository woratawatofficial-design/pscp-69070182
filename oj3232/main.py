"""โปรเเกรมคำนวณก้าวที่กบต้องใช้ในการกระโดด"""
X,Y = map(int,input().split())
TOTAL = 0
COUNT = 0
while X > 0:
    TOTAL += X
    X -= 2
    COUNT += 1
    if TOTAL >= Y:
        print(COUNT)
        break
if TOTAL < Y:
    print(-1)
