# Write a function to generate the first n Fibonacci numbers.


def fibonacci(n_terms):

    n_1 = 0
    n_2 = 1
    count = 0

    if n_terms <= 0:
        print("Please enter a positive integer, the given number is not valid")

    elif n_terms == 1:
        print(
            "The Fibonacci sequence of the numbers up to",
            n_terms,
            ":",
        )
        print(n_1)

    else:
        print("The fibonacci sequence of the numbers is:")
        while count < n_terms:
            print(n_1)
            nth = n_1 + n_2

            n_1 = n_2
            n_2 = nth
            count += 1


while True:
    try:
        n_terms = int(input("How many terms to print?:-"))

        if n_terms > 0:
            break
        else:
            print("Enter a positive number")

    except ValueError:
        print("Invalid input. Please enter a number.")

fibonacci(n_terms)
