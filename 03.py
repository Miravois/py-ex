'''Functions Exercises


Exercise 3.3
Python provides a built-in function called 'len' that returns the length of
a string. Write a function named right_justify that takes a string named s as 
a parameter and prints the string with enough leading spaces so that the last 
letter of the string is in column 70 of the display.


Exercise 3.4
A function object is a value you can assign to a variable or pass as an argument.
For example, do_twice is a function that takes a function object as an argument
and calls it twice:

def do_twice(f):
    f()
    f()

Here's an example that uses do_twice to call a function named print_spam twice.

def print_spam():
    print 'spam'

do_twice(print_spam)

1. Type this example into a script and test it.
2. Modify do_twice so that it takes two arguments, a function object and a value,
and calls the function twice, passing the value as an argument.
3. Write a more general version of print_spam, called print_twice, that takes a
string as a parameter and prints it twice.
4. Use the modified version of do_twice to call print_twice twice, passing 'spam'
as an argument.
5. Define a new function called do_four that takes a function object and a value
and calls the function four times, passing the value as a parameter. There
should be only two statements in the body of this function, not four.


Exercise 3.5
1. Write a function that draws a grid like the following:

+----+----+
|    |    |
|    |    |
|    |    |
|    |    |
+----+----+
|    |    |
|    |    |
|    |    |
|    |    |
+----+----+

Hint: to print more than one value on a line, you can print a comma-separated
sequence:
print '+', '-'

If the sequence ends with a comma, Python leaves the line unfinished, so the
value printed next appears one the same line.
print '+',
print '-'

The output of these statements is '+-'.

A print statement all by itself ends the current line and goes to the next line.

2. Write a function that draws a similar grid with four rows and four columns.

''' 