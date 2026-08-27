"""[LEARNING LOGS] จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""
A = int(input())
B = int(input())
d = int(input())
r = int(input())
total = 0
if B > A and  r < d:
    for i in range(A,B+1):
        if i % d == r:
            total += 1
print(total)
