"""CASTLE"""
import math
X = int(input())
FLOOR = math.ceil(math.sqrt(X))
COLUMN = 0
if not FLOOR % 2:
    if not X % 2:
        COLUMN = (FLOOR - 1)*2
    elif X % 2:
        COLUMN = ((FLOOR - 1)*2) - 1
elif FLOOR % 2:
    if not X % 2:
        COLUMN = ((FLOOR - 1)*2) - 1
    elif X % 2:
        COLUMN = (FLOOR - 1)*2
print(COLUMN)
