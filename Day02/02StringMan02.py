print ("replace".center(40, "-"))
st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

print(f"st1: {st1}")
res = st1.replace("h", "H")
print(f"res: {res}")

res = st1.replace("l", "L")
print(f"res: {res}")

res = st1.replace("l", "L", 1)
print(f"res: {res}")

res = st1.replace("l", "L", 2)
print(f"res: {res}")

print("-" * 40)
print(f"st2: {st2}")

res= st2.replace("the", "The")
print(f"res: {res}")

res= st2.replace("the", "The", 1)
print(f"res: {res}")

# maketrans and translate
print("maketrans".center(40, "-"))
st1 = "hello world"
print(f"st1: {st1}")
s1 = "helowrd"
s2 = "HELOWRD"
# length of s1 and s2 should be equal

resTbl = st1.maketrans(s1, s2)
print(f"resTbl : {resTbl}")

print("translate".center(40, "-"))
res = st1.translate(resTbl)
print(f"res : {res}")

print("strip".center(40, "-"))
st = "********hello********"
print(f"st: {st}")

print(st.rstrip("*"))
print(st.lstrip("*"))
print(st.strip("*"))

st = "+91-9894-530157"
print (f"st : {st}")
res = st.rpartition("-")
print(res)

print("format".center(40, "-"))
print("Welcome {}, what a {} player".format("Messi", "class"))
print("Welcome {pname}, what a {adj} player".format(pname="Messi", adj="class"))
print("Welcome {0}, with a rating of {1} what a {2} player".format("Messi", 9.8, "class"))
print("Welcome {0}, with a rating of {1:.2f} what a {2} player for {club}".format("Messi", 9.8, "class", club="PSG"))
print("Welcome {0}, with a rating of {rating:.3f} what a {adj} player for {club}".format("Messi", rating=9.8, adj="class", club="PSG"))
