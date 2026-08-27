"""โปรเเกรมคำนวณหาอิฐที่ต้องใช้"""
A = int(input())
B = int(input())
GOAL = int(input())
NEEDB = GOAL // 5
NEEDA = 0
if NEEDB <= B:
    GOAL -= NEEDB*5
elif NEEDB > B:
    GOAL -= B*5
if GOAL <= A:
    NEEDA = GOAL // 1
    print(NEEDA)
elif GOAL > A:
    print(-1)
