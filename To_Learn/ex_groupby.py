from itertools import combinations
# # value = list(input())
# # a_list = [list(b) for a, b in groupby(value, int)]
# # # print(a_list)
# # for ele in a_list:
# #     print((len(ele), ele[0]), end=" ")
# #
# print(*itertools.combinations(range(1, 5), 2))
# m = list(input().split())
# print(m)
N = 4
a_list = list("a a b c".split()[:N])
M = 2
another_list = []
count = 0
count_2 =0
b_list =[]
for ele in range(len(a_list)):
    if a_list[ele] == "a":
        another_list.append(ele + 1)
# print(another_list)
for a,b in combinations(range(1, N+1), M):
    count += 1
    print(a,b)
    if a and b not in another_list:
        count_2 += 1
    # print(x)

print(count,count_2)
print(f"{count_2/count:.3f}")

