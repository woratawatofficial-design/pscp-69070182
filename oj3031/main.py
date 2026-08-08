"""INK"""
import math
S,PEOPLECRY = map(int,input().split())
for i in range(PEOPLECRY):
    X,Y = map(int,input().split())
    AREA = 3.1416 * (X**2 + Y**2)
    i = math.ceil(AREA/S)
    print(i)
