print("items".center(40, '-'))
emp = {
    'emp1': {'name':'Mike', 'age':34, 'dept':'finance', 'desig': 'MGR', 'sal':85000},
    'emp2': {'name':'Mary', 'age':30, 'dept':'HR', 'desig': 'HR Executive', 'sal':45000},
    'emp3': {'name':'Steve', 'age':32, 'dept':'IT', 'desig': 'TL', 'sal':75000}
}
print (f"emp : {emp}")
print("-" * 40)

print(f"emp1 : {emp['emp1']}")
print(f"emp2 : {emp['emp2']}")
print(f"emp3 : {emp['emp3']}")

print('-' * 40)
# keys and values
for ky, info in emp.items():
    print (ky)
    print ("-" * len(ky))
    for k, v, in info.items():
        print (k, "=>", v)
    print("-" * 40)


print("update".center(40, "-"))

emp1 = {'name': 'Mike', 'age': 34, 'dept': 'finance', 'desig': 'MGR'}
emp2 = {'name': 'Mary', 'age': 30, 'dept': 'HR', 'sal': 45000}
print(f"emp1 : {emp1}")
print(f"emp2 : {emp2}")

print("-" * 40)
emp1.update(emp2)
print(f"emp1 : {emp1}")
print(f"emp2 : {emp2}")

print("-" * 40)
emp1 = {'name': 'Mike', 'age': 34, 'dept': 'finance', 'desig': 'MGR'}
print(f"emp1 : {emp1}")

emp1.clear()
print(f"emp1 : {emp1}")

print("copy".center(40, "-"))
emp1 = {'name': 'Mike', 'age': 34, 'dept': 'finance', 'desig': 'MGR'}
print(f"emp1 before: {emp1}")

emp2 = emp1     # shallow copy - copies the address along with the data
print(f"emp2 before: {emp2}")

emp2['sal'] = 45000
emp2['loc'] = 'Hyd'

print(f"emp1 after: {emp1}")
print(f"emp2 after: {emp2}")

print("\n", "="*40, '\n')
emp3 = {'name': 'Mary', 'age': 30, 'dept': 'HR', 'sal': 45000}
print(f"emp3 before: {emp3}")

emp4 = emp3.copy()              # deep copy
print(f"emp4 before: {emp4}")
emp4['desig'] = "HR Executive"
emp4['loc'] = 'Che'
print("-" * 40)
print(f"emp3 after: {emp3}")
print(f"emp4 after: {emp4}")

print("\n", "="*40, '\n')
emp5 = {'name': 'Mary', 'age': 30, 'dept': 'HR', 'sal': 45000, 'desig': {'wipro': 'Trainee', 'ibm' : 'Accountant', 'hp': 'TL'}, 'loc': 'Che'}
print(f"emp5 before : {emp5}")

emp6 = emp5.copy()

print(f"emp6 before : {emp6}")
emp6['desig']['tesco'] = 'TL'
emp6['desig']['sap'] = 'TM'
print("-" * 40)

print(f"emp5 after : {emp5}")
print(f"emp6 after : {emp6}")

emp7 = {'name': 'Mary', 'age': 30, 'dept': 'HR', 'sal': 45000, 'desig': {'wipro': 'Trainee', 'ibm': 'Accountant'}, 'loc': 'Che'}
print(f"emp7 before : {emp7}")
from copy import deepcopy

emp8 = deepcopy(emp7)
print(f"emp8 before : {emp6}")

emp8['desig']['tesco'] = 'TL'
emp8['desig']['sap'] = 'TM'

print("-" * 40)

print(f"emp7 after : {emp7}")
print(f"emp8 after : {emp8}")
