# Exercise 3.3
'''
Python provides a built-in function called 'len' that returns the length of
a string. Write a function named right_justify that takes a string named s as 
a parameter and prints the string with enough leading spaces so that the last 
letter of the string is in column 70 of the display.
'''
def right_justify(s):
    length = len(s)
    print " "*(70 - length) + s

# Exercise 3.4
'''
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
'''
# 1
'''
def do_twice(f):
    f()
    f()

def print_spam():
    print 'spam'

do_twice(print_spam)
'''

# 2
def do_twice(f, val):
    f(val)
    f(val)

# 3
def print_twice(s):
    print s
    print s

# 4
do_twice(print_twice, 'spam')

# 5
def do_four(f, val):
    do_twice(f, val)
    do_twice(f, val)
    

# Exercise 3.5
'''1. Write a function that draws a grid like the following:

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
# 1
def draw_grid():
    def draw_frame(item1, item2):
        print item1,item2*4,item1,item2*4,item1
    def do_four2(f, val1, val2):
        f(val1, val2)
        f(val1, val2)
        f(val1, val2)
        f(val1, val2)
    draw_frame('+','-')
    do_four2(draw_frame, '|', ' ')
    draw_frame('+','-')
    do_four2(draw_frame, '|', ' ')
    draw_frame('+','-')
    
draw_grid()
print ''

# 2
def draw_grid2():
    def draw_frame(item1, item2):
        print item1,item2*4,item1,item2*4,item1,item2*4,item1,item2*4,item1
    def do_four2(f, val1, val2):
        f(val1, val2)
        f(val1, val2)
        f(val1, val2)
        f(val1, val2)
    def do_set(f, g, val1, val2, val3, val4):
        f(val1, val2)
        g(f, val3, val4)
        f(val1, val2)
        g(f, val3, val4)
        f(val1, val2)
        g(f, val3, val4)
        f(val1, val2)
        g(f, val3, val4)        
    do_set(draw_frame, do_four2, '+', '-', '|', ' ')
    draw_frame('+','-')

draw_grid2()