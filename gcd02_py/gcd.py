def gcd(a, b):
    """
    Function to find the GCD of two numbers using the Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

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

# Function to take input for n numbers
def take_input():
    try:
        n = int(input("Enter the number of elements: "))
        numbers = []
        for i in range(n):
            num = int(input("Enter number {}: ".format(i+1)))
            numbers.append(num)
        return numbers
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return take_input()

# Main function
def main():
    numbers = take_input()
    if numbers:
        print("The GCD of", numbers, "is:", gcd_of_multiple_numbers(numbers))

if __name__ == "__main__":
    main()
