#Take customer's name
customer_name = input("Enter customer name: ")
#Name of the three products with their prices as input
product1_name = input("Enter the name of product 1: ")  
product1_price = float(input("Enter the price of product 1: "))
product2_name = input("Enter the name of product 2: ")
product2_price = float(input("Enter the price of product 2: "))
product3_name = input("Enter the name of product 3: ")
product3_price = float(input("Enter the price of product 3: "))

#Calculate total price
total_price = product1_price + product2_price + product3_price


# Discount calculation
if total_price >=5000:
    discount = total_price * 0.20
elif total_price >= 3000:
    discount = total_price * 0.10
elif total_price >= 1000:
    discount = total_price * 0.05
    total_price -= discount
else:
    discount = 0
    #print(f"\nYou have received a 5% discount of {discount:.2f}!")
final_price = total_price - discount
#Display the result
print(f"\n--- Shopping Cart for {customer_name} ---")
print(f"Product 1: {product1_name}")
print(f"Price: {product1_price:.2f}")
print(f"Product 2: {product2_name}")
print(f"Price: {product2_price:.2f}")
print(f"Product 3: {product3_name}")
print(f"Price: {product3_price:.2f}")
print(f"Sub-total Price: {total_price:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final Price: {final_price:.2f}")