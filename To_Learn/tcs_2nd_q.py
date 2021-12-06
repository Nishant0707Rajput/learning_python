n = int(input())
new_list = [[x, y, z] for x in range(1, n) for y in range(1, n) for z in range(1, n) if (x != y or y != z) and x+y+z == n]
print(sorted(new_list))
print(len(new_list))