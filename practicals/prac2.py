'''
#1. Write a program to create a list of the cubes of only the even integers appearing in the input list (may have elements of
#other types also) using the following: 
 #a. 'for' loop 
 #b. list comprehension 

L1= [ ] 
while True:
    a = int(input("enter no"))
    L1.append(a)
    g = input("cont? (y/n)")
    if g.lower() !="y":
        break

#a)
L2 = [ ]
for i in L1:
    if i%2==0:
        L2.append(i**3)
print(L2)

#b)
L2 = [x*x*x for x in L1 if x%2==0]
print(L2)

'''

'''
#2. Consider a tuple t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10). Write a program to perform following operations: 
 #a. Print half the values of the tuple in one line and the other half in the next line. 
 #b. Print another tuple whose values are even numbers in the given tuple. 
 #c. Concatenate a tuple t2=(11,13,15) with t1. 
 #d. Return maximum and minimum value from this tuple.

t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

#a)
half_len = len(t1) // 2
print(t1[:half_len])
print(t1[half_len:])

#b)
t3 = tuple(x for x in t1 if x % 2 == 0)
print(t3)

#c)
t2 = (11, 13, 15)
t4 = t1 + t2
print(t4)

#d)
print("Maximum value:", max(t1))
print("Minimum value:", min(t1))

'''