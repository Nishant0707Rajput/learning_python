def solve(s, d, h, n):
    if n == 1:
        print(f"{s} to {d}")
        return
    solve(s, h, d, n-1)
    print(f"{s} to {d}")
    solve(h, d, s, n-1)


solve(1, 2, 3, 4)
