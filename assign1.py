'''
# 1. Read any 5 numbers and compute their sum and average.

sum = 0
count = 0
while True:
    if count == 5:
        break
    num = int(input("Enter number : "))
    sum += num
    count += 1

average = sum / 5

print(f"Sum: {sum}")
print(f"Average: {average}")
'''

'''
#2. Read the value of N and compute the sum and average of any N numbers entered by the
user.

sum = 0
count = 0
N = int(input("Enter the value of N: "))
while True:
    if count == N:
        break
    num = int(input("Enter number : "))
    sum += num
    count += 1

average = sum / N

print(f"Sum: {sum}")
print(f"Average: {average}")

'''

'''
#3. Read the value of N and compute the sum and average of all odd numbers lying between 1
to N.

sum = 0
count = 0
N = int(input("Enter the value of N: "))
for i in range(1, N + 1, 2):
    sum += i
    count += 1
average = sum / count
print(f"Sum: {sum}")
print(f"Average: {average}")

'''

'''
#4. Read the value of N and compute factorial of N.

N = int(input("Enter the value of N: "))
fact = 1
for i in range(1, N + 1):
    fact *= i
print(f"Factorial of {N}: {fact}")

'''

'''
#5. Read the value of N and read N integers. Compute the sum and average of only the even
numbers entered.

N = int(input("Enter the value of N (how many numbers): "))
sum = 0
count = 0
for i in range(N):
    num = int(input("Enter number: "))
    if num % 2 == 0:
        sum += num
        count += 1
average = sum/count
print(f"Sum of even numbers: {sum}")
print(f"Average of even numbers: {average}")

'''

'''
#6. Read 5 numbers and print the largest of the three numbers.

largest = -9999999999999999999999
for i in range(5):
    num = float(input("Enter number: "))
    if num > largest:
        largest = num
print(f"The largest number is: {largest}")

'''

'''
#7. Keep reading the numbers from the user and add them till a negative number is entered.

sum = 0
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break  
    sum += num

print(f"The Sum: {sum}")

'''