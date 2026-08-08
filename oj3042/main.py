"""โปรเเกรมคำนวณเลขหาร 10"""
X = int(input())
while X >= 0:
    if not X % 10:
        print(X,end = " ")
        X -= 10

    elif X % 10:
        X -= (X%10)
        print(X, end = " ")
        X -= 10

    elif not X:
        break
