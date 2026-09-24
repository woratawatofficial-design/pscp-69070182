"""box"""
W,L,M,N = map(int,input().split())
LOWEST = []
for i in range(M,N+1):
    LOWEST.append((W%i)*(L%i))
print(min(LOWEST))
