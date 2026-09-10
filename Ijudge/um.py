K = int(input())  # width
N = int(input())  # height

new_stair = N//2

print("*"*K)

for i in range(1, new_stair):
    print(" "*i + "*"*K)

print(" "*new_stair + "*"*K)

for j in range(new_stair-1, 0, -1):
    print(" "*j + "*"*K)

print("*"*K)