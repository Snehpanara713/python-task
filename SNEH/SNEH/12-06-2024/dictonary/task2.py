# Given a list of names, create a dictionary where the keys are the names, and the values are the lengths of the names, using a dictionary comprehension.

names = ["Alice", "Bob", "Charlie", "David"]


name_legnth={name:len(name) for name in names}
print(name_legnth)