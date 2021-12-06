def print_rangoli(size):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    new_list = list(range(size+1))
    for j in range(0, 2*size-1):
        if j < size:
            print(alphabets[size-new_list[j]], end="-")
        else:
             print(alphabets[new_list[j-2]], end="-")


        # print()
        #
        # if j < 5:
        #     print(alphabets[size-1-j])
#         else:
#             print(alphabets[j-size+1].center(4*size-3, "-"))
#
#
# if __name__ == '__main__':
n = int(input())
print_rangoli(n)