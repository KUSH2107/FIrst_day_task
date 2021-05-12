'''
Write a program that accepts a sentence and calculate the number of uppercase letters
and lowercase letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''

a = input()

UPPERCASE = 0
LOWERCASE = 0

for i in a:
	if i.isupper():
		UPPERCASE += 1
	elif i.islower():
		LOWERCASE += 1

print(UPPERCASE)
print(LOWERCASE)
