"""
Shipping Cost Calculator
=======================

This program calculates shipping costs based on package weight and rate per kilogram.
"""

def get_valid_input(prompt: str) -> float:
    """Get and validate positive numerical input from user."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Value must be positive. Please try again.")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid number.")

def calculate_shipping_cost(weight: float, rate: float) -> float:
    """Calculate shipping cost based on weight and rate."""
    return weight * rate

def main():
    print("Shipping Cost Calculator\n" + "="*25)
    
    # Get user input with validation
    weight = get_valid_input("Enter package weight in kilograms: ")
    rate = get_valid_input("Enter shipping rate per kilogram (USD): ")
    
    # Calculate and display result
    cost = calculate_shipping_cost(weight, rate)
    print(f"\nShipping Cost: {cost:.2f} USD")

if __name__ == "__main__":
    main()
