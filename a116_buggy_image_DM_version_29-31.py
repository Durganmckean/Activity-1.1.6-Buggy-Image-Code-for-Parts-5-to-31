#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()

# Create a spider body
spider.pensize(40)
spider.circle(20)

# Configure spider legs
legs = 4
leg_length = 70
angle = 120 / legs
spider.pensize(5)
limit = 0

# Draw legs
while (limit < legs):
  spider.goto(0,20)
  spider.setheading(angle*limit+45)
  spider.forward(leg_length)
  limit = limit + 1
limit = 0
angle = -120 / legs
while (limit < legs):
  spider.goto(0,20)
  spider.setheading(angle*limit-45)
  spider.forward(leg_length)
  limit = limit + 1

spider.penup()
spider.color("yellow")
spider.goto(10,40)
spider.pensize(10)
spider.pendown()
spider.circle(5)

spider.penup()
spider.goto(10,5)
spider.pensize(10)
spider.pendown()
spider.circle(5)

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()