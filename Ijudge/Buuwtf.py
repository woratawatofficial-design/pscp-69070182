"""BUuu"""
X = input().upper()
count = 0
count_1 = 0
max_u = 0
if 'BUU' in X:
    for i in X:
        if i == 'U':
            count += 1
        else:
            count = 0
        count_1 = max(count_1,count)
    print(f'Yes {count_1}')
            

for i in range(len(X)):
    if X[i] == 'B':
        count = 0
        j = i + 1
        while j < len(X) and X[j] == 'U':
            count += 1
            j += 1
        if count > max_u:
            max_u = count
print(max_u)