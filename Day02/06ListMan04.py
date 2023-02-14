print("copy".center(40, '-'))
l1=list(range(1,5))
print(f"l1 Before : {l1}")

l2 = l1     # shadow copy - copies the address along with data

print(f"l2 Before : {l2}")
l2.append(6)
l2.append(7)
l2.append(8)
print(f"l1 After : {l1}")
print(f"l2 After : {l2}")

print("*" * 40)
print(f"l1 Before : {l1}")
l3=l1.copy()
print(f"l3 Before : {l3}")
l3.append(9)
l3.extend([10,11])
print(f"l3 After : {l3}")
print(f"l1 After : {l1}")

print("*" * 40)
l4 = [11, 22, 33, 44, [2, 4, 6, 8, 10], 55]
print (f"14 Before: {14}")

l5 = l4.copy()
print (f"15 Before: {15}")
l5[4].extend([12,14,16])
print(f"l4 After : {l4}")
print(f"l5 After : {l5}")

l6=[1,2,3,4,[11,22,33,44,55],5]
print (f"16 Before: {16}")

from copy import deepcopy
l7 = deepcopy(l6)

l7[4].extend([12,14,16])
print(f"l6 After : {l6}")
print(f"l7 After : {l7}")

