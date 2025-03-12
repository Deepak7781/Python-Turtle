# color program(using list data strcture)
import turtle
t=turtle.Turtle()
t.speed(0)
w=turtle.Screen()
w.bgcolor("black")
sides=(5)
l=["red","indigo","blue","yellow","magenta"]
for x in range(200):
      t.color(l[x%sides])
      t.forward(x*3/sides+x)
      t.left(700/sides+7)
      t.width(x*sides/280)
t.hideturtle()
turtle.mainloop()