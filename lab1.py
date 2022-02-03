"""
Lab 1: Problem Statement

Write a Python function to print all numbers from 1 to 100(inclusive).
For numbers that are divisible by 3, you should print "Fizz" instead of the number.
For numbers that are divisible by 5, you should print "Buzz" instead of the number.
For numbers that are divisible by both 3 and 5, you should print "FizzBuzz" instead of the number.

Sample I/O:

Input: None

Output:
1
2
Fizz
4
Buzz
...
14
FizzBuzz
16
...
"""

def printNumbers():
    # Enter your code after this line. Replace the pass statement.
    for x in range(101): 
    	if x%3==0 and x%5==0: 
    		print('FizzBuzz')
    	elif x%3 == 0: 
    		print('Fizz')
    	elif x%5 == 0: 
    		print('Buzz')
    	else: 
    		print(x)

printNumbers()
