# Please write a program to generate a list with 5 random numbers between 100 and 200
# inclusive.

import random

T = 5
list1 = []

while T>0:

	a = random.randint(100, 200)
	list1.append(a)
	T -= 1

print(list1)	