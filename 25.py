'''
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list
after removing all duplicate values with original order reserved.
'''

l1 = [12,24,35,24,88,120,155,88,120,155]

l2 = set(l1)

l3 = list(l2)

print(l3)