import random

def generate_random_numbers(count=4):
    random_numbers = [random.randint(1, 100) for _ in range(count)]
    return random_numbers

if __name__ == "__main__":
    numbers = generate_random_numbers()
    print(numbers)
