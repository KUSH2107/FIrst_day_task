'''
By using list comprehension, please write a program to print the list after removing the
0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
'''

l1 =  [12,24,35,70,88,120,155]

l1 = [x for (i,x) in enumerate(l1) if i not in (0,2,4,6)]

print(l1)