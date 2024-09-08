# -	Create a custom string class that supports operator overloading for concatenation (+ operator) and replication (* operator). Demonstrate the usage of these overloaded operators.
# 	Explanation: This task involves creating a class with customized behavior for string concatenation and replication using operator overloading.


class OperatorOne:
    def mammal_info(self):
        print("sneh"+"panara")
        
class OperatorTwo:
    def winged_animal_info(self):
        print("sneh"*4)
        
class Bat(OperatorOne,OperatorTwo):
    pass
        

b1=Bat()
b1.mammal_info()
b1.winged_animal_info()
