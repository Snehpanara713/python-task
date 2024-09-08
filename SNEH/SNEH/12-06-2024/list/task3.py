# Create a list of numbers from 1 to 10 and then use a list comprehension to create a new list containing the squares of these numbers.

number=[1,2,3,4,5,6,7,8,9,10]

square=[num**2 for num in number]

print(square)