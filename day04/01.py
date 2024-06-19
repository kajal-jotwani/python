def inverse_modulo(r1, r2, y1 = 0, y2 = 1):
    q2 = r1//r2
    r3 = r1 - (r2 * q2)
    y3 = y1 - (q2 * y2)

    if r3 == 1:
        return y3
    else:
        return inverse_modulo(r2, r3, y2, y3)
#print(inverse_modulo(100, 37))

p = 101
a = 28
x = 1
for i in range(101):
    x = (a * x)%p
