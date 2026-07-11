"""Season ตำนวนหาฤดู"""

month = int(input())
date = int(input())

WNT = [1,2,3]
SPR = [4,5,6]
SMR = [7,8,9]
FLL = [10,11,12]

if month in WNT:
    if date >= 21 and month // 3 == 1:
        print("spring")
    else : print("winter")
elif month in SPR:
    if date >= 21 and month // 3 == 2:
        print("summer")
    else : print("spring")
elif month in SMR:
    if date >= 21 and month // 3 == 3:
        print("fall")
    else: print("summer")
elif month in FLL:
    if date >= 21 and month // 3 == 4:
        print("winter")
    else: print("fall")
#
