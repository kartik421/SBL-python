# Iterative approach
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Recursive approach
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Test the functions
number = int(input("Enter a number to find its factorial: "))

# # Using iterative approach
# factorial_iter = factorial_iterative(number)
# print(f"Factorial of {number} (iterative): {factorial_iter}")

# Using recursive approach
factorial_rec = factorial_recursive(number)
print(f"Factorial of {number} (recursive): {factorial_rec}")
