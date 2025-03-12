#my creativity (using list data structure)
import turtle
t=turtle.Turtle()
t.speed(0)
w=turtle.Screen()
w.bgcolor("black")
sides=(10)
l=["red","blue","green","pink","indigo","light green","magenta","yellow","white","violet"]
for x in range(200):
      t.color(l[x%sides])
      t.forward(x*3/sides+x)
      t.left(600/sides+1)
      t.width(x*sides/444)
t.hideturtle()
turtle.mainloop()