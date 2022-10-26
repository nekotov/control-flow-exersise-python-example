import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = b ** 2 - 4 * a * c
if d < 0:
    print("No roots")
elif d == 0:
    print("x = ", -b / (2 * a))
else:
    print("x1 = ", (-b + math.sqrt(d)) / (2 * a))
    print("x2 = ", (-b - math.sqrt(d)) / (2 * a))