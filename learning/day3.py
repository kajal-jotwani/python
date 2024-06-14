# def std_poly(poly: str) -> str:
#     split_poly = poly.re.split()

#     return " " .join(split_poly[::-1])

# print(std_poly("x^5 + 6x^4 + 7x^3 - 5x^2 + 3x^1 - 1"))
   
p = "x^5 + 6x^4 + 7x^3 - 5x^2 + 3x^1 - 1"

SPACE, NONE = " ", ""
PLUS, MINUS, SPLUS, SMINUS  = "+", "-", " +", " -"

def terms(eqn: str) -> str:
    return eqn.replace(SPACE, NONE)\
    .lstrip(PLUS)\
    .replace(PLUS,SPLUS)\
    .replace(MINUS,SMINUS)\
    .lstrip(SPACE)\
    .split()

def to_math_form( eqn: str) -> str:
    return PLUS.join(reversed(terms(eqn)))\
    .replace(PLUS + MINUS, MINUS)\
    .replace(PLUS + PLUS, PLUS)

print(p)
print(to_math_form(p))