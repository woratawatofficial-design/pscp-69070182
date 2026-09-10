"""Teaching Schedule"""
N = int(input()) #คาบ
A = int(input()) #นาที
HOUR = (N*A)//60
MINUTE = (N*A)%60
if not N or not A:
    print("No teaching")
else:
    if not HOUR:
        print(f"{MINUTE} minute")
    elif not MINUTE:
        print(f"{HOUR} hours")
    else:
        print(f"{HOUR} hours {MINUTE} minute")
