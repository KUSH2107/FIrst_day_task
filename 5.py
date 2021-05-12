'''
Write a program that accepts sequence of lines as input and prints the lines after making
all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''
T = int(input())

kp = []

while T>0 :

	a1 = input()
	kp.append(a1)
	T -= 1

for i in kp:
	print(i.upper())

