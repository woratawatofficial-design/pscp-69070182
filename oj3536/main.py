"""Prime Number"""
def main():
    """โปรเเกรมหาจำนวนเฉพาะจากช่วงของ input"""
    X = int(input())
    if X < 2:
        PRIME = False
    else:
        PRIME = True
    for i in range(2,(int(X**0.5)+1)):
        if not X % i:
            PRIME = False
            break
    if PRIME:
        print('YES')
    else:
        print('NO')
main()
