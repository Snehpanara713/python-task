# Implement the FizzBuzz game: Print numbers from 1 to n, but for multiples of 3, print "Fizz," for multiples of 5, print "Buzz," and for multiples of both 3 and 5, print "FizzBuzz."


def fizz_buzz(num):

    data = []

    for i in range(1, num + 1):

        if i % 3 == 0 and i % 5 == 0:

            data.append("FizzBuzz")

        elif i % 3 == 0:

            data.append("Fizz")

        elif i % 5 == 0:

            data.append("Buzz")
        else:

            data.append(str(i))

    return data


n = int(input("enter a number:"))


result = fizz_buzz(n)


print(" ".join(result))
