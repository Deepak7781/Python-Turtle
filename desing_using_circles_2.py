#my design2
import turtle
t=turtle.Turtle()
t.speed(0)
w=turtle.Screen()
t.pencolor('magenta')
for x in range(150):
      t.forward(2*x)
      t.left(93)
      t.circle(45)
      t.left(9)
t.hideturtle()
turtle.mainloop()
