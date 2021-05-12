'''
Please write a program to randomly generate a list with 5 even numbers between 100
and 200 inclusive.
'''
import random

T = 50

list1 = []

while T>0:

	a = random.randint(1,100)
	if a%2 == 0:
		list1.append(a)

	T -= 1	
l1 = list1[:5]
print(l1)
