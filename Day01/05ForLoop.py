for i in range(1, 11):
    print(i, end=" ")

print()
print("hello")

for i in range(1, 30):
    if i > 25:
        break       # come out of the iteration
    if i % 2 == 0:
        continue    # skip the iteration
    print(i, end=" ")
else:
    print ("\n Iteration completed....")