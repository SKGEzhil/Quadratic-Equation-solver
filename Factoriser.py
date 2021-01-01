from math import *


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


def factor_finder():
    print("\nEnter the coefficients of ax² + bx + c")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    if b ** 2 - 4 * a * c >= 0:
        x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        mult1 = -x1 * a
        mult2 = -x2 * a
        (num1, den1) = simplifier(a, mult1)
        (num2, den2) = simplifier(a, mult2)
        if (num1 > a) or (num2 > a):
            print("It has no Factors")
        else:
            if den1 > 0:
                sign1 = "+"
            else:
                sign1 = ""
            if den2 > 0:
                sign2 = "+"
            else:
                sign2 = ""
            print(
                "\nThe Factors of the equation are:\n({}x{}{})({}x{}{})".format(int(num1), sign1, int(den1), int(num2),
                                                                                sign2, int(den2)))
    else:
        print("Solutions are imaginary")
    return


def factorize():
    print("\nEnter the coefficients of ax² + bx + c")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    r = ((-b) + (sqrt(b ** 2 - 4 * a * c))) / (2 * a)
    s = ((-b) - (sqrt(b ** 2 - 4 * a * c))) / (2 * a)
    p = -r
    q = -s
    # (r, s) = simplifier(p, q)

    if (hcf(abs(a), abs(b)) > 1) and (hcf(abs(b), abs(c)) > 1) and (hcf(abs(c), abs(a)) > 1) and abs(c) > abs(b):
        (i, j) = simplifier(a, b)
        (j, k) = simplifier(b, c)
        (k, i) = simplifier(c, a)

        if (b > 0) and (c < 0 or a < 0):
            e = int((j + sqrt(j ** 2 - 4 * i * k)) / 2 * i)
            f = int((j - sqrt(j ** 2 - 4 * i * k)) / 2 * i)
            (g, h) = simplifier(e, f)
            print(g)
            print(h)
            print(f"step-1: \n{round(i)}x²+{round(-j)}x+{round(k)}")
            print("\nstep-2: \n{}x²+({}x)+({}x)+({})({})".format(round(i), round(e), round(f), round(e), round(f)))
            if (i % e) != 0:
                print(f"\nstep-3: \n{round(i)}x(x + {round(e)})+{round(f)}(x + {round(e)})")
            elif ((i % e) == 0) and round(e) == 1:
                print(f"\nstep-3: \n{round(i)}x(x + {round(e)})+{round(f)}(x + {round(e)})")
            elif ((i % e) == 0) and round(e) != 1:
                if i < e:
                    m = e / i
                    print("ok")
            print(f"\nstep-4: \n({round(i)}x+{round(f)})(x+{round(e)})")
        if (b < 0) and (c > 0 or a > 0):
            print("11")
            print(j)
            g = int((j + sqrt(j ** 2 - 4 * i * k)) / 2 * i)
            h = int((j - sqrt(j ** 2 - 4 * i * k)) / 2 * i)
            e = -g
            f = -h
            print(f"step-1: \n{round(i)}x²+{round(-j)}x+{round(k)}")
            print("\nstep-2: \n{}x²+({}x)+({}x)+({})({})".format(round(i), round(e), round(f), round(e), round(f)))
            if (i % e) != 0:
                print(f"\nstep-3: \n{round(i)}x(x + {round(e)})+{round(f)}(x + {round(e)})")
            elif ((i % e) == 0) and round(e) == 1:
                print(f"\nstep-3: \n{round(i)}x(x + {round(e)})+{round(f)}(x + {round(e)})")
            elif ((i % e) == 0) and round(e) != 1:
                if i < e:
                    m = e / i
                    print("ok")
            print(f"\nstep-4: \n({round(i)}x + {round(f)})(x + {round(e)})")
    else:
        print("\nstep-1: \n{}x²+({}x)+({}x)+({})({})".format(a, round(p), round(q), round(p), round(q)))
        if (a % p) != 0:
            print(f"\nstep-2: \n{a}x(x + {round(p)}) + {round(q)}(x + {round(p)})")
        if ((a % p) == 0) and round(p) == 1:
            print(f"\nstep-2: \n{a}x(x + {round(p)}) + {round(q)}(x + {round(p)})")
        if ((a % p) == 0) and round(p) != 1 and round(p) != -1:
            m = p / a
            print("ok")
            # print(f"\nstep-2: \n{a}x(x + {round(m)})+{round(s)}(x + {round(m)}")
        print(f"\nstep-3: \n({a}x + {round(q)})(x + {round(p)})")

# a = int(2)
# b = int(-4)
# c = int(2)
# r = ((-b + sqrt((b**2)-4*a*c))/2*a)
# print(-b)
# print(sqrt(b**2 -4*a*c))
# print(2*a)
# print(((-b)+(sqrt(b**2 -4*a*c)))/(2*a))
# print(r)
