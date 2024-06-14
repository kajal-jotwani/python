def std_poly(poly: str) -> str:
    split_poly = poly.split()

    return " " .join(split_poly[::-1])

print(std_poly("x^5 + 6x^4 + 7x^3 - 5x^2 + 3x^1 + 1"))