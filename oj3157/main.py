"""สะสมเเต้ม"""
N = int(input())
TOTAL = 0
for I in range(N):
    I = input()
    if I == "+":
        TOTAL += 10
    elif I == "-":
        TOTAL -= 5
print(TOTAL)
