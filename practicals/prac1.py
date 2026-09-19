'''
#1. Write a program to find the roots of a quadratic equation. 

a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))
if a !=0 :
    d = b**2 - 4*a*c
    if d >= 0:
        root1 = (-b + d**0.5) / (2*a)
        root2 = (-b - d**0.5) / (2*a)
        print("The roots are:", root1, "and", root2)
    else:
        print("The equation has no real roots.")
else:
    print("The coefficient of x^2 cannot be zero.")

'''

'''
#2. Write a program to create a pyramid of the character "*" and a reverse pyramid.

rows = int(input("Enter the number of rows for the pyramid: "))
for i in range(rows, 0, -1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(0,i):
        print("*", end="")
    print()

'''

'''
#3. Write a program to accept a number "n" and: 
 # a. Check if "n" is prime.
 # b. Generate all prime numbers till "n".
 # c. Generate first "n" prime numbers.

def prime(n):
    if n <= 1:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True
    
def till_primes(n):
    print(f"Prime numbers till {n}:" , end = " ")
    for i in range(2, n + 1):
        if prime(i):
            print(i, end=" ")
    print()
    
def first_primes(n):
    print(f"First {n} prime numbers:" ,end = " ")
    count = 0
    num = 2
    while count < n:
        if prime(num):
            print(num, end=" ")
            count += 1
        num += 1
    print()

n = int(input("Enter a number: "))
if prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
till_primes(n)
first_primes(n)

'''