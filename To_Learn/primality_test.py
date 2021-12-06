def prime_num(n: int):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                print(f"{n} is not a prime number")
                break
        else:
            print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")


num = int(input("Enter the number for primality test or 0 to exit> "))
prime_num(num)