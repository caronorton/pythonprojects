from Notes5 import Fraction

f1 = Fraction(4, 7)
print("f1 = ", f1)

f2 = Fraction(3, 5)
print("f2 =", f2)

print(f1.getNumerator())
print(f1.asDecimal())
f1.multiplyFraction(f2)
print("f1 = ", f1)
