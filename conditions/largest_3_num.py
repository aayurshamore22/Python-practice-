def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    return c

print(largest(10, 40, 30))
