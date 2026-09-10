"""Left Arrow"""
N = int(input())
K = int(input())
new_stair = K//2
for i in range(new_stair,0,-1):
    print(' '*i + '*'*N)
print('*'*N)
for j in range(1,new_stair+1):
    print(' '*j + '*'*N)
