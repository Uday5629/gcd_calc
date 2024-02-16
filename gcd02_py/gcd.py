import random

# ////////////////////// Iterative function ///////////////////////////////

def gcd(a, b):
    """
    Function to find the GCD of two numbers using the Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

# /////////////////////// Recursive function ////////////////////////////

# def gcd(a, b):
#     # Base case: if b is 0, return a (the current value of a is the GCD)
#     if b == 0:
#         return a
#     # Recursive case: call gcd function with arguments b and the remainder of a divided by b
#     return gcd(b, a % b)


def gcd_of_multiple_numbers(numbers):
    """
    Function to find the GCD of multiple numbers using the GCD of two numbers.
    """
    if len(numbers) == 0:
        return None  # No numbers provided

    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    return result

# Function to generate n random numbers
def generate_random_numbers(n, min_value=1, max_value=100):
    """
    Function to generate n random numbers within a given range.
    """
    return [random.randint(min_value, max_value) for _ in range(n)]

# Main function
def main():
    try:
        n = int(input("Enter the number of elements: "))
        if n <= 0:
            print("Number of elements should be greater than 0.")
            return

        numbers = generate_random_numbers(n)
        print("Generated numbers:", numbers)
        print("The GCD of the generated numbers is:", gcd_of_multiple_numbers(numbers))
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
