# imports everything from the TurtleWorld module in the swampy package
from swampy.TurtleWorld import *

# creates a TurtleWorld assigned to world
world = TurtleWorld()
# creates a Turtle assigned to bob
bob = Turtle()
# yields <TurtleWorld.Turtle instance at 0xb7bfbf4c>
# bob refers to an instance of a Turtle as defined in module TurtleWorld
print bob

# fd for forward; bk for backward
# lt for left turn; rt for right turn
# pu for "pen up"; pd for "pen down"

# 1
'''
Write a function called square that takes a parameter named t, which is a turtle.
It should use the turtle to draw a square.
'''

# 2
'''
Add another parameter, named length, to square. Modify the body so length of the
sides is length, and then modify the function call to provide a second argument.
Run the program again. Test your program with a range of values for length.
'''

# 3
'''
The function lt and rt make 90-degree turns by default, but you can provide a 
second argument that specifies the number of degress. For example, lt(bob, 45)
turns bob 45 degrees to the left.
Make a copy of square and change the name to polygon. Add another parameter
named n and modify the body so it draws an n-sided regular polygon.
Hint: The exterior angles of an n-sided regular polygon are 360/n degrees.
'''

# 4
'''
Write a function called circle that takes a turtle, t, and radius, r, as
parameters and that draws an approximate circle by invoking polygon with an
appropriate length and number of sides. Test your function with a range of
values of r.
Hint: figure out the circumference of the circle and make sure that length * n
= circumference.
Hint: if bob is too slow for you, you can speed him up by changing bob.delay,
which is the time between moves, in seconds. bob.delay=0.01 ought to get him
moving.
'''

# 5
'''
Make a more general version of circle called arc that takes an additional 
parameter angle, which determines what fraction of a circle to draw. angle is
in units of degrees, so when angle=360, arc should draw a complete circle.
'''

# tells TurtleWorld to wait for the user to do something
wait_for_user()