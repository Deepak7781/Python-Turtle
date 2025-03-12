#my creativity
import turtle
t=turtle.Turtle()
t.speed(0)
w=turtle.Screen()
w.bgcolor("black")
s=["violet","green","yellow"]
for x in range(300):
      t.color(s[x%3])
      t.circle(x)
      t.left(103)
t.hideturtle()
turtle.mainloop()