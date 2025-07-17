# Step 1: Ask the user to input the first number
# We're using 'float()' to make sure our numbers can have decimals too. Fancy, right? ✨
num1 = float(input("Enter the first number: "))

# Step 2: Ask the user to input the second number
num2 = float(input("Enter the second number: "))



# Add the two numbers 
sum_result = num1 + num2

# Subtract the second number from the first
difference_result = num1 - num2

# Multiply the two numbers  
product_result = num1 * num2

# Divide the first number by the second 
# We'll assume the user is being responsible and not dividing by zero for now!
quotient_result = num1 / num2

# Step 4: Show the user what we got! 🥳 Time for the big reveal! 🎉
print(f"Results of your two numbers:")
print(f"Sum: {sum_result}")  # ➕
print(f"Difference: {difference_result}")  # ➖
print(f"Product: {product_result}")  # ✖️
print(f"Quotient: {quotient_result}")  # ➗


