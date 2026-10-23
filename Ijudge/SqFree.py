"""SqFree"""
def main():
    """This function calculates your SqFree from input"""
    HAVE = []
    POWER = []
    N = int(input())
    for i in range(1,N+1):
        HAVE.append(i)
        for j in range(2,N+1):
            if j**2 > i:
                break
            if not i % j**2:
                POWER.append(i)
    print(set(HAVE)-set(POWER))
    print(len(HAVE)-len(list(set(POWER))))
main()
