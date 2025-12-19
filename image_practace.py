# Section 1 - Your code
from utils import *
set_background("cliff")
s2 = create_sprite("Grunt-Fish", -10, 0)

message1 = create_sprite("alien",-50,100)
message1.color("red")
message1.write("LAND FISH",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()