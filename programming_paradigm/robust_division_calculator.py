# robust_division_calculator.py

# This function safely divides two values and handles potential errors.
def safe_divide(numerator, denominator):
    try:
        # Try to convert inputs to float for numeric division
        num = float(numerator)
        den = float(denominator)

        # Attempt the division
        result = num / den
        return f"The result of the division is {result}"

    # Handle division by zero
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    # Handle non-numeric inputs
    except ValueError:
        return "Error: Please enter numeric values only."
