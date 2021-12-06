n = 4
new_list = [""] * n
top = -1


def my_push(val):
    global top
    if top >= n-1:
        print("can't add Stack is full")
        return
    else:
        top += 1
        new_list[top] = val


def my_pop():
    global top
    if top == -1:
        print("stack is empty")
    else:
        val = new_list[top]
        new_list[top] = ""
        top -= 1
        return val


def peak():
    return new_list[top]


print(peak())
print()
for i in range(n):
    my_push(i)
    print(peak(),new_list)
print()
for i in range(n):
    print(my_pop(), new_list)
# N = 3
# M = 3
# N_list = [1,2,3]
# M_list = [5,6,7]
# # for i in range(N):
# #     N_list.append(int(input()))
# #
# # for j in range(M):
# #     M_list.append(int(input()))
#
# val = [[x,y] for x in N_list for y in M_list if (x*y)%2==0]
#
# print(val)