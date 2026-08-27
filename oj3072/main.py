"""โปรเเกรมหา Vowels ใน Input"""
X = input().lower()
count_A = 0
count_E = 0
count_I = 0
count_O = 0
count_U = 0
for i in X:
    if i in "a":
        count_A += 1
    if i in "e":
        count_E += 1
    if i in "i":
        count_I += 1
    if i in "o":
        count_O += 1
    if i in "u":
        count_U += 1
if count_A > 0:
    print(f"a : {count_A}")
if count_E > 0:
    print(f"e : {count_E}")
if count_I > 0:
    print(f"i : {count_I}")
if count_O > 0:
    print(f"o : {count_O}")
if count_U > 0:
    print(f"u : {count_U}")
    