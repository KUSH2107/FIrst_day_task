'''
By using list comprehension, please write a program to print the list after removing the
value 24 in "the list is :",
'''

given_list = [12, 24, 35, 70, 88, 120, 155]
given_list = [number for number in given_list if number != 24]
print(given_list)