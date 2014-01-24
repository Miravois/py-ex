# Exercise 3.3
def right_justify(s):
    length = len(s)
    print " "*(70 - length) + s

# Exercise 3.4
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