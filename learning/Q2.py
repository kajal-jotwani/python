# def pyramid(n):
#     for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             print(i+j-1, end=" ")
#         print("\r")
 
# n = 5
# pyramid(n)
SPACE, LF = ' ', '\n'
SEP = "-----"
def is_triangular(n: int) -> bool:
    r = 1
    while r * (r + 1) < 2 * n:
        r += 1
    return r * (r + 1) == 2 * n

def format(n: int) -> str:
    spacer = LF if is_triangular(n) else SPACE
    return f'{n:4}{spacer}'

def make_pyramid(size: int) -> str:
    return ''.join([format(i) for i in range(1, size)]) + f'{size:4}' + LF + SEP

print(make_pyramid(15))