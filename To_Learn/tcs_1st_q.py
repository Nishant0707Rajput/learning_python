var = input()
print(var)

for i in range(len(var)):

    if ord(var[i]) >= 58:
        var = var.replace(var[i], 'x')

ans = var.split('x')
arr = []
for i in range(len(ans)):
    if (ans[i] != ''):
        arr.append(ans[i])
print(arr)
