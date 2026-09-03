"""Password Key"""

NAME = input()

FIRST = NAME[0]
LAST = NAME[-1]
LENGTH = len(NAME)

DATA = []

# ขั้นที่ 1
for i in range(10):
    if (i + 1) % 2 != 0:
        DATA.append(ord(FIRST) + i)
    else:
        DATA.append(ord(LAST) - i)

# ขั้นที่ 2
for i in range(10):
    DATA[i] = DATA[i] % LENGTH
    DATA[i] = DATA[i] % 10

# ขั้นที่ 3 เอาตรงกลาง 6 ตัว
PASSWORD = DATA[2:8]

for x in PASSWORD:
    print(x, end="")