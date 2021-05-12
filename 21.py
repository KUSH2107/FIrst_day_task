'''
By using list comprehension, please write a program generate a 3*5*8 3D array whose
each element is 0
'''
a = 3
b = 5
c = 8

lst = [[ [ 0 for col in range(a)] for col in range(b)] for row in range(c)]

print(lst)
