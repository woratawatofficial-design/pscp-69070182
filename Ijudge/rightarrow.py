"""Right Arrow"""
N = int(input())
K = int(input())
new_stair = K//2
for i in range(0,new_stair):
    print(" "*i + "*"*N)
for j in range(new_stair,-1,-1):
    print(" "*j + "*"*N)
