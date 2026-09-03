"""isprimenumbeer"""
x,y = map(int,input().split())
PRIME = []
COUNT = 0
for number in range(x,y+1): #เลขในช่วงinput
    prime = True
    if number < 2:
        prime = False
    else:
        for i in range(2,number-1): #เอามาหาร 2ถึงก่อนnumber เพราะมีเเค่ 1เเละตัมัรเองที่หารลงตัว
            if not number % i:
                prime = False
                break
    if prime:
        PRIME.append(number)
        COUNT +=1
if COUNT:
    print(*PRIME)
print(f"Total primes: {COUNT}")
