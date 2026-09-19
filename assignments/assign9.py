'''
#1. Write a loop that counts the number of digits that appear in the string referenced by mystring.

mystring = input("enter string:")
c = 0
for i in mystring:
    if i.isdigit():
        c += 1
print(f"total digits in string is {c}")

'''

'''
#2. Write a loop that counts the number of lowercase characters that appear in the string referenced by mystring.

mystring = input("enter string:")
c = 0
for i in mystring:
    if i.islower():
        c += 1
print(f"total lowercase digits in string is {c}")

'''

'''
#3. Write a function that accepts a string as an argument and returns true if the argument ends with the substring '.com'. Otherwise, the function should return false.

str = input("enter string:")
def end(str):
    if str.endswith('.com'):
        return True
    else:
        return False
end(str)

'''

'''
#4.Write code that makes a copy of a string with all occurrences of the lowercase letter 't' converted to uppercase.

str = input("enter string:")
a = ""
for i in str:
    if i == 't':
        a = a + 'T'
    else:
        a = a + i
print(a)

'''

'''
#5.Write a function that accepts a string as an argument and displays the string backwards.

str = input("enter string:")
def back(str):
    rev = str[::-1]
    print(rev)
back(str)

'''

'''
#6.Assume mystring references a string. Write a statement that uses a slicing expression and displays the first 3 characters in the string.

print(mystring[:3])

'''

'''
#7.Assume mystring references a string. Write a statement that uses a slicing expression and displays the last 3 characters in the string.

print(mystring[-3:])

'''