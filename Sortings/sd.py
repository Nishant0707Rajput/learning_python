def counttriplets(low,high):
    c, m = 0, 2


    count = 0
    while c < high :

        # Now loop on n from 1 to m-1
        for n in range(low, high) :
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            # if c is greater than
            # limit then break it
            if c > high :
                break
            count += 1


        c = c + 1
    return count

print(counttriplets(1,6))