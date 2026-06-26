def add(a, b):
    """
    Adds two numbers and returns the sum.
    """
    return a + b

def subtract(a, b):
    """
    Subtracts the second number from the first and returns the difference.
    """
    return a - b

def divide(a, b):
    """
    Divides the first number by the second and returns the float result.
    Raises ZeroDivisionError if the second number is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
