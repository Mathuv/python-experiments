def is_prime(number):
    """Return True if *number* is prome."""
    for element in range(number):
        if number % element == 0:
            return False

    return True


def print_next_prime(number):
    """Print the closest prime number larger than *number*."""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)


def my_addition_function(number1, number2):
    return number1 + number2
