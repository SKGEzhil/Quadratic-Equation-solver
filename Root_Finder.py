from math import sqrt


def hcf(a, b):
    while b:
        a, b = b, a % b
    return a


def simplifier(numer, denom):
    if denom == 0:
        return "Division by 0 - result undefined"
    common_divisor = hcf(numer, denom)
    reduced_num = numer / common_divisor
    reduced_den = denom / common_divisor
    if common_divisor == 1:
        return numer, denom
    else:
        if reduced_den > denom:
            if reduced_den * reduced_num < 0:
                return -reduced_num, -reduced_den
            else:
                return reduced_num, reduced_den
        else:
            return reduced_num, reduced_den


def root_finder():
    print("\nEnter the coefficients of ax² + bx + c")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    x_1 = ((-b) + (sqrt(b ** 2 - 4 * a * c))) / (2 * a)
    x_2 = ((-b) - (sqrt(b ** 2 - 4 * a * c))) / (2 * a)
    print(f"\nThe roots of the equation are:\n{x_1} and {x_2}")
