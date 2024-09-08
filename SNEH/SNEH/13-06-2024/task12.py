class Calculate:
    def calculate_data(self):
        pass


class Sum(Calculate):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_data(self):
        return self.x + self.y
    
    
class Multiplication(Calculate):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_data(self):
        return self.x * self.y
    
    
class Substraction(Calculate):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_data(self):
        return self.x - self.y
    
    
class Devide(Calculate):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_data(self):
        return self.x/self.y
    
    

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))




# x=10
# y=20



# x=20
# y=10




# x=20
# y=5





print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")


select = int(input("Select operations form 1, 2, 3, 4 :"))


if select==1:
    
    sum=Sum(number_1,number_2)
    data_calculate=sum.calculate_data()
    print(data_calculate)
    

elif select==2:
    multi=Substraction(number_1,number_2)
    data_calculate=multi.calculate_data()
    print(data_calculate)
    
    
elif select==3:
    multi=Multiplication(number_1,number_2)
    data_calculate=multi.calculate_data()
    print(data_calculate)
    
    
    
elif select==4:
    multi=Devide(number_1,number_2)
    data_calculate=multi.calculate_data()
    print(data_calculate)

else:
   print("Invalid input")