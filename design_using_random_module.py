import random
import turtle
t=turtle.Turtle()
t.speed(0)
w=turtle.Screen()
w.bgcolor("black")
colors=['red','blue','green','yellow','violet','sky blue','pink','orange']
for m in range(50):
	t.color(random.choice(colors))
	size=random.randint(10,40)
	x=random.randrange(-turtle.window_width()//2,turtle.window_width())
	y=random.randrange(-turtle.window_height()//2,turtle.window_height()//2)
	t.up()
	t.setposition(x,y)
	t.down()
	for n in range(size):
		t.fd(n*2)
		t.left(90)
t.up()
t.home()
turtle.mainloop()