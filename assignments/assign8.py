'''
#1. WAP a program to check if a string is palindrome or not.

#M1)
str = input("enter string:")
a = str[::-1]
if str == a:
    print(f"{str} is a palindrome")
else:
    print(f"{str} is not a palindrome")

#M2)
str = input("enter string:")
a = ""
for i in str:
    a = i + a
if str == a:
    print(f"{str} is a palindrome")
else:
    print(f"{str} is not a palindrome")

'''

'''
#2. WAP to reverse words in a given String in Python.

#M1)
str = input("enter string:")
a = " "
a = str[::-1]
print(a)

#M2)
str = input("enter string:")
a = ""
for i in str:
    a = i + a
print(a)

'''

'''
#3. WAP to count the Number of matching characters in a pair of strings.

str1 = input("enter string1:")
str2 = input("enter string2:")
m = " "
c = 0
for i in str1:
    for j in str2:
        if i == j:
            if i not in m:
                m = m + i
                c += 1
print(f"{c} characters are repeated in the strings")

'''
