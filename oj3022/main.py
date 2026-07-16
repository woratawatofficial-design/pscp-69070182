"""เเปลงค่าอุณหภูมิ ยากโคตรเลยพี่"""
T = float(input())
TN = input().lower()
TN2 = input().lower()
C = 0
ANS2 = 0

#เเปลงทั้งหมดเป็น C
if TN == "c":
    C = T
elif TN == "k":
    C = T - 273.15
elif TN == "f":
    C = (T - 32)*(5/9)
elif TN == "r":
    C = (T*(5/9)) - 273.15
#เอาค่า C มาคิดต่อ
if TN2 == "c":
    ANS2 = C
elif TN2 == "k":
    ANS2 = C + 273.15
elif TN2 == "f":
    ANS2 = (C*(9/5)) + 32
elif TN2 == "r":
    ANS2 = (C + 273.15)*(9/5)
print(f"{ANS2:.2f}")
