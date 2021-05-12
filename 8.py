'''
Write a program that computes the net amount of a bank account based a transaction log
from console input. The transaction log format is shown as following:
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
D means deposit while W means withdrawal.
Then, the output should be:
500
'''

	
T=int(input())
Total=0

while T>0:
    c, n=input().split()
    n=int(n)
    if c=='D':
        Total+=n
    elif c=='W':
        Total-=n
    T-=1
    
print(Total)