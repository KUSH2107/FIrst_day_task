'''
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the
value of a.
Suppose the following input is supplied to the prografor i in range(1,7):
for j in range(1,7):
if j<=i:
print("*",end=" ")
else:
print(" ",end=" ")
print()m:
9
Then, the output should be:
11106
'''

digit=int(input("Enter digit:"))
num=input("enter a number:")

result=0
for i in range(1,digit+1):
  result= result + int(str(num*i))
  print(i)
print(result)  