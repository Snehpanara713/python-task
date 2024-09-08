
# Create a dictionary of products and their prices. Write a program that asks the user for a product name and checks if it exists in the dictionary. If it does, print its price; otherwise, display an error message.

products = {
    "apple": 1.99,
    "banana": 0.99,
    "orange": 1.49,
    "grapes": 2.99,
    "watermelon": 3.99
}

pro_name=input("enter a product_name")

if pro_name in products.keys():
    print(f"The price of:",products[pro_name])
     
else:
    print("Error: Product not found.")