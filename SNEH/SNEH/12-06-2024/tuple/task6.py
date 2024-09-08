# Create two tuples, one containing names and the other containing ages. Use the zip function to create a list of tuples where each tuple contains a name and an age.

lis1 = ['name','age']
list2 = ['sravan', 23]


data=list(zip(lis1,list2))

data2=tuple(data)

print(data2)