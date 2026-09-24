"""ไหนว่าใช้ C++"""
def main():
    """THis function converts to rgb number into the new one"""
    x1,y1,z1 = map(int,input().split())
    x2,y2,z2 = map(int,input().split())
    newx = (x1+x2)//2
    newy = (y1+y2)//2
    newz = (z1+z2)//2
    print(newx,newy,newz)
main()
