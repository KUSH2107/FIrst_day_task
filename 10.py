# Write a program which are divisible by 7 and between a given range 0 and n.
n = int(input())

for i in range(0,n):
	if i%7 == 0:
		print(i)