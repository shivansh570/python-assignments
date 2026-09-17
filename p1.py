'''
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
str = input("enter string:")
if len(str)<2:
    print("")
else:
    print(str[:2]+str[-2:])
'''

'''
a = input("enter string:")
b = input("enter string:")
print(b[:2] + a[2:] + " " + a[:2] + b[2:])
'''
print(1%2)