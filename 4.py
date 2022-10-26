# Знайти бiльше iз чисел A, B, C.
a = int(input("Введiть перше число: "))
b = int(input("Введiть друге число: "))
c = int(input("Введiть третє число: "))
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)
else:
    print("Числа рiвнi")

