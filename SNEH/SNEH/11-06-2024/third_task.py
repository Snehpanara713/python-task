# # Write a function to check if a number is prime.


def prime_not_prime(num):
    if num > 1:
        for i in range(2, (num // 2) + 1):

            if (num % i) == 0:
                print(num, "is not a prime number")
                break

            else:
                print(num, "is a prime")

    else:
        print(num, "is not a prime number")


num = int(input("enter a number:"))
prime_not_prime(num)
