# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
N = int(input())
new_dict = OrderedDict()
for i in range(N):
    b_inp = input()
    new_list = [int(i) for i in b_inp.split() if i.isdigit() ]
    if str(b_inp[:-2]).strip() not in new_dict:
        new_dict[str(b_inp[:-2]).strip()] = new_list[0]
    else:
        new_dict[str(b_inp[:-2]).strip()] += new_list[0]
# print(new_dict)
for i, j in new_dict.items():
    print(i, j)
new_list = ["base","dom"]

print(*new_list)
print(hex(165))
# n = int(input())
# new_list = [[x, y, z] for x in range(1, n) for y in range(1, n) for z in range(1, n) if (x != y or y != z) and x+y+z == n]
# print(new_list)
# print(len(new_list))