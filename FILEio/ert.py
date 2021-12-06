val = list(input())
n = len(val)
count = 0
for j in range(n-1):
    if ord(val[j]) > ord(val[j+1]):
        count += 1

print(count)
