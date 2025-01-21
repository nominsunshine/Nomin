def common_divisor(a, b):
# Continue until b becomes 0
    while b != 0:  
# Find how many times b fits into a
        quotient = a // b 
# Calculate the remainder
        remainder = a % b  
# Display the division step
        print(f"{a} = {b} * {quotient} + {remainder}")  
# Update a to b, and b to the remainder
        a, b = b, remainder  
# When b becomes 0, a is the GCD
    return a  

