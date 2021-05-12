
'''
By using list comprehension, please write a program to print the list after removing the
0th,4th,5th numbers in [12,24,35,70,88,120,155].
'''
l1 = [12,24,35,70,88,120,155]

l1 = [x for x in l1 if x !=12 and x !=88 and x !=120]

print(l1)
