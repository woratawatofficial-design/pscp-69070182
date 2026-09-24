"""Arrow"""
DIRECTION = input().upper()
N = int(input())
def right():
    """This fuction gives the result of right arrow"""
    SPACE1 = N
    for i in range(0,N):
        print(i*2*' ' + '*'*SPACE1)
        SPACE1 -= 1
    SPACE1 += 2
    for j in range(N-2,-1,-1):
        print(j*2*' ' + '*'*SPACE1)
        SPACE1 +=1
def left():
    """This function gives the result of left arrow"""
    SPACE1 = N
    for i in range(N-1,-1,-1):
        print(i*' ' + '*'*SPACE1)
        SPACE1 -= 1
    SPACE1 += 2
    for j in range(1,N):
        print(j*' ' + '*'*SPACE1)
        SPACE1 += 1
if DIRECTION == "R":
    right()
elif DIRECTION == 'L':
    left()
elif len(DIRECTION) >= 2:
    for k in DIRECTION:
        if k == 'R':
            right()
            print('')
        elif k == 'L':
            left()
            print('')
