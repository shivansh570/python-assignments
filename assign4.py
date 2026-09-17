'''
#1. Create list L2 having all the numbers of list L1 which are divisible by 5, and enter
 #a list L1 from the user.

L1 = []
while True:
    a = int(input("enter"))
    L1.append(a)
    g = input("cont? (y/n)")
    if g.lower()!="y":
        break
def main(L1):
    L2 = [x for x in L1 if x%5==0]
    return(L2)
main(L1)

'''

'''
#2. Create a list L3 having the elements as the square of each element of L1, and enter
# a list L1 from the user.

L1 = []
while True:
    a = int(input("enter"))
    L1.append(a)
    g = input("cont? (y/n)")
    if g.lower()!="y":
        break
def main(L1):
    L3 = [x*x for x in L1]
    return(L3)
main(L1)

'''