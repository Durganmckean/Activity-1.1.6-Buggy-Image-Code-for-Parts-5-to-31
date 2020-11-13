#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()

# Create a spider body
spider.pensize(40)
spider.circle(20)

# Configure spider legs
legs = 6
leg_length = 70
degrees = 380 / legs
spider.pensize(5)

# Draw legs
leg_drawing = 0
while (leg_drawing < legs):
  spider.goto(0,0)
  spider.setheading(degrees*leg_drawing)
  spider.forward(leg_length)
  leg_drawing = leg_drawing + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()