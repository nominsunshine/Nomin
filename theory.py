class GCDCalculator:
    def __init__(self):
# Initialize numbers to None because it will be updated by user input
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
        if self.a == 0 and self.b == 0:
            print("Error: Both numbers cannot be zero.")
            return False
        if self.a < 0 or self.b < 0:
            print("Error: Numbers must be positive.")
            return False
        return True

    def calculate_gcd(self):
# Use the Euclidean algorithm to find the GCD
        a, b = self.a, self.b  # Simultaneous assignment
        while b != 0:  # Iterate until b=0
            remainder = a % b
            print(f"{a} = {b} * ({a // b}) + {remainder}")  # Display the division step
            a, b = b, remainder  # Update values
        return a  # The last `a` is the GCD

    def relative_primes(self):
        # Check if two numbers are relative primes
        return self.calculate_gcd() == 1

    def run(self):
        # Main program workflow
        self.get_inputs()  # Get numbers
        if self.validate_numbers():  # Check if inputs are valid
            gcd = self.calculate_gcd()  # Calculate GCD
            if self.relative_primes():  # Check if the numbers are relative primes
                print(f"{self.a} and {self.b} are relative prime numbers.")
            print(f"The GCD of {self.a} and {self.b} is {gcd}.")
        else:
            print("Invalid input. Please restart the program.")  # Handle invalid input


# Run the program
if __name__ == "__main__":
    gcd_calculator = GCDCalculator()
    gcd_calculator.run()