# Enter your code here. Read input from STDIN. Print output to STDOUT
A =set(map(int, input().split()))
new_list = []
for i in range(int(input())):
    b = set(map(int, input().split()))
    new_list.append(b)
for ele in new_list:
    if ele.issubset(A) and ele != A:
        continue
    else:
        print(False)
        break
else:
    print(True)

# sample input
# 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
# 2
# 1 2 3 4 5
# 100 11 12