def is_palindrome(n):
    return str(n) == str(n)[::-1]

def next_palindromic_number(n):
    n += 1
    while not is_palindrome(n):
        n += 1
    return n

# Example usage:
number = 123
next_palindrome = next_palindromic_number(number)
print(f"The next palindromic number after {number} is {next_palindrome}")
