"""Che"""
LISTA = []
LISTB = []
A = int(input())
B = int(input())
for i in range(A):
    AX = int(input())
    LISTA.append(AX)
for j in range(B):
    AB = int(input())
    LISTB.append(AB)
print(*set(LISTA) - set(LISTB))
