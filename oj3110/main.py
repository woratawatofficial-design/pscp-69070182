"""โปรเเกรมคำนวณราคาค่าส่งพัสดุ ต้นทางเเละปลายทาง"""
L1,L2 = map(str,input().upper().split())
S = float(input())
if L1 == "BKK":
    if L2 == "CNX":
        print(f"{(10 + 30*S):.2f}")
    elif L2 == "PKT":
        print(f"{(25 + 50*S):.2f}")
    else: print("Error")
elif L1 == "UBP":
    if L2 == "BKK":
        print(f"{(20 + 40*S):.2f}")
    elif L2 == "PKT":
        print(f"{(40 + 70*S):.2f}")
    else: print("Error")
elif L1 == "CNX" and L2 == "UBP":
    print(f"{(15 + 40*S):.2f}")
elif L1 == "PKT" and L2 == "CNX":
    print(f"{(30 + 60*S):.2f}")
else: print("Error")
#
