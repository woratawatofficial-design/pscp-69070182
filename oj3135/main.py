"""Theif"""
def main():
    """Who is the thief"""
    N,K,T = map(int,input().split()) #มี N คน ส่ง K ครั้ง Kจุด T คือโจร
    status = 1
    DONE = [1]
    if T == 1:
        print(1)
    else:
        while True:
            status += K
            if status > N:
                status -= N
            if status == 1:
                break
            DONE.append(status)
            if status == T:
                break
        print(len(DONE))
main()
