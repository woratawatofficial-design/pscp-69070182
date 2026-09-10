"""สลากกินเเบ่งรัT"""
A = input()
B = input()
if A == B:
    print(1000000)
elif A[0] != B[0] and A[2:] == B[2:]:
    print(100000)
#กรณีตัวหน้าตรง
elif A[0] == B[0]:
    if A[4:] == B[4:]:
        print(2000)
    elif A[5:] == B[5:]:
        print(1000)
    elif A[2:] != B[2:]:
        print(20)
#ตัวหน้าไม่ตรง
elif A[0] != B[0]:
    if A[4:] == B[4:]:
        print(200)
    elif A[5:] == B[5:]:
        print(100)
    elif A[2:] != B[2:]:
        print(0)
