def multiply_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

numbers = [1, 2, 3, 4, 5]
print(multiply_list(numbers))