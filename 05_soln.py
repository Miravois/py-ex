# 1
'''
Fermat's Last Theorem says that there no integers a, b, and c such that 
a^n + b^n = c^n for any values of n greater than 2.

1. Write a function named check_fermat that takes four parameters - a, b, c, 
and n - and that checks to see if Fermat's theorem holds. If n is greater than
2 and it turns out to be true that the program should print, "Holy smokes, 
Fermat aws wrong!" Otherwise the program should print, "No, that doesn't work."

2. Write a function that prompts the user to input values for a, b, c, and n,
converts them to integers, and uses check_fermat to check whether they violate
Fermat's theorem.
'''
def check_fermat(a,b,c,n):
    if ((n > 2) and (a**n + b**n == c**n)):
        print "Holy smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."

def io_check_fermat():
    a = int(raw_input('Please input the value for a:\n'))
    b = int(raw_input('Please input the value for b:\n'))
    c = int(raw_input('Please input the value for c:\n'))
    n = int(raw_input('Please input the value for n:\n'))
    check_fermat(a, b, c, n)


# 2
'''
If you are given three sticks, you may or may not be able to arrange them in
a triangle. For example, if one of the sticks is 12 inches long and the other
two are 1 inch long, it is clear that you will not be able to get the short
sticks to meet in the middle. For any three lengths, there is a simple test to
see if it is possible to form a triangle:

If any of the three lengths is greater than the sum of the other two, then you
cannot form a triangle. Otherwise, you can.

1. Write a function named is_triangle that takes three integers as arguments, 
and that prints either "Yes" or "No", depending on whether you can or cannot
form a triangle from sticks with the given lengths.

2. Write a function that prompts the user to input three sticks lengths, 
converts them to integers, and uses is_triangle to check whether sticks with
the given lengths can form a triangle.
'''
def is_triangle(a,b,c):
    if (a+b > c or b+c > a or a+c > b):
        print 'Yes'
    else:
        print 'No'
        
def io_is_triangle():
    a = int(raw_input('Please input the first length:\n'))
    b = int(raw_input('Please input the first length:\n'))
    c = int(raw_input('Please input the first length:\n'))
    is_triangle(a, b, c)    