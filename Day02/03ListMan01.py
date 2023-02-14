l1 = list()
print(f"l1 : {l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, "four", 'five', 6, "Seven", 8.1, 9.6, 10+0j, 11-0j, True, False]
print(f"l2 : {l2}")
print(type(l2))
print(type(l2[9]))

l3 = list (range(1, 11))
print (f"l3: {l3}")
print(type(l3))

print("-" * 40)
#memory allocation
l4 = [1, 2, 3, "four", 'five', 6, "Seven", 8.1, 9.6, 10+0j, 11-0j, True, False]
print(f"l4 : {l4}")
print(id(l4[0]))
print(id(l4[1]))
print(id(l4[2]))
print(id(l4[3]))
print(id(l4[4]))

print("-" * 40)
l5 = [1, 2, 3, 4, 5]
print(f"l5 : {l5}")
l5[3] = 3.5
print(f"l5 : {l5}")

del l5[3]
print(f"l5 : {l5}")
print("-" * 40)
#print(dir(list))

#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# add new values into a list - append, extend, insert

print("append".center(40, "-"))
l6 = [1, 2, 3, 4, 5]
print(f"l6 : {l6}")

l6.append(6)
l6.append(7)
l6.append(8)
print(f"l6 : {l6}")

l6.append([9,10,11,12,13])
print(f"l6 : {l6}")

# l6.extend([9,10,11,12,13])
# print(f"l6 : {l6}")

print(l6[8][2:5])

print("extend".center(40, "-"))
l1 = ['a', 'b', 'c', 'd', 'e']
print(f"l1 : {l1}")
l1.extend(['f', 'g', 'h', 'i', 'j'])
print(f"l1 : {l1}")

print("insert".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 : {l1}")
l1.insert(1, 1.55)
print(f"l1 : {l1}")
l1.insert(3, 2.55)
print(f"l1 : {l1}")
l1.insert(5, 3.55)
print(f"l1 : {l1}")
l1.insert(7, 4.55)
print(f"l1 : {l1}")

print(f"len(l1) : {len(l1)}")
l1.insert(15, 100)
print(f"l1 : {l1}")
print(f"len(l1) : {len(l1)}")

print("-" * 40)

import numpy as np
from sys import getsizeof
l1 = list(range(1,11000))
print(getsizeof(l1))
arr=np.array(range(1,11000))
print(getsizeof(arr))