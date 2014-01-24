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
for i in range(4):
    fd(bob, 100)
    lt(bob)

# tells TurtleWorld to wait for the user to do something
wait_for_user()

# test