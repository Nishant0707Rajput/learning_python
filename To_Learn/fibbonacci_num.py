# def fibbonacci_num(n: int):
#     next_num = 0
#     num1, num2 = 0, 1
#     for j in range(n):
#         next_num = num2 + num1
#         num1 = num2
#         num2 = next_num
#     return next_num
#
#
# num = int(input("Enter the number up to which fibonacci is to be printed > "))
# for i in range(num):
#     print(i+1, fibbonacci_num(i))
def fibonacci(n):
    new_list = [0]

    num1, num2 = 0, 1
    for i in range(n-1):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        new_list.append(num1)
    return new_list


print(fibonacci(5))
