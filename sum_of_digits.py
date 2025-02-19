
def sum_of_digits(number):
    """
    Calculate the sum of the digits of a number.
    
    :param number: int
    :return: int
    """
    # Convert the number to a string to iterate over each digit
    digits = str(number)
    # Initialize the sum to 0
    total = 0
    # Iterate over each digit and add it to the total
    for digit in digits:
        total += int(digit)
    return total

if __name__ == "__main__":
    # Test the function with a sample input
    sample_number = 12345
    print(f"The sum of the digits of {sample_number} is {sum_of_digits(sample_number)}")
