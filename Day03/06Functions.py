def greet():
    print("Greetings Mr. Messi, Welcome to the event.... ")
greet()

def greetGst(gname):
    print(f"Greeting Mr. {gname} Welcome to the event....")

# gname is an non default function arguments
# city is an default function arguments
def greetGstCty(gname, city="Barcelona"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event......")

greetGst("Messi")
greetGst("Ronaldo")

greetGstCty("Messi", "Barcelona")
greetGstCty("Ronaldo", "Turin")
greetGstCty("Neymar")

print("-" * 40)
# Variable length arguments
def prodAll(*numbers):      # *numbers can accepts more than one value and store it in a tuple
    print(f"numbers : {numbers}")
    prod = 1
    for number in numbers:
        prod *= number
    return prod

print(prodAll(1, 2, 3, 4, 5))

def extractDetails(**details):
    print(details)
    print("-" * 40)
    for k, v in details.items():
        print(k, "=>", v)

extractDetails(name="Messi", age=35, goal=350, club='PSG', ballondor=7)

# Using recursive calls find - 1. factorial of a number, 2. Fibanoccoi series

print("-" * 40)
def factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number * factorial(number-1)

print (factorial(int(5)))

print("-" * 40)
def fibonocci(number):
    if (number <= 1):
        return number
    else:
        return fibonocci(number-1) + fibonocci(number - 2)

for i in range(8):
    print(fibonocci(i), end=" ")
print()

print("-" * 40)
def arithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = arithCalc(20, 5)
print(res)

def a(b, c, d): pass

def f(): pass

print(type(f()))

a = [1, 2, 3, None, (), [],]
print (len(a))

print("\x48\x49!")

for i in range(2):
    print(i)
for i in range(4,6):
    print (i)

print("-" * 40)
def myfunc(x, y, z, a):
    print (x + y)

nums = [1, 2, 3, 4]
myfunc(*nums)

my_string='sivakumar'
k = [print(i) for i in my_string if i not in "aeiou"]
print(k)

my_string="hello world"
k = [(i.upper(), len(i)) for i in my_string]
print(k)

A=[[1,2,3],[4,5,6],[7,8,9]]
print(A[1])
b = {}
print(all(b))

def find(a, **b):
    print (type(b))
find('letters', A='1',B='2')