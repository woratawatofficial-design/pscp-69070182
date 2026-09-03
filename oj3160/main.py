"""Prime Number"""
def main():
    """โปรเเกรมหาจำนวนเฉพาะจากช่วงของ input"""
    primenumber = []
    COUNT = 0
    x,y = map(int,input().split())
    for i in range(x,y+1): #เลข x to y ye
        PRIME = True
        if i < 2:
            PRIME = False
        else:
            for j in range(2,i):
                if not i % j:
                    PRIME = False
                    break
        if PRIME:
            COUNT +=1
            primenumber.append(i)
    if COUNT:
        print(*primenumber)
    print(f"Total primes: {COUNT}")
main()
