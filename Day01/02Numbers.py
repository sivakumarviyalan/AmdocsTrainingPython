a = 10
b = -10
print(f"a : {a}")
print(type(a))
print(f"b: {b}")
print(type(b))

print("-" * 40)

c = 10.3
d = -10.3
print(f"c : {c}")
print(type(c))
print(f"d: {d}")
print(type(d))
print("-" * 40)

e = 2e3
f = -2e3
print(f"e : {e}")
print(type(e))
print(f"f: {f}")
print(type(f))

print("-" * 40)

g = 10 + 3j
h = 10 - 3j

print(f"g : {g}")
print(type(g))
print(f"h: {h}")
print(type(h))

x = 10
y = 15.4
z = x + y
print(f"x= :{type(x)}")
print(f"y= :{type(y)}")
print(f"z= :{type(z)}")

print("conversion".center(40, "-"))

a = 100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print ("Number System".center(40, "-"))
print(f"11    : {11}")      # decimal
print(f"0b11  : {0b11}")      # binary
print(f"0b101 : {0b101}")      # binary
print(f"0o11  : {0o11}")      # octal
print(f"0o101 : {0o101}")      # octal
print(f"0xe   : {0xe}")      # hexa
print(f"0xb   : {0xb}")      # hexa

print ("Number System Conversion".center(40, "-"))
a = 100
print(f"a   : {a}")      # decimal
print(f"bin(a) : {bin(a)}")      # binary
print(f"oct(a) : {oct(a)}")      # octal
print(f"hex(a) : {hex(a)}")      # hexa
