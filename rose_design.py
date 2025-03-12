# my creativity 2
import turtle
t=turtle.Turtle()
t.speed(0)
w=turtle.Screen()
w.bgcolor("black")
l=["white","red","blue","yellow"]
for x in range(300):
	t.color(l[x%4])
	t.forward(x)
	t.left(66)
t.hideturtle()
turtle.mainloop()