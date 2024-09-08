# Create a function that takes three arguments (name, age, city) and returns them as a tuple. Then, call the function and unpack the tuple into separate variables.

def information(name, age, city):
    return name,age,city

# x=information("raj","23","surendranagar")
# print(x)


(name,age,city)=information("raj","23","surendranagar")
print(name,"name")
print(age,"age")
print(city,"city")