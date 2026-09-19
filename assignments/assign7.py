'''
#1.Write a Python program to count the number of characters (character frequency)
#in a string.

d={ }
str = input("enter string:")
for i in range(len(str)):
    if str[i] in d:
        d[str[i]] += 1
    else:
        d[str[i]] = 1
print(d)

'''

'''
#2.Write a Python program to get a string made of the first 2 and last 2
#characters of a given string. If the string length is less than 2, return the
#empty string instead.

str = input("enter string:")
if len(str)<2:
    print("")
else:
    print(str[:2]+str[-2:])
'''

'''
#3.Write a Python program to get a single string from two given strings, separated
#by a space and swap the first two characters of each string.

a = input("enter string:")
b = input("enter string:")
print(b[:2] + a[2:] + " " + a[:2] + b[2:])

'''