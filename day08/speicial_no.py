import math

def is_square(num: int) -> bool:
    return math.sqrt(num).is_integer()

def is_even(num: int) -> bool:
    number = str(num)
    for digit in number:
        if int(digit) % 2 != 0:
            return False
    return True

def is_special(num: int) -> bool:
    return is_square(num) and is_even(num)

# Example usage:
print(is_special(6400))  
