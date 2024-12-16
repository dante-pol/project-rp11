import math

a = int(input("input a >>"))
b = int(input("input b >>"))
c = int(input("input c >>"))

p = (a + b + c) / 2

s = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(f"s={s}")