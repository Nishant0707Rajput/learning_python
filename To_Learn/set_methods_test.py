# Enter your code here. Read input from STDIN. Print output to STDOUT
N_A = int(input())
A = set(map(int, input().split()[:N_A]))
for i in range(int(input())):
    ele = input()
    M  = int(ele[-2:])

    op_set = set(map(int, input().split()))
    if "intersection" in ele:
        A.intersection_update(op_set)
    elif ele[:7] == "update":
        A.update(op_set)
    elif "symmetric" in ele:
        A.symmetric_difference_update(op_set)
    else:
        A.difference_update(op_set)
print(sum(A))

