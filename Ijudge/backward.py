"""Backward"""
LIST = []
while True:
    X = input()
    if X == 'NULL':
        break
    LIST.append(X)
for i in LIST[::-1]:
    print(i)
