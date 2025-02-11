class GCDCalculator:
    def __init__(self):
# Initialise numbers to None because it will be updated by user inputs
        self.a = None
        self.b = None

    def get_inputs(self):
# Ask the user for two numbers
        while True:
            try:
                self.a = int(input("Enter the first number: "))
                self.b = int(input("Enter the second number: "))
 # Exit if input is valid
                break
            except ValueError:
# Handle non-integer input
                print("Invalid input. Please enter whole numbers only.")

    def validate_numbers(self):
 # Check if the inputs are valid
        if self.a == 0 or self.b == 0:
            print("Error: Neither number can be zero.")
            return False
        if self.a < 0 or self.b < 0:
            print("Error: Numbers must be positive.")
            return False
        return True

    def calculate_gcd(self):
# Use the Euclidean algorithm to find the GCD
# Simultaneous assignment
        a, b = self.a, self.b  
# Iterate until b=0
        while b != 0:  
            remainder = a % b
            print(f"{a} = {b} * ({a // b}) + {remainder}")  # Display the division step
# Update values
            a, b = b, remainder  
        return a  # The last `a` is the GCD

    def relative_primes(self):
# Check if two numbers are relative primes
        return self.calculate_gcd() == 1

    def calculate_lcm(self, gcd):
# Calculate the LCM using the GCD
# abs() for returning positive values
        return abs(self.a * self.b) // gcd 

    def run(self):
 # Main program workflow
        self.get_inputs()  # Get numbers
        if self.validate_numbers():  # Check if inputs are valid
            gcd = self.calculate_gcd()  # Calculate GCD
            lcm = self.calculate_lcm(gcd)  # Calculate LCM using the GCD
            if gcd == 1:  # Check if the numbers are relative primes
                print(f"{self.a} and {self.b} are relative prime numbers.")
            print(f"The GCD of {self.a} and {self.b} is {gcd}.")
            print(f"The LCM of {self.a} and {self.b} is {lcm}.")
        else:
            print("Invalid input. Please restart the program.")  # Handle invalid input


# Run the program
if __name__ == "__main__":
    gcd_calculator = GCDCalculator()
    gcd_calculator.run()