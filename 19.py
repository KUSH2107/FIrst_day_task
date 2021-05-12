'''
Please write a program to print the list after removing delete even numbers in
[5,6,77,45,22,12,24].
'''

l1 = [5,6,77,45,22,12,24]

l1 = [x for x in l1 if x%2!=0]

print(l1)