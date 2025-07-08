# main.py

import sys  # Import sys to access command line arguments
from robust_division_calculator import safe_divide  # Import the division function

def main():
    # Ensure that exactly two arguments are provided: numerator and denominator
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)  # Exit the program with error code 1

    # Extract arguments from the command line
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the safe_divide function and print the result
    result = safe_divide(numerator, denominator)
    print(result)

# This ensures main() runs only when the script is executed directly
if __name__ == "__main__":
    main()
