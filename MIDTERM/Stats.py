"""STats"""
X = int(input())
MAX = None
MIN = None
AVG = 0
for i in range(X):
    N = int(input())
    if not i:
        MAX = N
        MIN = N
    else:
        if N > MAX:
            MAX = N
        elif N < MIN:
            MIN = N
    AVG += N
print(f"MIN: {MIN:.3f}")
print(f"MAX: {MAX:.3f}")
print(f"AVG: {AVG/X:.3f}")
