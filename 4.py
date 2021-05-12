'''
Write a program which accepts a sequence of comma-separated numbers from the
console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''

T = int(input())

kp = []

while T>0:

	a1 = input()
	kp.append(a1)
	T -= 1
print(kp)

pk = tuple(kp)

print(pk)

